import queue
import threading

class EventBus:
  def __init__(self):
    self.queue = queue.Queue()
    self.listeners = {}
    self.one_time_listeners = {}

  def broadcast(self, event_type, **kwargs):
    self.queue.put((event_type, kwargs))

  def subscribe(self, event_type, callback):
    self.listeners.setdefault(event_type, []).append(callback)
      
  def unsubscribe(self, event_type, callback):
    if event_type in self.listeners:
      try:
        self.listeners[event_type].remove(callback)
        if not self.listeners[event_type]:
          del self.listeners[event_type]
      except ValueError:
        pass
    if event_type in self.one_time_listeners:
      try:
        self.one_time_listeners[event_type].remove(callback)
        if not self.one_time_listeners[event_type]:
          del self.one_time_listeners[event_type]
      except ValueError:
        pass

  def once(self, event_type, callback):
    self.one_time_listeners.setdefault(event_type, []).append(callback)

  def dispatch_loop(self):
    while True:
      event_type, data = self.queue.get()
      for callback in self.listeners.get(event_type, []):
        callback(**data)
      for callback in self.one_time_listeners.pop(event_type, []):
        callback(**data)