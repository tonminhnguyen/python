from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) < len(nums)

def main():
    test_nums = [1, 2, 3, 4, 5, 1]
    result = hasDuplicate(test_nums)
    print(f"{result}")

main()

# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false
