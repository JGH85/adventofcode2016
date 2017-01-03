import hashlib


# m.update(b"abc3231929")
# print(m.hexdigest())

found = 0
i = 0
password = ''
while found <8:
	tohash = "ugkcyxxp" + str(i)
	x = bytes(tohash)
	m = hashlib.md5()
	m.update(x)
	result = m.hexdigest()
	# print(result)
	if result[0:5] == '00000':
		password += result[5]
		print(password)
		found += 1
	i += 1
	# found = 9

