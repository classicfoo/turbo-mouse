# Introduction
turbo-mouse is a python script that allows easy desktop automation.

# Requirements

turbo-mouse requires a couple of packages:

pyautogui `pip install pyautogui`

pyperclip `pip install pyperclip`

# Usage

You can use the provided functions to automate various tasks on your computer. Here's how to use them:

### Double Click

Use the `double_click(x=None, y=None)` function to double-click at the specified coordinates `(x, y)`. If no coordinates are provided, it will double click where the cursor is.

### Single Click

Use the `single_click(x=None, y=None, button='left')` function to single-click at the specified coordinates `(x, y)` with the specified mouse button ('left', 'right', 'middle'). If no coordinates are provided, it will click where the cursor is.

### Right Click

Use the `right_click()` function to right-click at the current cursor position.

### Triple Click

Use the `triple_click(x=None, y=None)` function to triple click at the specified coordinates `(x, y)`. If no coordinates are provided, it will triple click where the cursor is.

### Move Cursor To

Use the `move_cursor_to(x, y)` function to move the cursor to the specified coordinates `(x, y)`.

### Get Cursor Position

Use the `get_cursor_position()` function to retrieve the current coordinates of the cursor.

### Copy Value

Use the `copy_value()` function to copy the selected text or content to the clipboard. It simulates pressing the 'Ctrl+C' keyboard shortcut.

### Paste Value

Use the `paste_value()` function to paste the trimmed content from the clipboard. It simulates pressing the 'Ctrl+V' keyboard shortcut after copying the trimmed value.

### Get Current Cursor Position

Use the `get_current_cursor_position()` function to print the current cursor position to the console.

### Wait

Use the `wait(seconds)` function to pause the script's execution for the specified number of seconds.

### Drag and Drop

Use the `drag_and_drop(start_x, start_y, end_x, end_y)` function to simulate clicking at `(start_x, start_y)`, dragging the cursor to `(end_x, end_y)`, and releasing the mouse button.

To start automating tasks, enter your automation instructions in the provided section within the script, and then run the script by executing it. For example:

```python
if __name__ == "__main__":
    # ENTER YOUR AUTOMATION INSTRUCTIONS HERE
    X = 0  # Replace 'X' with your specific instructions
```

Replace `X` with your custom automation instructions, and execute the script to automate tasks on your computer.

Feel free to customize the instructions further to suit your project's needs, and make sure to provide examples or additional details as necessary.
