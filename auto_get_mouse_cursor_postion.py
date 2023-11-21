import pyautogui

def get_cursor_position():
    """ Return the current coordinates of the cursor """
    return pyautogui.position()

def get_current_cursor_position():
    # Get current cursor position
    x, y = get_cursor_position()
    print(f"Mouse cursor is currently at ({x}, {y})")

if __name__ == "__main__":
    get_current_cursor_position()

