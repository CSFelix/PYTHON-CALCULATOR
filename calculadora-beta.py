# @CSFelix

import math

avg = lambda x: sum(x) / len(x)
command = ''

# Title
print()
print(('*' * 5) + ('*' * len(' Felix Calculator ')) + ('*' * 5))
print('***** Felix Calculator *****')
print(('*' * 5) + ('*' * len(' Felix Calculator ')) + ('*' * 5))
print()

# Menu
print("Tip 'W' to wiki, 'Q' to exit or your calc to get the result!")

# Proccess
while True:
	print()
	command = input('Command:')

	# Wiki Commands
	if command == 'W' or command == 'w':
		print()
		print("0) Tip 'W' to wiki or 'Q' to exit")
		print()
		print("1) Help Function >> help(sum) >> explains how to use the 'sum' function")
		print()
		print("2) Dir Function >> dir(math) >> display the sources and functions availables in 'math' package")
		print()
		print("3) 2 + 2 >> show the calc's result")
		print()

	# Exit Commands
	elif command == 'Q' or command == 'q': break

	# Calc Commands
	else:
		try: exec('print(' + command + ')')
		except:
			import traceback
			traceback.print_exc()	
		finally: command = None

print()
input('Tip any key to exit!')