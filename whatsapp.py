import pyautogui as p
import time
import pyperclip  # To copy emoji text to clipboard

time.sleep(5)  # Time to switch to WhatsApp Web

message = "😇😂"

for i in range(100):
    pyperclip.copy(message)  # Copy to clipboard
    p.hotkey("ctrl", "v")    # Paste using Ctrl+V
    p.press("enter")
