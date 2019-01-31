__author__ = "Chris Raitano"
__copyright__ = "Copyright 2018, Chris Raitano"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Chris Raitano"

'''
    ASCII Keyboard input codes
        Key codes may vary by system. Use the get_key_code.py script to
        determine key codes for your system and modify this file as necessary
'''

# Grouped based on US keyboard layout

# --------------------------------- Arrow Keys ---------------------------------

UP_ARROW                     = "\x1b\x5b\x41"
DOWN_ARROW                   = "\x1b\x5b\x42"
RIGHT_ARROW                  = "\x1b\x5b\x43"
LEFT_ARROW                   = "\x1b\x5b\x44"

SHIFT_UP_ARROW               = "\x1b\x5b\x31\x3b\x32\x41"
SHIFT_DOWN_ARROW             = "\x1b\x5b\x31\x3b\x32\x42"
SHIFT_RIGHT_ARROW            = "\x1b\x5b\x31\x3b\x32\x43"
SHIFT_LEFT_ARROW             = "\x1b\x5b\x31\x3b\x32\x44"

ALT_UP_ARROW                 = "\x1b\x5b\x31\x3b\x33\x41"
ALT_DOWN_ARROW               = "\x1b\x5b\x31\x3b\x33\x42"
ALT_RIGHT_ARROW              = "\x1b\x5b\x31\x3b\x33\x43"
ALT_LEFT_ARROW               = "\x1b\x5b\x31\x3b\x33\x44"

ALT_SHIFT_UP_ARROW           = "\x1b\x5b\x31\x3b\x34\x41"
ALT_SHIFT_DOWN_ARROW         = "\x1b\x5b\x31\x3b\x34\x42"
ALT_SHIFT_RIGHT_ARROW        = "\x1b\x5b\x31\x3b\x34\x43"
ALT_SHIFT_LEFT_ARROW         = "\x1b\x5b\x31\x3b\x34\x44"

CTRL_UP_ARROW                = "\x1b\x5b\x31\x3b\x35\x41"
CTRL_DOWN_ARROW              = "\x1b\x5b\x31\x3b\x35\x42"
CTRL_RIGHT_ARROW             = "\x1b\x5b\x31\x3b\x35\x43"
CTRL_LEFT_ARROW              = "\x1b\x5b\x31\x3b\x35\x44"

CTRL_SHIFT_UP_ARROW          = "\x1b\x5b\x31\x3b\x36\x41"
CTRL_SHIFT_DOWN_ARROW        = "\x1b\x5b\x31\x3b\x36\x42"
CTRL_SHIFT_RIGHT_ARROW       = "\x1b\x5b\x31\x3b\x36\x43"
CTRL_SHIFT_LEFT_ARROW        = "\x1b\x5b\x31\x3b\x36\x44"

CTRL_ALT_UP_ARROW            = "\x1b\x5b\x31\x3b\x37\x41"
CTRL_ALT_DOWN_ARROW          = "\x1b\x5b\x31\x3b\x37\x42"
CTRL_ALT_RIGHT_ARROW         = "\x1b\x5b\x31\x3b\x37\x43"
CTRL_ALT_LEFT_ARROW          = "\x1b\x5b\x31\x3b\x37\x44"

CTRL_ALT_SHIFT_UP_ARROW      = "\x1b\x5b\x31\x3b\x38\x41"
CTRL_ALT_SHIFT_DOWN_ARROW    = "\x1b\x5b\x31\x3b\x38\x42"
CTRL_ALT_SHIFT_RIGHT_ARROW   = "\x1b\x5b\x31\x3b\x38\x43"
CTRL_ALT_SHIFT_LEFT_ARROW    = "\x1b\x5b\x31\x3b\x38\x44"

# --------------------------------- First Row ----------------------------------

