from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d=defaultdict(lambda: [])
        for idx, val in enumerate(nums):
            d[val].append(idx)
            tm = target -val
            
            if tm in d  :
                for t_idx in d[tm]:
                    if t_idx!= idx:
                        return [idx,  t_idx]

        return []