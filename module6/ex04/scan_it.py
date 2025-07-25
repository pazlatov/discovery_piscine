import sys
import re
if len(sys.argv) -1 != 2:
	print("none")
else:
	if re.findall(rf'\b{re.escape(sys.argv[1])}\b', sys.argv[2]):
		print(len(re.findall(rf'\b{re.escape(sys.argv[1])}\b', sys.argv[2])))
	else:
		print("none")