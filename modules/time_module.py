class TimeModule:
  def __init__(self, bus):
    bus.subscribe("time.second", self.announce_second)
    
  def announce_second(self, now):
    print(f"⏰ SecondAnnouncer: The time is now {now.strftime('%H:%M:%S')}")