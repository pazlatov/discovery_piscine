import sys
def shrink(text):
	print(text[:8])
def enlarge(text):
	print(text.ljust(8, 'z'))

if len(sys.argv[1]) >= 8:
	shrink(sys.argv[1])
elif len(sys.argv[1]) <= 8:
	enlarge(sys.argv[1])
else:
	print(sys.argv[1])