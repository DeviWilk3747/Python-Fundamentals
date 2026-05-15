# Takes all the text from a file and reads it
file = open("message.txt", "r")
content = file.read()
print(content)
file.close()