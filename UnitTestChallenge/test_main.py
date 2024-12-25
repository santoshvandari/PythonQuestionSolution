import pytest
from main import perimeter

def test_perimeter():
    assert perimeter(4, 5) == 18
    with pytest.raises(ValueError, match="Undefined"):
        perimeter(0, 5)
    with pytest.raises(ValueError, match="Not a number"):
        perimeter("four", 5)
    with pytest.raises(ValueError, match="Dimension cannot be negative"):
        perimeter(-4, 5)
