class StartupModule:
  def __init__(self, bus):
    bus.subscribe("system.startup", self.greet)

  def greet(self):
    print("🤖 Startup: Hello, I'm alive!")