ESC                          = "\x1b" # ESC, Escape
SHIFT_ESC                    = "\x1b" # ESC, Escape
ALT_ESC                      = "\x1b\x1b"
ALT_SHIFT_ESC                = "\x1b\x1b"
CTRL_ESC                     = "\x1b" # ESC, Escape
CTRL_SHIFT_ESC               = "\x1b" # ESC, Escape
CTRL_ALT_SHIFT_ESC           = "\x1b\x1b"

# F1-F12 Not implemented since these are often captured by OS

# --------------------------------- Second Row ---------------------------------

GRAVE                        = "\x60"
ONE                          = "\x31"
TWO                          = "\x32"
THREE                        = "\x33"
FOUR                         = "\x34"
FIVE                         = "\x35"
SIX                          = "\x36"
SEVEN                        = "\x37"
EIGHT                        = "\x38"
NINE                         = "\x39"
ZERO                         = "\x30"
MINUS                        = "\x2d"
EQUALS                       = "\x3d"
BACKSPACE                    = "\x7f"

SHIFT_GRAVE                  = "\x7e"
SHIFT_1                      = "\x21"
SHIFT_2                      = "\x40"
SHIFT_3                      = "\x23"
SHIFT_4                      = "\x24"
SHIFT_5                      = "\x25"
SHIFT_6                      = "\x5e"
SHIFT_7                      = "\x26"
SHIFT_8                      = "\x2a"
SHIFT_9                      = "\x28"
SHIFT_0                      = "\x29"
SHIFT_MINUS                  = "\x5f"
SHIFT_EQUALS                 = "\x2b"
SHIFT_BACKSPACE              = "\x7f"

ALT_GRAVE                    = "\x1b\x60"
ALT_1                        = "\x1b\x31"
ALT_2                        = "\x1b\x32"
ALT_3                        = "\x1b\x33"
ALT_4                        = "\x1b\x34"
ALT_5                        = "\x1b\x35"
ALT_6                        = "\x1b\x36"
ALT_7                        = "\x1b\x37"
ALT_8                        = "\x1b\x38"
ALT_9                        = "\x1b\x39"
ALT_0                        = "\x1b\x30"
ALT_MINUS                    = "\x1b\x2d"
ALT_EQUALS                   = "\x1b\x3d"
ALT_BACKSPACE                = "\x1b\x7f"

ALT_SHIFT_GRAVE              = "\x1b\x7e"
ALT_SHIFT_1                  = "\x1b\x21"
ALT_SHIFT_2                  = "\x1b\x40"
ALT_SHIFT_3                  = "\x1b\x23"
ALT_SHIFT_4                  = "\x1b\x24"
ALT_SHIFT_5                  = "\x1b\x25"
ALT_SHIFT_6                  = "\x1b\x5e"
ALT_SHIFT_7                  = "\x1b\x26"
ALT_SHIFT_8                  = "\x1b\x2a"
ALT_SHIFT_9                  = "\x1b\x28"
ALT_SHIFT_0                  = "\x1b\x29"
ALT_SHIFT_MINUS              = "\x1b\x5f"
ALT_SHIFT_EQUALS             = "\x1b\x2b"
ALT_SHIFT_BACKSPACE          = "\x1b\x7f"

CTRL_GRAVE                   = "\x00" # NUL, Null
CTRL_1                       = "\x31"
CTRL_2                       = "\x00" # NUL, Null
CTRL_3                       = "\x1b" # ESC, Escape
CTRL_4                       = "\x1c" # FS, File Separator
CTRL_5                       = "\x1d" # GS, Group Separator
CTRL_6                       = "\x1e" # RS, Record Separator
CTRL_7                       = "\x1f"
CTRL_8                       = "\x7f"
CTRL_9                       = "\x39"
CTRL_0                       = "\x30"
CTRL_MINUS                   = "\x1f" # US, Unit Separator
CTRL_EQUALS                  = "\x3d"
CTRL_BACKSPACE               = "\x08"

