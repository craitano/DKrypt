__author__ = "Chris Raitano"
__copyright__ = "Copyright 2018, Chris Raitano"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Chris Raitano"

'''
    Caesar cipher decryption
'''

'''
* Decrypts using RSA
* Params:
*   c (int): the Ciphertext
*   d (int): private key exponent
*   e (int): public key exponent
*   p (int): prime 1
*   q (int): prime 2
*   dp (int): fast decryptio exponent 1
*   dq (int): fast decryption exponent 2
* Return (string): the decrypted message
'''
def decrypt(c, d, e, n, p, q, dp, dq):
    if(c and n and d):
        return decrypt_c_n_d(c, n, d)
    # TODO: you know what to do
    return

'''
* Perform a modular multiplicative inverse
* Params:
*   a (int): the number to perform the operation on
*   m (int): the modulus
* Return (int): a^-1 mod m 
'''
def mod_inverse(a, m):
    c = 1
    while (c % a > 0):
        c += m
    return c // a

'''
* Calculate dp given d and p
* Params:
*   d (int): private key exponent
*   p (int): prime 1
* Return (int): dp
'''
def get_dp(d, p):
    return d % (p - 1)

'''
* Calculate dq given d and q
* Params:
*   d (int): private key exponent
*   q (int): prime 2
* Return (int): dq
'''
def get_dq(d, q):
    return d % (q - 1)

'''
* Decrypt given c, n, and d
* Paras:
*   c (int): ciphertext
*   n (int): mod value
*   d (int): private key exponent
* Return (string): the decrypted plaintext
'''
def decrypt_c_n_d(c, n, d):
    return pow(c, d, n)

'''
* Attempt to decrypt given c, n, and d using Wiener's attack
* Paras:
*   c (int): ciphertext
*   n (int): mod value
*   e (int): public key exponent
* Return:
*   (string) the decrypted plaintext, if available
*   (int) -1, otherwise
'''
def decrypt_c_n_e(c, n, e):
    continuedFraction = ()
    # Get the continued fraction expansion
    divisor = n
    result = e / divisor
    remainder = e % divisor
    continuedFraction.append(result)
    while(remainder != 0):
        num = divisor
        divisor = remainder
        result = num / divisor
        remainder = num % divisor
        continuedFraction.append(result)
    # Attempt to find likely roots of n
    # TODO: finish this

'''
* Decrypt given c, p, q, qp, and dq
* Params:
*   c (int): ciphertext
*   p (int): prime 1
*   q (int): prime 2
*   dp (int): fast decription exponent 1
*   dq (int): fast decription exponent 2
* Return (string): the decrypted plaintext
'''
def decrypt_c_p_q_dp_dq(c, p, q, dp, dq):
    qinv = mod_inverse(q, p)
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    h = (qinv * (m1 - m2)) % p
    return m2 + h * q

