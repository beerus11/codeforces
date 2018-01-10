string=raw_input()
lno= len(filter(lambda x: x.islower(),list(string)))
uno= len(filter(lambda x: x.isupper(),list(string)))
if lno<uno:
	print string.upper()
else:
	print string.lower()
