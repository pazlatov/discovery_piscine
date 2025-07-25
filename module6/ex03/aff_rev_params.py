import sys
if len(sys.argv) -1 <= 2:
	print("none")
else:
	for param in sys.argv[1:][::-1]:
		print(param)