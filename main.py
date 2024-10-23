# Sian Jose
def encode(password):
    password1 = ''
    for i in password:
        if i == "7":
            element = "0"
        elif i == "8":
            element = "1"
        elif i == "9":
            element = "2"
        else:
            element = int(i) + 3
        password1 += str(element)
    print("Your password has been encoded and stored!")
    return password1

def decode(decode_pass):
    password = ""
    for i in decode_pass:
        if i == "0":
            password += "7"
        elif i =="1":
            password += "8"
        elif i == "2":
            password += "9"
        else:
            password += str(int(i) -3)
    return password

if __name__ == '__main__':
    option = 0
    while option < 3:
        print("Menu\n----------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("\nPlease enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
        elif option == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}")
        elif option == 3:
            continue
