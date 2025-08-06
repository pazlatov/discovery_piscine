def array_of_names(array):
	return[f"{first.capitalize()} {last.capitalize()}" for first, last in array.items()]

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))