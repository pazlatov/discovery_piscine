import sys
if len(sys.argv) - 1 < 1:
	print("none")
else:
	for i in sys.argv[1:]:
		if i.endswith("ism"):
			print(i)
		else:
			print(f"{i}ism")