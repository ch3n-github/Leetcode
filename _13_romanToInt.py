class Solution:
    def romanToInt(self, s: str) -> int:    
        num=0
        def tonum(s,num):
            if not s:
                return num
            dic = {'M':1000,'D':500,'C':100,'L':50,\
            'X':10,'V':5,'I':1,'CM':900,'CD':400,'XC':90,'XL':40,'IV':4,'IX':9}
            if s[0:2]in dic:
                num+=dic[s[0:2]]
                return tonum(s[2:],num)
            else:
                num+=dic[s[0]]
                return tonum(s[1:],num)
        return tonum(s,num)