def perimeter(length, breadth):
    if not length or not breadth:
        raise ValueError("Undefined")
    if not isinstance(length, (int, float)):
        raise ValueError("Not a number")
    if not isinstance(breadth, (int, float)):
        raise ValueError("Not a number")
    if length < 0 or breadth < 0:
        raise ValueError("Dimension cannot be negative")
    return 2 * (length + breadth)

