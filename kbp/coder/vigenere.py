#vigenere cipher
#Blaide de Vigenere, 1586
#substitution cipher
#
#Kabopan - Readable Algorithms. Public Domain, 2009



from _subst import *

def vigenere(plaintext, key):
    ciphertext = str()
    for (char, current_key) in zip(plaintext, key):
        current_shift = ALPHABET.index(current_key)
        shifted_char = substitute(char, ALPHABET, lambda x: x + current_shift)
        shifted_char = substitute(shifted_char, ALPHABET_LOWERCASE, lambda x: x + current_shift)
        ciphertext += shifted_char
    return ciphertext


if __name__ == "__main__":
    import test.vigenere_test