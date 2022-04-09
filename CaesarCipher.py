#Python3 program designed to create a caesar cipher
import string

message = input("Enter the message: ")
shift = int(input("Enter the shift for the Caesar Cipher: "))


def caesar(text, alphabet):
        
    def shift_alphabet(alphabet):
        return (alphabet[shift:] + alphabet[:shift])
    
    shifted_alphabet = tuple(map(shift_alphabet, alphabet))
    final_alphabet = ''.join(alphabet)
    final_shifted_alphabet = ''.join(shifted_alphabet)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)
    
print(caesar(message, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))