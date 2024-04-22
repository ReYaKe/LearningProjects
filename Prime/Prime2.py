# Initialize an empty list to store prime numbers
prime = []

# Initialize a counter for the total number of prime numbers found
l = 0

# Iterate through numbers from 2 to 1000
for i in range(2, 1001):
    # Initialize a variable to track whether i is divisible by any other number
    k = 0
    
    # Check divisibility of i by numbers from 2 to i-1
    for j in range(2, i):
        if i != j and i % j == 0:
            # If i is divisible by j, increment k
            k += 1
            break
        else:
            # Otherwise, keep k unchanged
            k += 0
    
    # If k remains 0, i is a prime number; add it to the prime list
    if k == 0:
        prime.append(i)
        l += 1
    else:
        # Otherwise, continue to the next number
        continue

# Print the list of prime numbers
print("Prime numbers between 2 and 1000:")
print(prime)

# Print the total count of prime numbers found
print(f"Total prime numbers found: {l}")
