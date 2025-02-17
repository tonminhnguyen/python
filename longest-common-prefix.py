from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]

def main():
    test_strs = ["flower", "flow", "flight"]
    result = longestCommonPrefix(test_strs)
    print(f"The longest common prefix is: '{result}'")

main()
