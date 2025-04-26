def password(st):
    if len(st) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    for char in st:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        if has_upper and has_lower and has_digit:
            return True
    return has_upper and has_lower and has_digit