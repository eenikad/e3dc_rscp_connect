"This file contains the RscpHandlerPipeline."

import logging
from .RscpModelInterface import RscpModelInterface

_LOGGER = logging.getLogger(__name__)


class RscpHandlerPipeline:
    def __init__(self):
        self._handlers = []

    def add_handler(self, handler: RscpModelInterface):
        self._handlers.append(handler)

    async def process(self, values):
        """Process a list of RSCP values."""
        for value in values:
            handled = False

            for handler in self._handlers:
                if handler.handle_rscp_data(value):
                    handled = True
                    break

            if not handled:
                _LOGGER.warning("Unhandled RSCP tag: %s", value.getTagName())
