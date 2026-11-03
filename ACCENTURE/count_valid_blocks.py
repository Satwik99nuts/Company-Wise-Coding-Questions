# Count consecutive blocks whose length equals their element value.
# Example: [2, 2, 3, 3, 3, 4, 2, 2, 2] -> 2

def count_valid_blocks(n, arr):
    """Return the number of consecutive equal-value blocks with matching length."""
    if n != len(arr):
        raise ValueError("n must match the length of arr")

    valid_blocks = 0
    i = 0

    while i < n:
        value = arr[i]
        j = i

        # Move j to the first index after this consecutive block.
        while j < n and arr[j] == value:
            j += 1

        block_length = j - i
        if block_length == value:
            valid_blocks += 1

        # The next block starts where this one ends.
        i = j

    return valid_blocks


arr = [2, 2, 3, 3, 3, 4, 2, 2, 2]
print(count_valid_blocks(len(arr), arr))  # 2
