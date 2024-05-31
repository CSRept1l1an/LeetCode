from typing import List
from collections import Counter


def singleNumber(nums: List[int]) -> List[int]:
    count = Counter(nums)
    return [num for num in count if count[num] == 1]


class Solution:
    nums = [1, 2, 1, 3, 2, 5]
    print(singleNumber(nums))
