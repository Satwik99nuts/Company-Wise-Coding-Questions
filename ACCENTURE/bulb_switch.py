# Pressing switch i flips bulb i and every bulb after it.
# 0 means off and 1 means on. Return the fewest presses needed to turn all on.
# Example: [0, 1, 0, 1] -> 4


def minimum_switch_presses(bulbs):
    """Return the minimum number of suffix-switch presses needed."""
    presses = 0

    for bulb in bulbs:
        # An odd number of earlier presses flips this bulb's original state.
        current_state = bulb if presses % 2 == 0 else 1 - bulb

        # If this bulb is off, this switch must be pressed now.
        # That press also flips every future bulb.
        if current_state == 0:
            presses += 1

    return presses


print(minimum_switch_presses([0, 1, 0, 1]))  # 4
print(minimum_switch_presses([1, 0, 0, 0, 0]))  # 1
