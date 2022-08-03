from email import message


alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_latter = dict(zip(range(len(alphabet)), alphabet))

def encrypt(message, shift=3):
    cipher =''
    for letter in message:
        index = (letter_to_index[letter] + shift) % len(alphabet)
        shifted_letter = index_to_latter[index]
        cipher += shifted_letter
    return cipher
def decrypt(ciphered_text, shift=3):
    pass
def main():
    message = 'attack at noon'
    encrypted_message = encrypt(message, shift=3)
    print(encrypted_message)
main()