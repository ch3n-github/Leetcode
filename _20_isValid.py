class Solution:
    def isValid(self, s: str) -> bool:
        valdic=['{}','()','[]']
        s0=''
        for i in s:
            s0+=i
            if s0[-2:]in valdic:
                s0=s0[:-2]
        if s0=='':return True
        else:return False