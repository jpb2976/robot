from gtts import gTTS
from playsound import playsound
import tempfile
import threading
import queue
import os

class SpeechModule:
    def __init__(self, bus):
        self._queue = queue.Queue()
        bus.subscribe("robot.speak", self._on_speak)
        threading.Thread(target=self._loop, daemon=True).start()

    def _on_speak(self, text):
        self._queue.put(text)

    def _loop(self):
        while True:
            message = self._queue.get()
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                    tts = gTTS(text=message, lang='en', tld='com')
                    tts.save(fp.name)
                    temp_path = fp.name

                playsound(temp_path)
                os.remove(temp_path)
            except Exception as e:
                print("❌ TTS error:", e)
