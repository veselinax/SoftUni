while True:
    command = input()
    if command == "end":
        break
    reversed_word = "".join(command)[::-1]
    print(f"{command} = {reversed_word}")