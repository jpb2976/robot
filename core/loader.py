import os
import importlib

def snake_to_pascal(name):
    return ''.join(word.capitalize() for word in name.split('_'))

def load_modules_from(folder, bus):
    for filename in os.listdir(folder):
        if filename.endswith(".py") and not filename.startswith("__"):
            modulename = filename[:-3]
            classname = snake_to_pascal(modulename)
            try:
                module = importlib.import_module(f"{folder}.{modulename}")
                cls = getattr(module, classname)
                cls(bus)
                print(f"✅ Loaded {folder}/{classname}")
            except Exception as e:
                print(f"❌ Failed to load {classname}: {e}")
