__author__ = "Chris Raitano"
__copyright__ = "Copyright 2018, Chris Raitano"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Chris Raitano"

'''
    ASCII codes to style command line interface output
'''

# Turn CSI styles off
RESET             = "\033[0m"

# CSI Styles
BOLD              = "\033[1m"
FAINT             = "\033[2m"
ITALIC            = "\033[3m"  # Not widely supported
UNDERLINE         = "\033[4m"
SLOW_BLINK        = "\033[5m"  # < 150 per minute
RAPID_BLINK       = "\033[6m"  # >= 150 per minute. Not widely supported
REVERSE           = "\033[7m"  # Swap foreground and background color
CONCEAL           = "\033[8m"  # Not widely supported
CROSSED_OUT       = "\033[9m"
DEFAULT_FONT      = "\033[10m"
ALT_FONT_1        = "\033[11m"
ALT_FONT_2        = "\033[12m"
ALT_FONT_3        = "\033[13m"
ALT_FONT_4        = "\033[14m"
ALT_FONT_5        = "\033[15m"
ALT_FONT_6        = "\033[16m"
ALT_FONT_7        = "\033[17m"
ALT_FONT_8        = "\033[18m"
ALT_FONT_9        = "\033[19m"
FRAKTUR           = "\033[20m" # Not widely supported
DOUBLE_UNDERLINE  = "\033[21m"
NORMAL_INTENSITY  = "\033[22m" # Not bold or faint
NOT_ITC_OR_FRAK   = "\033[23m" # Not italic or fraktur
NO_UNDERLINE      = "\033[24m"
NO_BLINK          = "\033[25m"
NO_INVERSE        = "\033[27m"
REVEAL            = "\033[28m" # No conceal
NO_CROSSED_OUT    = "\033[29m"
# 30-37 reserved for foreground (font) colors. See below
SET_FG_COLOR      = "\033[38m" # set foreground color
DEFAULT_FG_COLOR  = "\033[39m" # Restore the foreground color to default
# 40-47 reserved for background colors. See below
SET_BG_COLOR      = "\033[48m" # set background color
DEFAULT_BG_COLOR  = "\033[49m" # Restore the background color to default
FRAMED            = "\033[51m"
ENCIRCLED         = "\033[52m"
OVERLINED         = "\033[53m"
NO_FRAME          = "\033[54m" # also not encircled
NO_OVERLINE       = "\033[55m"
