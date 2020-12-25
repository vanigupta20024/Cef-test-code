'''
Code sample for CoronaSafe Fellowship
Python application implementing a todo app
Submitted by: Vani Gupta
Time taken: 6-7 hours (approx.)
'''

import sys
import os.path
from datetime import datetime

# globally declaring file path
todoPath = "C:/Users/Vani/Desktop/python/list/todo.txt"
donePath = "C:/Users/Vani/Desktop/python/list/done.txt"

# creates a file is file not already present om first time execution
try:
	todoPoint = open(todoPath, "r")
	donePoint = open(donePath, "r")
finally:
	todoPoint.close()
	donePoint.close()

def fileLength(fname):
	''' Input: file name
	Output: Number of lines present in the file
	'''
	num_lines = 0
	with open(fname, 'r') as f:
		for line in f: num_lines += 1
	return num_lines

# length of input from command line
input_length = len(sys.argv)
if input_length == 1 or (input_length == 2 and sys.argv[1] == 'help'):
	sys.stdout.buffer.write("Usage :-\n".encode('utf8'))
	sys.stdout.buffer.write("$ ./todo add \"todo item\"  # Add a new todo\n".encode('utf8'))
	sys.stdout.buffer.write("$ ./todo ls               # Show remaining todos\n".encode('utf8'))
	sys.stdout.buffer.write("$ ./todo del NUMBER       # Delete a todo\n".encode('utf8'))
	sys.stdout.buffer.write("$ ./todo done NUMBER      # Complete a todo\n".encode('utf8'))
	sys.stdout.buffer.write("$ ./todo help             # Show usage\n".encode('utf8'))
	sys.stdout.buffer.write("$ ./todo report           # Statistics".encode('utf8'))

elif sys.argv[1] == 'report':
	date = datetime.today().strftime('%Y-%m-%d')
	# using fileLength function to count pending and completed tasks
	pending = fileLength(todoPath)
	completed = fileLength(donePath)
	string = date + " Pending : " + str(pending) + " Completed : " + str(completed)
	sys.stdout.buffer.write(string.encode('utf8'))

elif sys.argv[1] == 'add':
	if sys.argv[-1] == 'add':
		# if no argument is specified after add
		sys.stdout.buffer.write("Error: Missing todo string. Nothing added!".encode('utf8'))
	else:
		line = sys.argv[2]
		flag = 0
		with open(todoPath, "r") as file:
			lines = file.readlines()
			for ln in lines:
				# checking redundancy of input todo task
				if ln.strip() == line: 
					flag = 1
					sys.stdout.buffer.write('Added todo: "{}"'.format(line).encode('utf8'))
		if flag == 0:
			with open(todoPath, 'r+') as file:
				content = file.read()
				file.seek(0, 0)
				file.write(line.rstrip('\r\n') + '\n' + content)
				sys.stdout.buffer.write('Added todo: "{}"'.format(line).encode('utf8'))

elif sys.argv[1] == 'ls':
	length = fileLength(todoPath)
	if length == 0:
		# when todo file is empty
		sys.stdout.buffer.write("There are no pending todos!".encode('utf8'))
	else:
		with open(todoPath, 'r') as file:
			line = file.readline()
			while line:
				string = "[" + str(length) + "] " + line
				sys.stdout.buffer.write(string.encode('utf8'))
				length -= 1
				line = file.readline()

elif sys.argv[1] == 'del':
	if sys.argv[-1] == 'del':
		# when delete number is not specified
		sys.stdout.buffer.write("Error: Missing NUMBER for deleting todo.".encode('utf8'))
	else:	
		remove = int(sys.argv[2])
		length = fileLength(todoPath)
		if length < remove or remove < 1:
			# Entering a negative number or 0 or number greater than already present 
			sys.stdout.buffer.write("Error: todo #{} does not exist. Nothing deleted.".format(remove).encode('utf8'))
		else:
			with open(todoPath, "r") as file:
				lines = file.readlines()
			with open(todoPath, "w") as file:
				for line in lines:
					if length != remove:
						file.write(line)
					length -= 1
			sys.stdout.buffer.write("Deleted todo #{}.".format(remove).encode('utf8'))

elif sys.argv[1] == 'done':
	if sys.argv[-1] == 'done':
		# when done number is not specified
		sys.stdout.buffer.write("Error: Missing NUMBER for marking todo as done.".encode('utf8'))
	else:
		doneNumber = int(sys.argv[2])
		length = fileLength(todoPath)
		if doneNumber > length or doneNumber < 1:
			sys.stdout.buffer.write("Error: todo #{} does not exist.".format(doneNumber).encode('utf8'))
		else:
			with open(todoPath, "r") as file:
				lines = file.readlines()
			with open(todoPath, "w") as file:
				for line in lines:
					if length != doneNumber:
						file.write(line)
					else:
						with open(donePath, "a") as filePointer:
							filePointer.write(line)
					length -= 1
			sys.stdout.buffer.write("Marked todo #{} as done.".format(doneNumber).encode('utf8'))
			# checking for redundancy
			uniqlines = set(open(donePath).readlines())
			open(donePath, "w").close()
			donefile = open(donePath, 'w').writelines(set(uniqlines))

# -----------------------------------------------------------End-of-program------------------------------------------------------ #