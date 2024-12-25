# Unit Test Challenge

Below is a sample pseudocode that calculates the perimeter of a rectangle by taking the length and breadth as input. Create a Pytest (snippet will be enough) to ensure maximum test coverage, such that every line inside the function body is executed at least once.

```python
function perimeter(length, breadth) {
    if(!length || !breadth) {
        throw Exception(‘Undefined’);
    }
    
    if(length is not Number) {
        throw Exception(‘Not a number’);
    }
    
    if(breadth is not Number) {
        throw Exception(‘Not a number’);
    }
                   
    if(length < 0 OR breadth < 0) {
        throw Exception(‘dimension cannot be negative’);
    }
   
    return 2 * (length + breadth);
}

```
