# You are given an integer array A of length N, where each element is between 2 and 10 (inclusive).

# A block is a consecutive group of identical elements.

# Count how many such blocks exist where:

# Length of the block = value of the element.

# Return the count of such blocks.

# Input
# input1: An integer N, representing the size of the array.
# input2: An integer array A.
# Output

# Return an integer representing the number of blocks whose length is equal to their element value.

# Example 1
# input1 = 9
# input2 = {2, 2, 3, 3, 3, 4, 2, 2, 2}

# Consecutive blocks:

# {2, 2}       → length = 2, value = 2  ✅
# {3, 3, 3}    → length = 3, value = 3  ✅
# {4}          → length = 1, value = 4  ❌
# {2, 2, 2}    → length = 3, value = 2  ❌

# Therefore:

# Output = 2
# Core concept

# Array traversal + consecutive groups / run-length counting






















