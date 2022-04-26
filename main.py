from de_en_code import Morse

morse = Morse()

should_continue = True

while should_continue:
    action = input("Do you want to encode text or decode Morse Code? Write encode or decode. \n")

    if action == "encode":
        user_input = input("Enter your text. \n")
        print(f"Your encoded Morse Code: \n{morse.encode(user_input)}")
    else:
        user_input = input("Enter your morse. \n")
        print(f"Your decoded Text: \n{morse.decode(user_input)}")
    should_continue = input("\nDo you want to continue? Write True or False \n").title()
