import sys

if len(sys.argv) == 1:
	print('please, enter filepath')
	sys.exit()

filepath = sys.argv[1]

try:
	with open(filepath, 'r') as f:
		print(sum((1 for x in f)))

except(FileNotFoundError):
	print('file not found')