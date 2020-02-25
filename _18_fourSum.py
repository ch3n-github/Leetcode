class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums)<4:return []
        res=[]
        nums.sort()
        for i in range(len(nums)-3):
            if nums [i]>(target/4):return res
            for j in range(i+1,len(nums)-2):
                start=j+1
                end=len(nums)-1
                while start < end :
                    if nums[end]<(target/4):break
                    if nums[i]+nums[j]+nums[start]+nums[end]>target :
                        end-=1
                    elif nums[i]+nums[j]+nums[start]+nums[end]<target:
                        start+=1
                    else:
                        res0=[nums[i],nums[j],nums[start],nums[end]]
                        if res0 not in res:
                            res.append(res0)
                        start+=1
                        end-=1

        return res