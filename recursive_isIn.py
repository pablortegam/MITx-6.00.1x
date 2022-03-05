def isIn(char, aStr):
    s=aStr
    if len(s)==0:
        return False
    if char==s[int(len(s)/2)]:
        return True
    if s[int(len(s)/2)]>char:
        aStr=s[0:int(len(s)/2)]
        return isIn(char,aStr)
    if s[int(len(s)/2)]<char:
        aStr=s[int(len(s)/2)+1:len(s)]
        return isIn(char,aStr)
isIn('e','abcde')
