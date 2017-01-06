

inputfile = open('inputday6.txt')

filein = (inputfile.read())

# filein = '''eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar'''

f = filein.split()
# print(f)
answer = ''
for i in range (0,8):
	d = {}
	for word in f:
		# print(word)
		letter = word[i]
		if letter in d:
			d[letter] = d[letter] + 1
		else:
			d[letter] = 1
	# print(max(d.values()))
	# print("text2")
	
	#Use this for part 1!!!
	# letter = max(d, key=d.get)
	#this one is for part 2!!!
	letter = min(d, key=d.get)

	answer += letter
	# max_letter = d(max(d.values()))
	# print(max_letter)

	#  in f:
	
	# for i in range(len(word)):
	# 	dictname = "d" + str(i)
	# 	if 
	# print("next")

print(answer)