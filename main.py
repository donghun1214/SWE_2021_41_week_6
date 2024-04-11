from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    index = {}  
    for i, num in enumerate(nums):
        complement = target - num  
        if complement in index:  
            return [index[complement], i]  
        index[num] = i  
