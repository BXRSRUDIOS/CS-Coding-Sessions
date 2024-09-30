from itertools import permutations

# Function to check if a sequence forms an arithmetic sequence
def is_arithmetic_sequence(seq):
    # Calculate the common difference
    diff = seq[1] - seq[0]
    # Check if the difference between consecutive terms is constant
    return all(seq[i+1] - seq[i] == diff for i in range(1, len(seq) - 1))

# Function to form a number from two digits
def form_number(d1, d2):
    return 10 * d1 + d2

# Digits 0 to 9
digits = list(range(10))

# All permutations of 10 digits
all_permutations = permutations(digits, 10)

# Collect valid sequences and their sums
valid_sequences = []

# Loop over each permutation of digits
for perm in all_permutations:
    # Form five two-digit numbers using the digits
    sequence = [form_number(perm[2*i], perm[2*i+1]) for i in range(5)]
    
    # Check if the sequence is in increasing order and forms an arithmetic sequence
    if sequence == sorted(sequence) and is_arithmetic_sequence(sequence):
        valid_sequences.append(sequence)

# Calculate the total sum of all valid sequences
total_sum = sum(sum(seq) for seq in valid_sequences)

# Output the result
print("Valid arithmetic sequences:", valid_sequences)
print("Total sum of all sequences:", total_sum)
