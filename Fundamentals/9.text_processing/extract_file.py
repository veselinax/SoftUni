path = input().split('\\')   # escaping ('\')

for word in path:
    if "." in word:
        word = word.split(".")
        file_name = word[0]
        extension = word[1]
        print(f"File name: {file_name}")
        print(f"File extension: {extension}")


