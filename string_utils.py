def split_before_each_uppercases(formula):
    start = 0
    split_formula = []

    for i in range(1, len(formula)):
        ch = formula[i]

        if ch.isupper():
            split_formula.append(formula[start:i])
            start = i   
            
    split_formula.append(formula[start:])

    return split_formula


    def split_at_first_digit(formula):
    digit_location = 1
    
    for ch in formula[1:]:
        if ch.isdigit():
            break
        digit_location += 1
    
    if digit_location == len(formula):
        return formula, 1
    
    prefix = formula[:digit_location]
    number_part = int(formula[digit_location:])
    return prefix, number_part
