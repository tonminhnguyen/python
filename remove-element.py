# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]

def removeElement(nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

def main():
    test_nums = [3, 2, 2, 3] 
    test_val = 3
    result = removeElement(test_nums, test_val)
    print(f"Output: {result}, nums = {test_nums[:result] + ['_'] * (len(test_nums) - result)}")

main()
