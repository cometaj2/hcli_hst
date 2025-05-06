import json
import io
import service
import logger
from utils import formatting

from typing import Optional, Dict, Callable, List

logging = logger.Logger()
logging.setLevel(logger.INFO)


class CLI:
    def __init__(self, commands: List[str], inputstream: Optional[io.BytesIO] = None):
        self.commands = commands
        self.inputstream = inputstream
        self.service = service.Service()
        self.handlers: Dict[str, Callable] = {
            'ship': self._handle_ship
        }

    def execute(self) -> Optional[io.BytesIO]:
        if len(self.commands) == 1 and self.inputstream:
            response = self.service.chat(self.inputstream)
            return io.BytesIO(response.encode('utf-8'))

        if len(self.commands) > 1 and self.commands[1] in self.handlers:
            return self.handlers[self.commands[1]]()

        return None

    def _handle_ship(self) -> None:
        if len(self.commands) == 3:
            if self.commands[2] == "status":
                return io.BytesIO(self.service.status().encode('utf-8'))
        return None
