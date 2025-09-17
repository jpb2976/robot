import os
os.environ["PATH"] += os.pathsep + r"C:\Users\plane\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0-full_build\bin"
import whisper
import sounddevice as sd
import numpy as np
import tempfile
import threading
import wave

class ListenModule:
    def __init__(self, bus):
        self._bus = bus
        self._model = whisper.load_model("base")
        bus.subscribe("audio.wake_word", self._listen)

    def _listen(self):
        print("🎙️ Listening for voice command...")

        duration = 3
        sample_rate = 16000

        audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()
        audio = audio.flatten()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            with wave.open(tmp.name, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(sample_rate)
                wf.writeframes(audio.tobytes())

            print("⏳ Transcribing...")
            result = self._model.transcribe(tmp.name)
            command = result["text"].strip()

            print(f"🧠 Recognized: {command}")
            self._bus.broadcast("audio.heard", text=command)
