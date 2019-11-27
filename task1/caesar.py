alph = list()
for i in range(26):
	alph.append(chr(ord('a') + i))
print("Input text:")
inp = input()
print("Input key:")
key = int(input())
res = ""
for i in inp:
	if (i == ' '):
		res += ' '
	else:
		res += alph[(alph.index(i) + key) % 26] 
print("Output text:")
print(res)	
