def fiz_buzz(upper_limit):
    """
    A function that outputs a number, the string "fiz", "buzz", or "fizbuzz",
    depening on the following conditions:

    If the number the generator has currently counted up to is a multiple of
    3, then it returns the string "fiz".

    If the number is a multiple of 5, then it returns the string "buzz".

    If the number is a multiple of 3 and 5, the it returns the string "fizbuzz".

    If the number is not a multipl of 3 or 5, then it returns the number.

    Arguments:
        upper_limit (int): The max number the generator counts to.

    Returns:
        (str | int): One of an integer not divisible by 3 or 5, "fiz", "buzz",
        or "fizbuzz".
    """
    for i in range(1, upper_limit):
        is_divisible_by_3 = i % 3 == 0
        is_divisible_by_5 = i % 5 == 0

        if is_divisible_by_3 and is_divisible_by_5:
            yield "fizbuzz"
        elif is_divisible_by_3:
            yield "fiz"
        elif is_divisible_by_5:
            yield "buzz"
        else:
            yield i
