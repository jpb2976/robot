from datetime import datetime
import threading
import time

class TimeEvents:
  def __init__(self, bus):
    self._bus = bus
    self._last_second = None
    self._last_minute = None
    self._last_hour = None
    self._last_day = None
    self._last_month = None
    self._last_year = None
    threading.Thread(target=self._loop, daemon=True).start()
    
  def _loop(self):
    while True:
      now = datetime.now()
      
      if now.second != self._last_second:
        self._last_second = now.second
        self._bus.broadcast("time.second", now=now)
      
      if now.minute != self._last_minute:
        self._last_minute = now.minute
        self._bus.broadcast("time.minute", now=now)
      
      if now.hour != self._last_hour:
        self._last_hour = now.hour
        self._bus.broadcast("time.hour", now=now)
      
      if now.day != self._last_day:
        self._last_day = now.day
        self._bus.broadcast("time.day", now=now)
      
      if now.month != self._last_month:
        self._last_month = now.month
        self._bus.broadcast("time.month", now=now)
      
      if now.year != self._last_year:
        self._last_year = now.year
        self._bus.broadcast("time.year", now=now)
      
      time_to_sleep = 1.0 - (time.time() % 1.0)
      time.sleep(time_to_sleep)