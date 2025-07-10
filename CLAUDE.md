# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `orderly-set`, a Python package that provides multiple implementations of ordered sets. The package includes five main set implementations:

- **StableSet**: A dict-based ordered set that maintains insertion order with O(1) operations but O(N) index lookup
- **OrderedSet**: A list-based ordered set with O(1) index lookup but O(N) deletion
- **StableSetEq**: Like StableSet but with different equality semantics (ignores order for equality)
- **OrderlySet**: Keeps order on insertion but loses order on set operations like difference
- **SortedSet**: A set that maintains alphabetical order when displayed or iterated

## Development Commands

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=orderly_set

# Run specific test file
pytest tests/test_ordered_set_1.py

# Run doctests (configured in pytest.ini)
pytest --doctest-modules --doctest-glob=README.md
```

### Code Quality
```bash
# Format code
black .

# Type checking
mypy orderly_set/

# Lint code
flake8 orderly_set/
```

### Build and Distribution
```bash
# Install in development mode
uv pip install -e ".[coverage,dev,static,test]"
```

### Multi-version Testing
```bash
# Test across Python versions
tox
```

## Code Architecture

### Core Module Structure
- `orderly_set/__init__.py`: Package exports
- `orderly_set/sets.py`: Main implementation file containing all set classes
- `orderly_set/py.typed`: Type stub marker

### Key Implementation Details

**StableSet** (lines 55-681 in sets.py):
- Uses `dict.fromkeys()` for O(1) operations
- Maintains insertion order via Python 3.7+ dict ordering
- Index lookup requires O(N) iteration through dict keys

**OrderedSet** (lines 816-1057 in sets.py):
- Uses separate `_items` list and `_map` dict for O(1) index access
- `_map` stores `{item: index}` mappings
- Deletion requires reindexing all subsequent items

**Type System**:
- Uses generics extensively with `TypeVar("T")` 
- Implements `MutableSet[T]` and `Sequence[T]` protocols
- Complex type annotations for set operations and indexing

### Performance Characteristics
- StableSet: Fast for all operations except index lookup
- OrderedSet: Fast index lookup but slow deletion
- OrderlySet: Optimized for set operations, loses order guarantees
- SortedSet: Maintains sorted order with lazy evaluation

## Configuration Files

- `pytest.ini`: Test configuration with doctest support
- `setup.cfg`: Flake8 linting config (max line length 120)
- `tox.ini`: Multi-version testing for Python 3.8-3.10, PyPy3
- `requirements-dev.txt`: Development dependencies
