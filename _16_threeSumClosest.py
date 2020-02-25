#Author：chen
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums)<=2:return None
        nums.sort()
        dis=float('inf')
        allsum=0
        for i in range(len(nums)-2):
            strat=i+1
            end=len(nums)-1
            while(strat<end):

                if abs(nums[i]+nums[strat]+nums[end]-target)<dis:
                    dis=abs(nums[i]+nums[strat]+nums[end]-target)
                    allsum=nums[i]+nums[strat]+nums[end]
                if nums[i]+nums[strat]+nums[end]-target>0:
                    end-=1
                elif nums[i]+nums[strat]+nums[end]-target<0:
                    strat+=1
                else:
                    return target
        return allsum