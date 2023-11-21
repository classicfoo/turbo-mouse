import pyautogui
import time
import pyperclip

def double_click(x=None, y=None):
    """ Double click at (x, y). If no coordinates are provided, it will double click where the cursor is. """
    pyautogui.doubleClick(x, y)

def single_click(x=None, y=None, button='left'):
    """ Single click at (x, y) with specified button ('left', 'right', 'middle'). 
    If no coordinates are provided, it will click where the cursor is. """
    pyautogui.click(x, y, button=button)

def right_click():
    """ Right-click at the current cursor position. """
    pyautogui.rightClick()

def triple_click(x=None, y=None):
    """ Triple click at (x, y). If no coordinates are provided, it will triple click where the cursor is. """
    if x is None or y is None:
        x, y = pyautogui.position()
    
    pyautogui.click(x, y, clicks=3, interval=0.2)  # Click three times with a 0.2-second interval


def move_cursor_to(x, y):
    """ Move the cursor to (x, y) """
    pyautogui.moveTo(x, y)

def get_cursor_position():
    """ Return the current coordinates of the cursor """
    return pyautogui.position()

def copy_value():
    """ Copy value to clipboard """
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Give some time for copying to complete
    

def paste_value():
    """ Paste trimmed value from clipboard """
    clipboard_content = pyperclip.paste().strip()  # Get clipboard content and trim it
    pyperclip.copy(clipboard_content)  # Copy the trimmed content back to the clipboard
    pyautogui.hotkey('ctrl', 'v')  # Paste the trimmed value

def get_current_cursor_position():
    # Get current cursor position
    x, y = get_cursor_position()
    print(f"Cursor is currently at ({x}, {y})")

def wait(seconds):
    """ Wait for the specified number of seconds """
    time.sleep(seconds)

def drag_and_drop(start_x, start_y, end_x, end_y):
    """ Click at (start_x, start_y), drag the cursor to (end_x, end_y), and release the mouse button. """
    pyautogui.mouseDown(x=start_x, y=start_y)
    pyautogui.moveTo(end_x, end_y)
    pyautogui.mouseUp()


if __name__ == "__main__":

    # ENTER YOUR AUTOMATION INSTRUCTIONS HERE

    X = 0