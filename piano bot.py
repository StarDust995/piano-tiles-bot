import pyautogui
import keyboard
import win32api,win32con
import time

def mouseclick(x,y):
    """
    a function that makes the mouse clicks at a certain position(x,y)
    
    """
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    
    #holding the click for .02 seconds so that it registers
    #(manipulate this till you find the sweet spot)
    time.sleep(0.02) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



while keyboard.is_pressed('p')==False: #'p' to break the while loop
    if pyautogui.pixel(386,390)[0]==0: #adjust the .pixel(x,y) to your specific tile position on the monitor
        mouseclick(386,390)            #[0] to specifiy the red color
                                       # black pixel on the tile has rgb value of(0,0,0)
    if pyautogui.pixel(460,390)[0]==0:
        mouseclick(460,390) #mouse click once the specific pixel's red value becomes 0, indicating a black tiel
    if pyautogui.pixel(540,390)[0]==0:
        mouseclick(540,390)
    if pyautogui.pixel(610,390)[0]==0:
        mouseclick(610,390)
    
    

#expiremental values of mouse position and rgb values using pyautogui.displaymouse position()
#X:  342 Y:  560 RGB: (  0,   0,   0)
#X:  437 Y:  560 RGB: (  0,   0,   0)
#X:  550 Y:  560 RGB: (  0,   0,   0)
#X:  662 Y:  560 RGB: (  0,   0,   0)
