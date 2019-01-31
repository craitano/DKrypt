__author__ = "Chris Raitano"
__copyright__ = "Copyright 2018, Chris Raitano"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Chris Raitano"

'''
    One time pad decryption
'''

import sys

'''
  Decrypts using a one-time-pad
    cipher (string): the ciphertext
    key (string): the pad for decryption
  Requires: len(cipher) == len(key)
  Return (string): a string with the decrypted mesage
    or (int) -1 if there is an error
'''
def decrypt(cipher, pad):
    out = ""
    if(len(cipher) != len(pad)):
        print("\ncipher and pad must be the same length\n", file=sys.stderr)
        return -1
    for i in range(0, len(cipher)):
        valc = cipher[i]
        valp = pad[i]
        # Make sure both cipher and pad are letters
        if(valc.isalpha() and valp.isalpha()):
            uppercase = False
            if(valc.isupper()):
                uppercase = True
            valc = valc.lower()
            valp = valp.lower()
            valc = ord(valc)
            valp = ord(valp)
            valc =  valc + 26 - valp
            valc %= 26
            valc +=  97
            valc = chr(valc)
            # restore case
            if(uppercase):
                valc = valc.upper()
        out += valc
    return out
