def get_input():
    while True:
        try:
            return input() 
        except ValueError:
            return False
def is_palindrome(str, l, r):
    while l < r:
        if str[l] != str[r]:
            return False
        l += 1
        r -= 1
    return True

def checkPalindrome(str):
    l = 0
    r = len(str) - 1
    l, r = 0, len(str) - 1
    while l < r:
        if str[l] != str[r]:
            return (is_palindrome(str, l + 1, r) or 
                        is_palindrome(str, l, r - 1))
        l += 1
        r -= 1
    return True
        
def main():
    num = get_input()
    print(checkPalindrome(num))

main()
