def get_input():
    while True:
        try:
            return int(input())
        except ValueError:
            return False

def checkPalindrome(x: int) -> bool:
    if x < 0:
        return False
    rev = 0
    num = x
    while num:
        rev = (rev * 10) + (num % 10)
        num //= 10
    return rev == x

def main():
    num = get_input()
    print(checkPalindrome(num))
    # if count <= 0:
    #     return
    
    # for _ in range(count):
    #     num = get_input()
    #     print(checkPalindrome(num))

main()
