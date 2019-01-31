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
def decrypt(cipher, alphabet, colorUnknown = False):
    dict = {}
    out = ""
    if(len(alphabet) > 26):
        print("\033[31mAlphabet cannot be longer than 26 characters. " + \
            "Characters map to the letters a-z.\033[0m\n")
        return -1
    # parse alphabet
    for i in range(0, len(alphabet)):
        sub = alphabet[i].lower()
        if(sub != ' '):
            dict[chr(i + ord('a'))] = sub
    # decrypt
    for c in cipher:
        isUpper = c.isupper()
        # substitute known letters
        if(c.lower() in dict):
            if(isUpper):
                out += dict[c.lower()].upper()
            else:
                out += dict[c]
        # color unsubstituted letters faint red
        elif(colorUnknown and ((c <= 'a' and c >= 'z') or
          (c <= 'A' and c >= 'Z'))):
            out += "\033[31m\033[2m" + c + "\033[0m"
        # print anything else as is
        else:
            out += c
    return out
