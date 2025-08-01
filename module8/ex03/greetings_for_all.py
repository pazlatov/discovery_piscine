def greetings(text=""):
	if text == "":
		print("Hello, noble stranger")
	elif type(text) == str:
		print(f"Hello, {text}")
	else:
		print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)