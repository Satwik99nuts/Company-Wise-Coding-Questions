# ============================================================
# STRING PERMUTATIONS — FROM SCRATCH
# No imports. No libraries. Pure recursion.
# ============================================================
# LOGIC IDEA:
# To permute "ABC":
#   Fix 'A' at front → permute "BC" → gives AB C, ACB → ABC, ACB
#   Fix 'B' at front → permute "AC" → gives BAC, BCA
#   Fix 'C' at front → permute "AB" → gives CAB, CBA
#
# For each character, remove it from string, permute the rest,
# stick it back at the front.
# Stop when string has 1 character (only one arrangement).
# ============================================================


def get_permutations(s):
    # Base case: only one character → only one arrangement
    if len(s) == 1:
        return [s]

    result = []

    for i in range(len(s)):
        current_char = s[i]

        # Remove current character from string
        remaining = s[:i] + s[i + 1 :]

        # Recursively get all permutations of remaining string
        for perm in get_permutations(remaining):
            result.append(current_char + perm)

    return result


def get_unique_permutations(s):
    all_perms = get_permutations(s)

    # Remove duplicates manually (no set())
    seen = []
    for p in all_perms:
        if p not in seen:
            seen.append(p)

    # Sort manually using bubble sort
    for i in range(len(seen)):
        for j in range(i + 1, len(seen)):
            if seen[i] > seen[j]:
                seen[i], seen[j] = seen[j], seen[i]

    return seen


# ============================================================
# TAKE INPUT AND PRINT OUTPUT
# ============================================================

s = input("Enter a string: ").strip()

if len(s) == 0:
    print("Empty string entered.")
else:
    result = get_unique_permutations(s)

    print("Total permutations:", len(result))
    print("All permutations:")
    for p in result:
        print(" ", p)
