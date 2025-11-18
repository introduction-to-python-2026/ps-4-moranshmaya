def split_at_first_digit(formula: str):
    """
    מחזיר זוג (prefix, number) לפי המספר הרציף הראשון.
    לדוגמה: 'C6H12' -> ('C', 6), 'H2O' -> ('H', 2), 'NaCl' -> ('NaCl', 1)
    """
    digit_location = None

    for i, ch in enumerate(formula):
        if ch.isdigit():
            digit_location = i
            break

    # אם אין בכלל ספרה – מחזירים את המחרוזת כמו שהיא והמספר 1
    if digit_location is None:
        return formula, 1

    # למצוא את סוף רצף הספרות
    j = digit_location
    while j < len(formula) and formula[j].isdigit():
        j += 1

    prefix = formula[:digit_location]
    number_str = formula[digit_location:j]

    # כאן number_str תמיד רק ספרות
    number_part = int(number_str)
    return prefix, number_part


from typing import List

def split_before_each_uppercases(formula: str) -> List[str]:
    """מפצל מחרוזת לפי אותיות גדולות, למשל 'NaClH2O' -> ['Na', 'Cl', 'H2O']"""
    if not formula:
        return []

    start = 0
    split_formula: List[str] = []

    for i in range(1, len(formula)):
        ch = formula[i]

        if ch.isupper():
            split_formula.append(formula[start:i])
            start = i

    split_formula.append(formula[start:])
    return split_formula
