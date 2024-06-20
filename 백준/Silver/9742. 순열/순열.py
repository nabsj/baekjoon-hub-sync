from itertools import islice, permutations

def find_permutation(input_str, pos):
    elements = input_str.strip()
    pos = int(pos)
    
    # Generate the permutations and directly fetch the desired one
    perm_iter = permutations(elements)
    
    try:
        # Move the iterator to the desired position (pos-1 because islice is zero-based)
        desired_permutation = next(islice(perm_iter, pos-1, pos))
        return ''.join(desired_permutation)
    except StopIteration:
        return "No permutation"

# Read input
import sys
input = sys.stdin.read

data = input().strip().split('\n')
results = []

for line in data:
    if line.strip():
        parts = line.rsplit(' ', 1)
        if len(parts) == 2:
            input_str, pos = parts
            result = find_permutation(input_str, pos)
            results.append(f"{input_str} {pos} = {result}")

# Print all results
for result in results:
    print(result)
