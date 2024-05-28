def is_positive_number(value):
    try:
        number_string = float(value)
    except ValueError as e:
        print(e.__class__.__name__)
        return False
    return number_string > 0
