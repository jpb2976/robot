from core.event_bus import EventBus
from core.loader import load_modules_from
import threading

bus = EventBus()

load_modules_from("modules", bus)

bus.emit("system.startup")

bus.dispatch_loop()
