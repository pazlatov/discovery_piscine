import sys
found = False
if len(sys.argv) - 1 != 1:
    print("none")
else:
	for arg in sys.argv[1]:
		if 'z' == arg:
			print("z", end="")
			found = True
	if not found:
		print("none")
