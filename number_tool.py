def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
def explore_numbers():
    name = input("Enter your name: ")
    numbers = []
    for i in range(1, 4):
        number = int(input(f"Enter your {i} favorite number: "))
        numbers.append(number)
    print(f"\nHello, {name}! Let's explore your favorite numbers:")
    even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    for num, status in even_odd_info:
        print(f"The number {num} is {status}.")   
    print("\nHere are your numbers and their squares:")
    for num in numbers:
        square_info = (num, num**2)
        print(f"The number {num} and its square: {square_info}")
    sum_numbers = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {sum_numbers}")
    if is_prime(sum_numbers):
        print(f"Wow, {sum_numbers} is a prime number!")
    else:
        print(f"{sum_numbers} is not a prime number, but it's still special!")
explore_numbers()
