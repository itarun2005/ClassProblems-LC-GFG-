class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxidx=0
        for i in range(0,len(nums)):
            if i>maxidx:
                return False
            maxidx=max(maxidx, i+nums[i])
        return True
        