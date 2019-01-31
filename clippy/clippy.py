__author__ = "Chris Raitano"
__copyright__ = "Copyright 2018, Chris Raitano"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Chris Raitano"

'''
' Command line interface helper methods
'''
import sys, termios, tty, os, fcntl
from clippy.misc import *

'''
' Set up a windowed cli session
'''
def init():
    print(controls.HIDE_CURSOR + controls.NEW_SCREEN_BUF)

'''
' Clean up cli session and restore terminal
'''
def close():
    print(controls.SHOW_CURSOR + controls.CLOSE_SCREEN_BUF)

'''
' Check if ascii value is a char
'   key (string): ascii value from keyboard
'   return (bolean): true if key represents a char
'                    false, otherwise
'''
def isChar(key):
    return len(key) == 1 and key >= keys.SPACE and key <= keys.SHIFT_GRAVE

'''
'  Check if ascii value is a digit
'    key (string): ascii value from keyboard
'    return (bolean): true if key represents a digit
'                     false, otherwise
'''
def isDigit(key):
    return key >= keys.ZERO and key <= keys.NINE

'''
' Read in a keypress
'   return (string): ascii value returned by keyboard for next keypress
'''
def get_key():
    # get file object, file descriptor and status flags for stdin
    file = sys.stdin
    fd = file.fileno()
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    # store the settings for stdin
    old_settings = termios.tcgetattr(fd)
    try:
        # turn off input pre-processing
        tty.setraw(fd)
        # blocking read. Get first char
        fcntl.fcntl(fd, fcntl.F_SETFL, flags & ~os.O_NONBLOCK)
        ch = file.read(1)
        # process escape codes
        if(ch == '\x1b'):
            # nonblocking read. Get any remaining chars
            fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
            x = ' '
            while(x):
                x = file.read(1)
                ch += x;
            # Restore blocking
            fcntl.fcntl(fd, fcntl.F_SETFL, flags & ~os.O_NONBLOCK)
    finally:
        # restore settings for stdin
        tty.setcbreak(fd)
        termios.tcsetattr(fd, termios.TCSANOW, old_settings)
    return ch

'''
' Print a menu item
'   num (int): number to display next to the item
'   name (string): text to display for the item
'   selected (boolean): true if item is currently seleccted
'                       false, otherwise
'     default: false, not selected
'   pre (string): text to display before item number.
'     default: 4 spaces for padding
'''
def print_item(num, name, selected = False, pre = '    '):
    print(pre, end='') # beginning spacer
    if(selected):
        print(styles.REVERSE, end='')
    print("{}. {}".format(num, name))
    if(selected):
        print(styles.RESET, end='')

'''
' Display a menu and get user's choice
'   items (list): the items to display in the menu
'   title (string): text to display at the top of the menu
'   return (int): negative int representing program exit signal
'''
def menu(items, title = ""):
    cursor_pos = 1
    # Print initial menu
    if title: print(title + "\n")
    print(controls.SAVE_POS, end = '');
    for i, item in enumerate(items):
        print_item(i + 1, item, i == 0)
    print(controls.RESTORE_POS, end='\r')
    # User interaction
    while(1):
        # Get keypress
        key = get_key()
        # Quit
        if(key == keys.CTRL_C or key == keys.CTRL_D):
            return -1
        # Select previous item
        elif key == keys.UP_ARROW and cursor_pos > 1:
            print(controls.CLR_LINE, end='')
            print_item(cursor_pos, items[cursor_pos - 1])
            cursor_pos -= 1
            print(controls.PREV_LINE + controls.PREV_LINE, end='')
            print_item(cursor_pos, items[cursor_pos - 1], True)
            print(controls.PREV_LINE, end='\r')
        # Select next item
        elif key == keys.DOWN_ARROW and cursor_pos < len(items):
            print(controls.CLR_LINE, end='')
            print_item(cursor_pos, items[cursor_pos - 1])
            cursor_pos += 1
            print_item(cursor_pos, items[cursor_pos - 1], True)
            print(controls.PREV_LINE, end='\r')
        # Clear menu and return selection
        elif key == keys.ENTER:
            print(controls.RESTORE_POS + controls.CLR_SCREEN_DOWN, end='\r')
            return cursor_pos

'''
' Get input from user
'   prompt (string): text to display to user
'   checkFunction (function): function to check if input chars are valid
'   return (string): User input
'             (int): -1 if ctrl+c or ctrl+d is pressed
'''
def input(prompt = "", checkFunction = isChar, allowEmpty = False):
    print(prompt, end = controls.SHOW_CURSOR, flush = True)
    index = 0
    out = ""
    while(1):
        key = get_key()
        # exit
        if(key == keys.CTRL_C or key == keys.CTRL_D):
            return -1
        # return user input
        elif(key == keys.ENTER and (len(out) > 0 or allowEmpty)):
            print(controls.HIDE_CURSOR)
            return out
        # delete char
        elif(key == keys.BACKSPACE and index > 0):
            out = out[:index - 1] + out[index:]
            index -= 1
            print(controls.LEFT + controls.CLR_LINE_RIGHT, end = '',flush = True)
            if(index < len(out)):
                print(out[index:] + "\033[" + str(len(out) - index) + "D", end = "", flush = True)
        # move cursor left
        elif(key == keys.LEFT_ARROW and index > 0):
            print(controls.LEFT, end = '', flush = True)
            index -= 1
        # move cursor right
        elif(key == keys.RIGHT_ARROW and index < len(out)):
            print(controls.RIGHT, end = '', flush = True)
            index += 1
        # get char
        elif(checkFunction(key)):
            out = out[:index] + key + out[index:]
            print(controls.CLR_LINE_RIGHT + out[index:], end = "", flush = True)
            if(index < len(out) - 1):
                print("\033[" + str(len(out) - index - 1) + "D", end = "", flush = True)
            index += 1

'''
' Get an integer input from user
'   prompt (string): text to display to the user
'   return (int): positive input by user, or
'                 negative if an error occurred
'''
def get_int(prompt = "", allowEmpty = False):    
    i = input(prompt, isDigit, allowEmpty)
    if i == "":
        return
    else:
        return int(i)
