class Solution:
#字符串转整数
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        s=str
        l=len(s)
        dic=['0','1','2','3','4','5','6','7','8','9']
        if l ==1 :
            if s in dic:
                return int(s)
            else:return 0
        start=0
        end=0
        
        for i in range(l):
            if s[i] in dic:
                start=i
                end=i
                for j in range(l-i-1):
                    if s[i+1+j] in dic:
                        end+=1
                    else:
                        break
                if int(s[start:end+1])>2147483647:
                    return 2147483647
                else:
                    return int(s[start:end+1])
            elif s[i] in ['+','-']:
                if s[i+1] in dic:
                    start=i
                    end=i+1
                    for j in range(l-i-2):
                        if s[i+2+j] in dic:
                            end+=1
                        else:
                            break
                    if int(s[start:end+1])<-2147483648:
                        return -2147483648
                    elif int(s[start:end+1])>2147483647:
                        return 2147483647
                    else:
                        return int(s[start:end+1])
                else:
                    return 0
            elif s[i]==' ':
                continue
            else:
                return 0
        return 0