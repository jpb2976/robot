class Startup:
    def __init__(self, bus):
        bus.on("system.startup", self.greet)

    def greet(self):
        print("🤖 Startup: Hello, I'm alive!")
