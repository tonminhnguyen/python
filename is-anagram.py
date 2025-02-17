def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

def main():
    test_s = "listen" 
    test_t = "silent"
    result = isAnagram(test_s, test_t)
    print(f"Are '{test_s}' and '{test_t}' anagrams? {result}")

main()
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

# Example 2:
# Input: s = "jar", t = "jam"
# Output: false