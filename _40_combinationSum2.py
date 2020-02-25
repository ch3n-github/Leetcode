class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        if not candidates:return res
        def example(suml,candidates,count=[]):
            for  i in range(len(candidates)):
                if suml+candidates[i]<target:
                    count.append(candidates[i])
                    example(suml+candidates[i],candidates[i+1:],count)
                    count.remove(candidates[i])
                elif suml+candidates[i]==target:
                    count.append(candidates[i])
                    count.sort()
                    if count not in res:
                        res.append(count[:])
                    count.remove(candidates[i])
                else:
                    i=len(candidates)
                i+=1
        example(0,candidates)
        return res