import sys
if len(sys.argv) - 1 != 2:
	print("none")
else:
	first_num = int(sys.argv[1])
	second_num = int(sys.argv[2])
	if first_num >= second_num:
		print("none")
	else:
		print(list(range(first_num, second_num + 1)))	