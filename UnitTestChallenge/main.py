import pytest

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

def perimter_test():
    assert perimeter(4, 5) == 18
    with pytest.raises(ValueError, match="Undefined"):
        perimeter(0, 5)
    with pytest.raises(ValueError, match="Not a number"):
        perimeter("four", 5)
    with pytest.raises(ValueError, match="Dimension cannot be negative"):
        perimeter(-4, 5)

if __name__ == "__main__":
    perimter_test()
    print("All tests passed")