import os

a = []

for filename in os.listdir():
	if '.txt' in filename:
		with open(filename, 'r') as file:
			file = open(filename, 'r')
			char = file.read(1)
			while char:
				if ord(char) > 96 and ord(char) < 123:
					a.append(ord(char))
				elif ord(char) > 64 and ord(char) < 91:
					a.append(ord(char) + 32)
				char = file.read(1)
for letter in range(97, 123, 1):
	print(chr(letter), a.count(letter), end='\n')
