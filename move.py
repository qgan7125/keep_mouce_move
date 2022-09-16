import pyautogui
import time
import random
import tkinter

def getScreenSize():
    """
    Purpose: a function to get screen size
    """
    root = tkinter.Tk()
    root.withdraw()
    return (root.winfo_screenwidth(), root.winfo_screenheight())

def randomMoveMouce(width: 500, height: 500, sleep: 2):
    while True:
        x = random.randint(0, width)
        y = random.randint(0, height)
        pyautogui.moveTo(x, y)

        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)

        print("Moved at {} ({} , {})".format(str(result), str(x), str(y)))
        time.sleep(2)

def main():
    width, height = getScreenSize()
    randomMoveMouce(width, height, 2)

if __name__ == "__main__":
    main()