CTRL_SHIFT_GRAVE             = "\x1e"
CTRL_SHIFT_1                 = "\x21"
CTRL_SHIFT_2                 = "\x00"
CTRL_SHIFT_3                 = "\x23"
CTRL_SHIFT_4                 = "\x24"
CTRL_SHIFT_5                 = "\x25"
CTRL_SHIFT_6                 = "\x1e"
CTRL_SHIFT_7                 = "\x26"
CTRL_SHIFT_8                 = "\x2a"
CTRL_SHIFT_9                 = "\x28"
CTRL_SHIFT_0                 = "\x29"
CTRL_SHIFT_MINUS             = "\x1f"
CTRL_SHIFT_EQUALS            = "\x2b"
CTRL_SHIFT_BACKSPACE         = "\x08"

CTRL_ALT_GRAVE               = "\x1b\x00"
CTRL_ALT_1                   = "\x1b\x31"
CTRL_ALT_2                   = "\x00"
CTRL_ALT_3                   = "\x1b"
CTRL_ALT_4                   = "\x1c"
CTRL_ALT_5                   = "\x1d"
CTRL_ALT_6                   = "\x1e"
CTRL_ALT_7                   = "\x1f"
CTRL_ALT_8                   = "\x7f"
CTRL_ALT_9                   = "\x1b\x39"
CTRL_ALT_0                   = "\x1b\x30"
CTRL_ALT_MINUS               = "\x1f"
CTRL_ALT_EQUALS              = "\x1b\x3d"
CTRL_ALT_BACKSPACE           = "\x1b\x08"

CTRL_ALT_SHIFT_GRAVE         = "\x1b\x1e"
CTRL_ALT_SHIFT_1             = "\x1b\x21"
CTRL_ALT_SHIFT_2             = "\x1b\x00"
CTRL_ALT_SHIFT_3             = "\x1b\x23"
CTRL_ALT_SHIFT_4             = "\x1b\x24"
CTRL_ALT_SHIFT_5             = "\x1b\x25"
CTRL_ALT_SHIFT_6             = "\x1b\x1e"
CTRL_ALT_SHIFT_7             = "\x1b\x26"
CTRL_ALT_SHIFT_8             = "\x1b\x2a"
CTRL_ALT_SHIFT_9             = "\x1b\x28"
CTRL_ALT_SHIFT_0             = "\x1b\x29"
CTRL_ALT_SHIFT_MINUS         = "\x1b\x1f"
CTRL_ALT_SHIFT_EQUALS        = "\x1b\x2b"
CTRL_ALT_SHIFT_BACKSPACE     = "\x1b\x08"

# --------------------------------- Third Row ----------------------------------

TAB                          = "\x09"
Q                            = "\x71"
W                            = "\x77"
E                            = "\x65"
R                            = "\x72"
T                            = "\x74"
Y                            = "\x79"
U                            = "\x75"
I                            = "\x69"
O                            = "\x6f"
P                            = "\x70"
OPEN_BRAC                    = "\x5b"
CLOSE_BRCK                   = "\x5d"
BACKSLASH                    = "\x5c"

SHIFT_TAB                    = "\x1b\x5b\x5a"
SHIFT_Q                      = "\x51"
SHIFT_W                      = "\x57"
SHIFT_E                      = "\x45"
SHIFT_R                      = "\x52"
SHIFT_T                      = "\x54"
SHIFT_Y                      = "\x59"
SHIFT_U                      = "\x55"
SHIFT_I                      = "\x49"
SHIFT_O                      = "\x4f"
SHIFT_P                      = "\x50"
SHIFT_OPEN_BRAC              = "\x7b"
SHIFT_CLOSE_BRCK             = "\x7d"
SHIFT_BACKSLASH              = "\x7c"

# ALT_TAB                      = ""
ALT_Q                        = "\x1b\x71"
ALT_W                        = "\x1b\x77"
ALT_E                        = "\x1b\x65"
ALT_R                        = "\x1b\x72"
ALT_T                        = "\x1b\x74"
ALT_Y                        = "\x1b\x79"
ALT_U                        = "\x1b\x75"
ALT_I                        = "\x1b\x69"
ALT_O                        = "\x1b\x6f"
ALT_P                        = "\x1b\x70"
ALT_OPEN_BRAC                = "\x1b\x5b"
ALT_CLOSE_BRCK               = "\x1b\x5d"
ALT_BACKSLASH                = "\x1b\x5c"

