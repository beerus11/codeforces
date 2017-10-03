string=raw_input()
def isAllUpper(array):
	return all(map(lambda x: x>='A' and x<='Z',array))
def isOnlyFirstSmall(array):
	if array[0]>='a' and array[0]<='z' and isAllUpper(array[1:]):
		return True
	return False
	
if isOnlyFirstSmall(string) :
	print string[0].upper()+string[1:].lower()
elif isAllUpper(list(string)):
	print string.lower()
else:
	print string
	