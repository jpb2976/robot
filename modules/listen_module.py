class ListenModule:
    def __init__(self, bus):
        self._bus = bus
        bus.subscribe("audio.wake_word", self._listen)

    def _listen(self, text):
        pass
