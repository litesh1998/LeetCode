class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=int(''.join(map(str,digits)))
        return list(str(n+1))