class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Manacher算法
        s0=list()
        #添加分隔符
        for i in s:
            s0+='#'
            s0+=i
        s0+='#'
        l=len(s0)
        num=list()
        #扩散
        for j in range(len(s0)):
            step=0
            while j-step!=-1 and j+step!=l and s0[j-step]==s0[j+step]:
                step+=1
            num.append(step-1)
        nuindex=num.index(max(num))
        maxstep=(max(num))
        
        return s[int((nuindex-maxstep)/2):int((nuindex+maxstep)/2)]