
'''
To do list
1. Define a function with two paramietrs like:contact_number,shift
2. Perform a simple arithmetic operation on each code point to obscure the original value.
3. Convert the modified code points back to characters: Use chr() for this.
4 Combine the characters to form the encoded contact number.
'''


def encode_contact_number(contact_number,shift=3):
    encoded_number=""
    for digits in contact_number:
        encoded_each_digit=str((int(digits) +shift) %10)
        encoded_number +=encoded_each_digit

    return encoded_number

contact_number = "01191187061"
encoded_number = encode_contact_number(contact_number,shift=4)
print("Encoded number:", encoded_number)

### decoding the number
def decode_contact_number(encoded_contact_number, shift=3):
    decoded_number = ""
    for digit in encoded_contact_number:
        decoded_digit = str((int(digit) - shift) % 10)
        decoded_number += decoded_digit
    return decoded_number

# Example usage
encoded_number = "45535521405"
decoded_number = decode_contact_number(encoded_number, shift=4)
print("Decoded number:", decoded_number)
