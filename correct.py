def is_narc(n):
    """Check if a number is a narc."""
    num_str = str(n)
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == n

def print_narcis_numbers(start, end):
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1):
        if is_narc(n=num):
            print(num)

print_narcis_numbers(1000, 5000)
