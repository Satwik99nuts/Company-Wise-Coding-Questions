# ============================================================
# EXTRACT NUMBERS FROM A STRING — FROM SCRATCH
# No imports. No libraries. Pure logic only.
# ============================================================
# LOGIC IDEA:
# Go through every character one by one.
# If it's a digit (0-9), keep collecting it.
# When a non-digit appears, save what we collected.
# That saved chunk is one number.
# ============================================================


def extract_numbers(s):
    numbers = []
    current = ""

    for ch in s:
        if ch >= "0" and ch <= "9":  # check if character is a digit
            current += ch  # keep building the number
        else:
            if current != "":  # non-digit found, save number
                numbers.append(int(current))
                current = ""  # reset for next number

    if current != "":  # catch last number if string ends with digit
        numbers.append(int(current))

    return numbers


# ============================================================
# TAKE INPUT AND PRINT OUTPUT
# ============================================================

s = input("Enter a string: ").strip()

result = extract_numbers(s)

print("Numbers found:", result)
print("Count        :", len(result))
print("Sum          :", sum(result))