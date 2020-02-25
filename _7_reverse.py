class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        if s[0]=='-':
            if int(s[1:][::-1])>=2**31:return 0
            else:return -int(s[1:][::-1])
        else:
            if int(s[::-1])>=2**31-1:return 0
            else:return int(s[::-1])