# ALT_SHIFT_TAB                = ""
ALT_SHIFT_Q                  = "\x1b\x51"
ALT_SHIFT_W                  = "\x1b\x57"
ALT_SHIFT_E                  = "\x1b\x45"
ALT_SHIFT_R                  = "\x1b\x52"
ALT_SHIFT_T                  = "\x1b\x54"
ALT_SHIFT_Y                  = "\x1b\x59"
ALT_SHIFT_U                  = "\x1b\x55"
ALT_SHIFT_I                  = "\x1b\x49"
ALT_SHIFT_O                  = "\x1b\x4f"
ALT_SHIFT_P                  = "\x1b\x50"
ALT_SHIFT_OPEN_BRAC          = "\x1b\x7b"
ALT_SHIFT_CLOSE_BRCK         = "\x1b\x7d"
ALT_SHIFT_BACKSLASH          = "\x1b\x7c"

CTRL_TAB                     = "\x09"
CTRL_Q                       = "\x11" # DC1, Device Control 1
CTRL_W                       = "\x17" # CAN, End of Transmission Block
CTRL_E                       = "\x05" # ENQ, Enquiry
CTRL_R                       = "\x12" # DC2, Device Control 2
CTRL_T                       = "\x14" # DC4, Device Control 4
CTRL_Y                       = "\x19" # EM, End of Medium
CTRL_U                       = "\x15" # NAK, Negative Acknowledge
CTRL_I                       = "\x09" # HT, Horizontal Tabulation
CTRL_O                       = "\x0f" # SI, Shift In
CTRL_P                       = "\x10" # DLE, Data Link Escape
CTRL_OPEN_BRAC               = "\x1b" # ESC, Escape
CTRL_CLOSE_BRCK              = "\x1d" # GS, Group Separator
CTRL_BACKSLASH               = "\x1c" # FS, File Separator

CTRL_ALT_TAB                 = "\x1b\x09"
CTRL_ALT_Q                   = "\x1b\x11"
CTRL_ALT_W                   = "\x1b\x17"
CTRL_ALT_E                   = "\x1b\x05"
CTRL_ALT_R                   = "\x1b\x12"
CTRL_ALT_T                   = "\x1b\x14"
CTRL_ALT_Y                   = "\x1b\x19"
CTRL_ALT_U                   = "\x1b\x15"
CTRL_ALT_I                   = "\x1b\x09"
CTRL_ALT_O                   = "\x1b\x0f"
CTRL_ALT_P                   = "\x1b\x10"
CTRL_ALT_OPEN_BRAC           = "\x1b\x1b"
CTRL_ALT_CLOSE_BRCK          = "\x1b\x1d"
CTRL_ALT_BACKSLASH           = "\x1b\x1c"

CTRL_SHIFT_TAB               = "\x1b\x5b\x5a"
CTRL_SHIFT_Q                 = "\x11"
CTRL_SHIFT_W                 = "\x17"
# CTRL_SHIFT_E                 = ""
CTRL_SHIFT_R                 = "\x12"
CTRL_SHIFT_T                 = "\x14"
CTRL_SHIFT_Y                 = "\x19"
# CTRL_SHIFT_U                 = ""
CTRL_SHIFT_I                 = "\x09"
CTRL_SHIFT_O                 = "\x0f"
CTRL_SHIFT_P                 = "\x10"
CTRL_SHIFT_OPEN_BRAC         = "\x1b"
CTRL_SHIFT_CLOSE_BRCK        = "\x1d"
CTRL_SHIFT_BACKSLASH         = "\x1c"

