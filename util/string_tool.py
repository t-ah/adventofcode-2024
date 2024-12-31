def combinations(state, left, right):
    """
    Generate all possible mixtures of the two strings (characters of the same string remain in their original order).
    Example: "ab" x "12" -> ab12, a12b, 12ab, 1ab2, 1a2b, a1b2
    """
    if left == "":
        if len(right) == 1:
            yield state + right
        else:
            yield from combinations(state + right[:1], "", right[1:])
    elif right == "":
        if len(left) == 1:
            yield state + left
        else:
            yield from combinations(state + left[:1], left[1:], "")
    else:
        yield from combinations(state + left[:1], left[1:], right)
        yield from combinations(state + right[:1], left, right[1:])
