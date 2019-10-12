age = input('Hello hacker, what is your age? ')
print()
print('In five years your will be ' + str(int(age)++5))
print('When you live ten times as long you will be ' + str(int(age)*10))

if int(age) % 3 == 0:
	print('Your age divided by 3 equals ' + str(round(int(age)/3)))
if int(age) % 3 != 0:
	print('Your age diveded by 3 equals ' + str(round(int(age)/3)) + ' remainder ' + str(round(int(age)%3)))