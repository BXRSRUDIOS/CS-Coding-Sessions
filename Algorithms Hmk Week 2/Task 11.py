'''
Task 11
Write an algorithm that will take in a string as input and a key, 
the key will act as a cipher and output a different character 
for example entering the letter A and a Key of 2 will make the new character a C. 
This is also known as a Caesar cipher 
'''

result = ""
string = "HELLO WORLD"
key = 2

for i in range(len(string)):
    char = string[i]
    if char.isupper():
        result += chr((ord(char) + key-65) % 26 + 65)
    elif char.islower():
        result += chr((ord(char) + key-97) % 26 + 97)
    else:
        result += char

print(result)