CTRL_ALT_SHIFT_TAB           = "\x1b\x5b\x5a"
CTRL_ALT_SHIFT_Q             = "\x1b\x11"
CTRL_ALT_SHIFT_W             = "\x1b\x17"
CTRL_ALT_SHIFT_E             = "\x1b\x05"
CTRL_ALT_SHIFT_R             = "\x1b\x12"
CTRL_ALT_SHIFT_T             = "\x1b\x14"
CTRL_ALT_SHIFT_Y             = "\x1b\x19"
CTRL_ALT_SHIFT_U             = "\x1b\x15"
CTRL_ALT_SHIFT_I             = "\x1b\x09"
CTRL_ALT_SHIFT_O             = "\x1b\x0f"
CTRL_ALT_SHIFT_P             = "\x1b\x10"
CTRL_ALT_SHIFT_OPEN_BRAC     = "\x1b\x1b"
CTRL_ALT_SHIFT_CLOSE_BRCK    = "\x1b\x1d"
CTRL_ALT_SHIFT_BACKSLASH     = "\x1b\x1c"

# --------------------------------- Fourth Row ---------------------------------

A                            = "\x61"
S                            = "\x73"
D                            = "\x64"
F                            = "\x66"
G                            = "\x67"
H                            = "\x68"
J                            = "\x6a"
K                            = "\x6b"
L                            = "\x6c"
SEMICOLON                    = "\x3b"
QUOTE                        = "\x27"
ENTER                        = "\x0d"

SHIFT_A                      = "\x41"
SHIFT_S                      = "\x53"
SHIFT_D                      = "\x44"
SHIFT_F                      = "\x46"
SHIFT_G                      = "\x47"
SHIFT_H                      = "\x48"
SHIFT_J                      = "\x4a"
SHIFT_K                      = "\x4b"
SHIFT_L                      = "\x4c"
SHIFT_SEMICOLON              = "\x3a"
SHIFT_QUOTE                  = "\x22"
SHIFT_ENTER                  = "\x0d"

ALT_A                        = ""
ALT_S                        = ""
ALT_D                        = ""
ALT_F                        = ""
ALT_G                        = ""
ALT_H                        = ""
ALT_J                        = ""
ALT_K                        = ""
ALT_L                        = ""
ALT_SEMICOLON                = ""
ALT_QUOTE                    = ""
ALT_ENTER                    = ""

ALT_SHIFT_A                  = ""
ALT_SHIFT_S                  = ""
ALT_SHIFT_D                  = ""
ALT_SHIFT_F                  = ""
ALT_SHIFT_G                  = ""
ALT_SHIFT_H                  = ""
ALT_SHIFT_J                  = ""
ALT_SHIFT_K                  = ""
ALT_SHIFT_L                  = ""
ALT_SHIFT_SEMICOLON          = ""
ALT_SHIFT_QUOTE              = ""
ALT_SHIFT_ENTER              = ""

CTRL_A                       = "\x01" # SOH, Start of heading
CTRL_S                       = "\x13" # DC3, Device Control 3
CTRL_D                       = "\x04" # EOT, End of transmission
CTRL_F                       = "\x06" # ACK, Acknowledge
CTRL_G                       = "\x07" # BEL, Bell
CTRL_H                       = "\x08" # BS, Backspace
CTRL_J                       = "\x0a" # LF, Line Feed
CTRL_K                       = "\x0b" # VT, Vertical Tabulation
CTRL_L                       = "\x0c" # FF, Form Feed
CTRL_SEMICOLON               = "\x3b"
CTRL_QUOTE                   = "\x27"
CTRL_ENTER                   = "\x0d"

CTRL_SHIFT_A                 = ""
CTRL_SHIFT_S                 = ""
CTRL_SHIFT_D                 = ""
CTRL_SHIFT_F                 = ""
CTRL_SHIFT_G                 = ""
CTRL_SHIFT_H                 = ""
CTRL_SHIFT_J                 = ""
CTRL_SHIFT_K                 = ""
CTRL_SHIFT_L                 = ""
CTRL_SHIFT_SEMICOLON         = ""
CTRL_SHIFT_QUOTE             = ""
CTRL_SHIFT_ENTER             = ""

