__author__ = "Chris Raitano"
__copyright__ = "Copyright 2018, Chris Raitano"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Chris Raitano"

'''
    ASCII codes for command line interface controls
'''

# Enable/disable alternate screen buffer
NEW_SCREEN_BUF    = "\033[?1049h\033[H"
CLOSE_SCREEN_BUF  = "\033[?1049l"

# Turn bracketed mode on/off to prevent command execution
BRACKETED_ON      = "\033[?2004h"
BRACKETED_OFF     = "\033[?2004l"

# Move cursor 1 position
UP                = "\033[1A"
DOWN              = "\033[1B"
RIGHT             = "\033[1C"
LEFT              = "\033[1D"

# Move cursor to start of next or previous line
NEXT_LINE         = "\033[1E"
PREV_LINE         = "\033[1F"

# Get the current cursor position.
# Returns as keyboard output 'ESC[n;mR' where n is the row and m is the column
GET_CURSOR_POS    = "\033[6n"

# Set cursor to top left of screen
SET_CURSOR_0_0    = "\033[H"

# Save/Restore the cursor Position
SAVE_POS          = "\033[s"
RESTORE_POS       = "\033[u"

# Hide/Show the cursor
HIDE_CURSOR       = "\033[?25l"
SHOW_CURSOR       = "\033[?25h"

# Clear the screen
CLR_SCREEN        = "\033[2J" # Whole screen
CLR_SCREEN_UP     = "\033[1J" # Before cursor
CLR_SCREEN_DOWN   = "\033[0J" # AFter cursor
CLR_SCREEN_DEL    = "\033[3J" # Clear whole screen and delete scrollback buffer

# Clears the current line
CLR_LINE          = "\033[2K" # The whole line
CLR_LINE_LEFT     = "\033[1K" # Everything left of the cursor
CLR_LINE_RIGHT    = "\033[0K" # Everything right of the cursor

# Scroll the page up or down
SCROLL_UP         = "\033[1S"
SCROLL_DOWN       = "\033[1T"
