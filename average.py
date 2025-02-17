def get_input():
    while True:
        try:
            return int(input())
        except ValueError:
            return
def main():
    numbers = []
    
    print("Enter the number of integers:")
    count = get_input()

    if count <= 0:
        return
    
    print(f"Enter {count} integers:")
    for n in range(count):  
        num = get_input()
        numbers.append(num)
    
    average = sum(numbers) / len(numbers)
    print(f"Average: {average}")

main()
