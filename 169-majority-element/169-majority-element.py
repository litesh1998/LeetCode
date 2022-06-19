class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        ans=None
        
        for i in nums:
            if cnt==0:
                ans=i
            cnt+=(1 if i==ans else -1)
            
        return ans