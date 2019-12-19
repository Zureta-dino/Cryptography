from random import shuffle
import json
import argparse

def keygen():
	key = [i for i in range(256)]
	shuffle(key)
	return key

def write_to_file(list_of, filename):
	with open(filename, 'w') as file:
		file.write(json.dumps(list_of))

def encoding(key_list, filename, filename_enc = 'encoded.txt'):
	seq =''
	with open(filename, 'r') as file:
		letter = file.read(1)
		while letter:
			seq += chr(key_list[ord(letter)])
			letter = file.read(1)
	with open(filename_enc, 'w') as file_enc:
		file_enc.write(seq)		

def decoding(key_list, filename_enc = 'encoded.txt', filename_dec = 'decoded.txt'):
	seq = ''
	with open(filename_enc, 'r') as file_enc:
		letter = file_enc.read(1)
		while letter:
			seq += chr(key_list.index(ord(letter)))
			letter = file_enc.read(1)
	with open(filename_dec, 'w') as file_dec:
		file_dec.write(seq)	

def frequency(filename):
	dict = {i : 0 for i in range(256)}
	with open(filename, 'r') as f:
		text = f.read()
		for i in range(256):
			letter = chr(i)
			dict[i] = text.count(letter)/ len(text)
	return dict

def sort(dict):
	dict_sort = list(dict.items())
	dict_sort.sort(key = lambda i : i[1], reverse = True)
	return dict_sort

def get_dict(filename):
	with open(filename, 'r') as f:
		dict = json.loads(str(f.read()))
	return dict

def possible_key(dict1, dict2):
	list1 = []
	list2 = []
	for i in range(256):
		list1.append(dict1[i][0])
		list2.append(dict2[i][0])
	possible_key = {list1[i] : list2[i] for i in range(len(list1))}
	return possible_key

def dict_to_list(dict):
	list_keys = list(dict.items())
	list_keys.sort()
	keys = []
	for i in range(256):
		keys.append(int(list_keys[i][1]))
	return keys
		
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('mode', help = 'keygen/encode/decode/break')
	parser.add_argument('-k', '-key', help = 'makes possible decryption key')
	parser.add_argument('-c', '-count', help = 'makes frequency analysis of the text')
	args = parser.parse_args()
	if args.mode == 'keygen':
		list_of_keys = keygen()
		write_to_file(list_of_keys, 'list_of_keys.json')
		print("List of keys was added in list_of_keys.json")
	if args.mode == 'encode':
		list_of_keys = keygen()
		write_to_file(list_of_keys, 'list_of_keys.json')
		encoding(list_of_keys, 'initial.txt')
		print("Encoded text was added in encoded.txt")
	if args.mode == 'decode':
		list_of_keys = keygen()
		write_to_file(list_of_keys, 'list_of_keys.json')
		encoding(list_of_keys, 'initial.txt')
		decoding(list_of_keys)
		print("Decoded text was added in decoded.txt")
	if args.mode == 'break':	
		if args.k:			
			count_file = get_dict(args.k)
			count_orig = frequency('initial.txt')
			sort_count_file = sort(count_file)
			sort_count_orig = sort(count_orig)
			key_poss = possible_key(sort_count_orig, sort_count_file)
			list_keys = dict_to_list(key_poss)
			write_to_file(list_keys, 'possible_key.json')
			decoding(list_keys, filename_dec = 'decoded_possible.txt')
			print("Possible key was added in possible_key.json")			
		if args.c:
			count = frequency(args.c)
			write_to_file(count, 'frequency.json')
			print("Frequencies was added in frequency.json")

if __name__ == "__main__":
	main()
