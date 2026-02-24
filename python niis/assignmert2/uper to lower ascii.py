print("Enter a char")
ch=input()
ch=ord(ch)
if ch>=65 and ch<=90:
     ch=chr(ch+32)
     print(ch)
