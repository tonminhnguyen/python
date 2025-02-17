from typing import List

def twoSum(nums: List[int], target: int):
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

def main():
    test_nums = [2, 7, 11, 15]
    test_target = 9
    result = twoSum(test_nums, test_target)
    print(f"Indices of numbers that add up to {test_target}: {result}")

main()
