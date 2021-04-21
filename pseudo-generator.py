import random
import sys

given = 0

if len(sys.argv) == 2:
	given = sys.argv[1]
else:
    given = input("Please enter the length of your password: ")

characters = [ 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '§', '!', '$', '%', '&', '(', ')', '=', '?', '{', '[', ']', '}'
]

password = ""

for i in range(int(given)):
	password = password + characters[random.randint(0, len(characters) - 1)]

print("Your generated password: ", password)