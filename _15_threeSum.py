#Author：chen
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        if not nums or len(nums)<3:return []
        pat=[]
        nums.sort()
        start=0
        while nums[start]<=0 and start<len(nums)-1:
            end=len(nums)-1
            while nums[end]>=0 and start<end:
                if -(nums[start]+nums[end])in nums[start+1:end]:
                    midgro=[-(nums[start]+nums[end]),nums[start],nums[end]]
                    midgro.sort()
                    if midgro not in pat:
                        pat.append(midgro)
                end-=1
            start+=1
        return pat