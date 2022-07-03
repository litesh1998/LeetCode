class Solution(object):
    def increasingTriplet(self, nums):

        
        i = j = float('inf')
        
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        
        return False