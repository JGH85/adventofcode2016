import hashlib


# m.update(b"abc3231929")
# print(m.hexdigest())

found = 0
i = 0
password = '________'
used = []
print(len(password))
while found <8:
	tohash = "ugkcyxxp" + str(i)
	x = bytes(tohash)
	m = hashlib.md5()
	m.update(x)
	result = m.hexdigest()
	
	if result[0:5] == '00000':
		print(result)
		position = result[5]
		print(position)
		if position.isdigit():
			print("converting")
			position = int(position)
			if position <= (len(password)-1) and position not in used:
				print("valid")
				position = int(position)
				password = password[:position] + result[6] + password[position+1:]
				found += 1
				used.append(position)
			else:
				print("invalid")
		else:
			print("not a num")
		print(password)
	i += 1
	if i % 1000000 == 0:
		print(i)
	# found = 9

