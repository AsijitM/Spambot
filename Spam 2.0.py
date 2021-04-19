from pynput.keyboard import Key, Controller
import time
 
message = "*Jai Hind*"
keyboard = Controller()
 
time.sleep(5)
 
for num in range(5000):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
