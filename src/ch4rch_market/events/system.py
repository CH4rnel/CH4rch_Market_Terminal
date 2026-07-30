from dataclasses import dataclass

from .base import Event


@dataclass
class SystemStarted(Event):

    def __init__(self):
        super().__init__(
            event_type="system.started"
        )


@dataclass
class SystemStopped(Event):

    def __init__(self):
        super().__init__(
            event_type="system.stopped"
        )
