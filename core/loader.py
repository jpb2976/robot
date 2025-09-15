import os
import importlib
import inspect

def load_modules_from(folder, bus):
    for filename in os.listdir(folder):
        if filename.endswith(".py") and not filename.startswith("__"):
            modulename = filename[:-3]

            try:
                module = importlib.import_module(f"{folder}.{modulename}")

                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if obj.__module__ == module.__name__:
                        cls = obj
                        cls(bus)
                        print(f"✅ Loaded {folder}/{cls.__name__}")
                        break
                else:
                    print(f"⚠️ No class found in {modulename}.py")

            except Exception as e:
                print(f"❌ Failed to load {modulename}.py: {e}")
