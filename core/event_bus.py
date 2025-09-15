import queue
import threading

class EventBus:
    def __init__(self):
        self.queue = queue.Queue()
        self.listeners = {}

    def broadcast(self, event_type, **kwargs):
        self.queue.put((event_type, kwargs))

    def subscribe(self, event_type, callback):
        self.listeners.setdefault(event_type, []).append(callback)

    def once(self, event_type, callback):
        self.one_time_listeners.setdefault(event_type, []).append(callback)

    def dispatch_loop(self):
        while True:
            event_type, data = self.queue.get()
            for callback in self.listeners.get(event_type, []):
                callback(**data)
