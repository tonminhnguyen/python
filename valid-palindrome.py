def get_input():
    while True:
        try:
            return input() 
        except ValueError:
            return False
        
def isAlphabetNumber(c):
    return ('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9')

def checkPalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if not isAlphabetNumber(s[l]):  
            l += 1
            continue 
        if not isAlphabetNumber(s[r]):
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
        
def main():
    num = get_input()
    print(checkPalindrome(num))

main()
