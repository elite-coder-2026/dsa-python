# Bug Fixes

## polynomial-hash.py - Hash Assignment Bug

**Location:** `math/polynomial-hash.py:43-44`

**Issue:**
The `compute_hashes` function was incorrectly assigning the entire list objects to array indices instead of the computed hash values.

**Incorrect Code:**
```python
hsh[i] = hsh      # Assigns the list itself
_hsh[i] = _hsh    # Assigns the list itself
```

**Fixed Code:**
```python
hsh[i] = h1       # Assigns the computed hash value
_hsh[i] = h2      # Assigns the computed hash value
```

**Explanation:**
The function computes rolling polynomial hashes in variables `h1` and `h2` during each iteration of the loop (lines 37-38). These accumulated hash values should be stored at each position in the `hsh` and `_hsh` arrays to create a prefix hash array.

The bug would have caused:
- Each position in the array to reference the list itself rather than containing a hash value
- Runtime errors or incorrect hash comparisons when trying to use these values
- The polynomial hash functionality to be completely broken

**Why This Matters:**
Polynomial hashing is used for efficient string matching and comparison. The prefix hash array allows computing the hash of any substring in O(1) time. Without storing the correct progressive hash values, the entire algorithm fails to work.

**Pattern Recognition:**
This is a common mistake when working with accumulator variables - forgetting to store the accumulated value and instead referencing the container. Always ensure you're storing the computed value (`h1`, `h2`) not the storage container (`hsh`, `_hsh`).
