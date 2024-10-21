def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def find_palindromic_primes():
    """Find all 3-digit palindromic primes."""
    palindromic_primes = []
    for num in range(100, 1000):  # Loop through all 3-digit numbers
        if is_prime(num) and is_palindrome(num):
            palindromic_primes.append(num)
    return palindromic_primes

# Get all 3-digit palindromic primes
palindromic_primes = find_palindromic_primes()
print(palindromic_primes)
print(len(palindromic_primes))