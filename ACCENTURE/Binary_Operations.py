# The string alternates between binary digits and operators.
# A = AND, B = OR, C = XOR. Evaluate strictly from left to right.
# Example: "1C0C1C1A0B1" -> 1


def evaluate_binary_expression(expression):
    """Evaluate a valid alternating binary expression; return -1 for None."""
    if expression is None:
        return -1

    result = int(expression[0])  # The first digit is our running answer.

    # Read an operator and the digit after it: positions 1/2, 3/4, and so on.
    for index in range(1, len(expression), 2):
        operator = expression[index]
        next_digit = int(expression[index + 1])

        if operator == "A":
            result = result & next_digit  # AND: 1 only when both values are 1.
        elif operator == "B":
            result = result | next_digit  # OR: 1 when either value is 1.
        elif operator == "C":
            result = result ^ next_digit  # XOR: 1 when the values differ.

    return result


print(evaluate_binary_expression("1C0C1C1A0B1"))  # 1
