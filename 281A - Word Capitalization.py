string=raw_input()
print string if ord(string[0])<97 else  chr(ord(string[0])-32)+string[1:]