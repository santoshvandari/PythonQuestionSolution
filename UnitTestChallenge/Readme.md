# Unit Test Challenge

### Running the Tests
- Install the pytest package:
```bash
pip install pytest
```

- Execute the following command:
```bash
pytest test-main.py
```


## Example Test Cases
Here are some of the test cases validated in the suite:
- **Valid Input**: `perimeter(4, 5)` returns `18`.
- **Undefined Input**: `perimeter(0, 5)` raises a `ValueError` with the message `"Undefined"`.
- **Non-Numeric Input**: `perimeter("four", 5)` raises a `ValueError` with the message `"Not a number"`.
- **Negative Dimension**: `perimeter(-4, 5)` raises a `ValueError` with the message `"Dimension cannot be negative"`.

---