CTRL_ALT_A                   = ""
CTRL_ALT_S                   = ""
CTRL_ALT_D                   = ""
CTRL_ALT_F                   = ""
CTRL_ALT_G                   = ""
CTRL_ALT_H                   = ""
CTRL_ALT_J                   = ""
CTRL_ALT_K                   = ""
CTRL_ALT_L                   = ""
CTRL_ALT_SEMICOLON           = ""
CTRL_ALT_QUOTE               = ""
CTRL_ALT_ENTER               = ""

CTRL_ALT_SHIFT_A             = ""
CTRL_ALT_SHIFT_S             = ""
CTRL_ALT_SHIFT_D             = ""
CTRL_ALT_SHIFT_F             = ""
CTRL_ALT_SHIFT_G             = ""
CTRL_ALT_SHIFT_H             = ""
CTRL_ALT_SHIFT_J             = ""
CTRL_ALT_SHIFT_K             = ""
CTRL_ALT_SHIFT_L             = ""
CTRL_ALT_SHIFT_SEMICOLON     = ""
CTRL_ALT_SHIFT_QUOTE         = ""
CTRL_ALT_SHIFT_ENTER         = ""

# --------------------------------- Fifth Row ----------------------------------

Z                            = "\x7a"
X                            = "\x78"
C                            = "\x63"
V                            = "\x76"
B                            = "\x62"
N                            = "\x6e"
M                            = "\x6d"
COMMA                        = "\x2c"
PERIOD                       = "\x2e"
FORWARD_SLASH                = "\x2f"

SHIFT_Z                      = "\x5a"
SHIFT_X                      = "\x58"
SHIFT_C                      = "\x43"
SHIFT_V                      = "\x56"
SHIFT_B                      = "\x42"
SHIFT_N                      = "\x4e"
SHIFT_M                      = "\x4d"
SHIFT_COMMA                  = "\x3c"
SHIFT_PERIOD                 = "\x3e"
SHIFT_FORWARD_SLASH          = "\x3f"

ALT_Z                        = ""
ALT_X                        = ""
ALT_C                        = ""
ALT_V                        = ""
ALT_B                        = ""
ALT_N                        = ""
ALT_M                        = ""
ALT_COMMA                    = ""
ALT_PERIOD                   = ""
ALT_FORWARD_SLASH            = ""

ALT_SHIFT_Z                  = ""
ALT_SHIFT_X                  = ""
ALT_SHIFT_C                  = ""
ALT_SHIFT_V                  = ""
ALT_SHIFT_B                  = ""
ALT_SHIFT_N                  = ""
ALT_SHIFT_M                  = ""
ALT_SHIFT_COMMA              = ""
ALT_SHIFT_PERIOD             = ""
ALT_SHIFT_FORWARD_SLASH      = ""

CTRL_Z                       = "\x1a" # SUB, Substitute
CTRL_X                       = "\x18" # ETB, Cancel
CTRL_C                       = "\x03" # ETX, End of text
CTRL_V                       = "\x16" # SYN, Synchronous IDLE
CTRL_B                       = "\x02" # STX, Start of text
CTRL_N                       = "\x0e" # CR, Carriage Return
CTRL_M                       = "\x0d" # SO, Shift Out
CTRL_COMMA                   = "\x2c"
CTRL_PERIOD                  = "\x2e"
CTRL_FORWARD_SLASH           = "\x1f"

CTRL_SHIFT_Z                 = ""
CTRL_SHIFT_X                 = ""
CTRL_SHIFT_C                 = ""
CTRL_SHIFT_V                 = ""
CTRL_SHIFT_B                 = ""
CTRL_SHIFT_N                 = ""
CTRL_SHIFT_M                 = ""
CTRL_SHIFT_COMMA             = ""
CTRL_SHIFT_PERIOD            = ""
CTRL_SHIFT_FORWARD_SLASH     = ""

