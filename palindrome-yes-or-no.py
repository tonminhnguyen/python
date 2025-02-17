def main():
    cases = int(input())

    for i in range(1, cases + 1):
        str = input()
        rev = str[::-1]
        result = "Yes" if str == rev else "No"
        print(f"Case {i}: {result}")

main()