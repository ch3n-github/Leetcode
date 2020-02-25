class Solution:
#堆栈
    def isMatch(self, s: str, p: str):
        if not p:return not s
        firstmatch = bool(s) and p[0] in ['.',s[0]]
        if len(p)>=2 and p[1]=='*':
            return(firstmatch and self.isMatch(s[1:],p)) or self.isMatch(s,p[2:])
        else:
            return firstmatch and self.isMatch(s[1:],p[1:])