CTRL_ALT_Z                   = ""
CTRL_ALT_X                   = ""
CTRL_ALT_C                   = ""
CTRL_ALT_V                   = ""
CTRL_ALT_B                   = ""
CTRL_ALT_N                   = ""
CTRL_ALT_M                   = ""
CTRL_ALT_COMMA               = ""
CTRL_ALT_PERIOD              = ""
CTRL_ALT_FORWARD_SLASH       = ""

CTRL_ALT_SHIFT_Z             = ""
CTRL_ALT_SHIFT_X             = ""
CTRL_ALT_SHIFT_C             = ""
CTRL_ALT_SHIFT_V             = ""
CTRL_ALT_SHIFT_B             = ""
CTRL_ALT_SHIFT_N             = ""
CTRL_ALT_SHIFT_M             = ""
CTRL_ALT_SHIFT_COMMA         = ""
CTRL_ALT_SHIFT_PERIOD        = ""
CTRL_ALT_SHIFT_FORWARD_SLASH = ""

# --------------------------------- Special Keys -------------------------------

INSERT                       = ""
HOME                         = ""
PAGE_UP                      = ""
DELETE                       = ""
END                          = ""
PAGE_DOWN                    = ""
SPACE                        = "\x20"

SHIFT_INSERT                 = ""
SHIFT_HOME                   = ""
SHIFT_PAGE_UP                = ""
SHIFT_DELETE                 = ""
SHIFT_END                    = ""
SHIFT_PAGE_DOWN              = ""
SHIFT_SPACE                  = "\x20"

ALT_INSERT                   = ""
ALT_HOME                     = ""
ALT_PAGE_UP                  = ""
ALT_DELETE                   = ""
ALT_END                      = ""
ALT_PAGE_DOWN                = ""
ALT_SPACE                    = ""

ALT_SHIFT_INSERT             = ""
ALT_SHIFT_HOME               = ""
ALT_SHIFT_PAGE_UP            = ""
ALT_SHIFT_DELETE             = ""
ALT_SHIFT_END                = ""
ALT_SHIFT_PAGE_DOWN          = ""
ALT_SHIFT_SPACE              = ""

# CTRL_INSERT                  = "" # Undefined
CTRL_HOME                    = "\x1b\x5b\x31\x3b\x35\x48"
CTRL_PAGE_UP                 = "\x1b\x5b\x35\x3b\x35\x7e"
CTRL_DELETE                  = "\x1b\x5b\x33\x3b\x35\x7e"
CTRL_END                     = "\x1b\x5b\x31\x3b\x35\x46"
CTRL_PAGE_DOWN               = "\x1b\x5b\x36\x3b\x35\x7e"
CTRL_SPACE                   = "\x00" #NUL, Null

CTRL_SHIFT_INSERT            = ""
CTRL_SHIFT_HOME              = ""
CTRL_SHIFT_PAGE_UP           = ""
CTRL_SHIFT_DELETE            = ""
CTRL_SHIFT_END               = ""
CTRL_SHIFT_PAGE_DOWN         = ""
CTRL_SHIFT_SPACE             = ""

CTRL_ALT_INSERT              = ""
CTRL_ALT_HOME                = ""
CTRL_ALT_PAGE_UP             = ""
CTRL_ALT_DELETE              = ""
CTRL_ALT_END                 = ""
CTRL_ALT_PAGE_DOWN           = ""
CTRL_ALT_SPACE               = ""

CTRL_ALT_SHIFT_INSERT        = ""
CTRL_ALT_SHIFT_HOME          = ""
CTRL_ALT_SHIFT_PAGE_UP       = ""
CTRL_ALT_SHIFT_DELETE        = ""
CTRL_ALT_SHIFT_END           = ""
CTRL_ALT_SHIFT_PAGE_DOWN     = ""
CTRL_ALT_SHIFT_SPACE         = ""
