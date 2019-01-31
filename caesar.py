__author__ = "Chris Raitano"
__copyright__ = "Copyright 2018, Chris Raitano"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Chris Raitano"

'''
    Caesar cipher decryption
'''


'''
  Decrypts using a caesar cipher
    cipher (string): the Ciphertext
    shift (int): the shift used for encryption
  Return (string): the decrypted message
'''
def decrypt(cipher, shift):
    out = ""
    for i in range(0, len(cipher)):
        val = ord(cipher[i])
        # Lowercae
        if(val > 96 and val < 123):
            val = val -  97 - shift
            val %= 26
            val += 97
        # Uppercase
        if(val > 64 and val < 91):
            val = val - 64 - shift
            val %= 26
            val += 65
        out += chr(val)
    return out
