import sys
import re
parameter = input("What was the parameter? ")
if len(sys.argv) -1 != 1:
	print("none")
else:
	if parameter == sys.argv[1]:
		print("Good job!")
	else:
		print("Nope, sorry...")