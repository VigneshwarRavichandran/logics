'''
2 - a b c
3 - d e f
4 - g h i
5 - j k l
6 - m n o
7 - p q r s
8 - t u v
9 - w x y z
'''

phone = {
	2 : {
		1 : 'a',
		2 : 'b',
		3 : 'c'
	},
	3 : {
		1 : 'd',
		2 : 'e',
		3 : 'f'
	},
	4 : {
		1 : 'g',
		2 : 'h',
		3 : 'i'
	},
	5 : {
		1 : 'j',
		2 : 'k',
		3 : 'l'
	},
	6 : {
		1 : 'm',
		2 : 'n',
		3 : 'o'
	},
	7 : {
		1 : 'p',
		2 : 'q',
		3 : 'r',
		4 : 's'
	},
	8 : {
		1 : 't',
		2 : 'u',
		3 : 'v'
	},
	9 : {
		1 : 'w',
		2 : 'x',
		3 : 'y',
		4 : 'z'
	}
}

encrypted_str = "2233344555"
prev = encrypted_str[0]
flag = True
temp_value = prev
temp_count = 1
result = ''
for index in range(1, len(encrypted_str)):
	element = encrypted_str[index]
	if prev != element:
		flag = False
		result += phone[int(temp_value)][int(temp_count)]
		prev = element
		temp_value = prev
		temp_count = 1
	else:
		flag = True
		temp_count += 1
if flag:
	result += phone[int(temp_value)][int(temp_count)]
print(result)
