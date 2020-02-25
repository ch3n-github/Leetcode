class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        if not candidates:return res
        def example(suml,count=[]):
            for i in range(len(candidates)):
                if suml+candidates[i]<target:
                    count.append(candidates[i])
                    example(suml+candidates[i],count)
                    count.remove(candidates[i])
                elif suml+candidates[i]==target:
                    count.append(candidates[i])
                    count.sort()
                    if count not in res:
                        res.append(count[:])
                    count.remove(candidates[i])
                else:
                    break
                
        example(0)
        return res