def split_before_each_uppercase(formula: str) -> list[str]:
    if not formula:
        return []

    start = 0
    split_formula = []

    for i in range(1, len(formula)):
        if formula[i].isupper():
            split_formula.append(formula[start:i])
            start = i

    split_formula.append(formula[start:])
    return split_formula



    def split_at_first_digit(formula: str):
    digit_location = None

    for i, ch in enumerate(formula):
        if ch.isdigit():
            digit_location = i
            break

    if digit_location is None:
        return formula, 1

    prefix = formula[:digit_location]
    number_str = formula[digit_location:]

    if not number_str.isdigit():
        return formula, 1

    number_part = int(number_str)
    return prefix, number_part
