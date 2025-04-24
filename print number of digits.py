def count_digits(number):
    digits = len(str(abs(number)))  # absolute value to handle negative numbers
    print(f"The number {number} has {digits} digits")

# Example usage:
count_digits(12345)
