class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=nums[0]
        for i in nums[1:]:
            res=res^i
            # print(res)
            
        return res
        