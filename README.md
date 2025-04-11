# Orderly Set 5.4.0

Orderly Set is a package containing multiple implementations of Ordered Set.


## OrderlySet

This implementation keeps the order in all set operations except set difference operations.
As a result, it can do set difference operations much faster than other implementations. Still 2X slower than of Python's built-in set.


## StableSet

A StableSet is a mutable set that remembers its insertion order.
Featuring: Fast O(1) insertion, deletion, iteration and membership testing.
But slow O(N) Index Lookup.

## StableSetEq

Same as StableSet but the order of items doesn't matter for equality comparisons.

## OrderedSet

An OrderedSet is a mutable data structure that is a hybrid of a list and a set.
It remembers its insertion order so that every entry has an index that can be looked up. 
Featuring: O(1) Index lookup, insertion, iteration and membership testing.
But slow O(N) Deletion.


## SortedSet

SortedSet is basically set but when printed, turned into string, or iterated over, returns the items in alphabetical order.

# Installation

`pip install orderly-set`

# Usage examples

An OrderedSet is created and used like a set:

    >>> from orderly_set import OrderedSet

    >>> letters = OrderedSet('abracadabra')

    >>> letters
    OrderedSet(['a', 'b', 'r', 'c', 'd'])

    >>> 'r' in letters
    True

It is efficient to find the index of an entry in an OrderedSet, or find an
entry by its index. To help with this use case, the `.add()` method returns
the index of the added item, whether it was already in the set or not.

    >>> letters.index('r')
    2

    >>> letters[2]
    'r'

    >>> letters.add('r')
    2

    >>> letters.add('x')
    5

OrderedSets implement the union (`|`), intersection (`&`), and difference (`-`)
operators like sets do.

    >>> letters |= OrderedSet('shazam')

    >>> letters
    OrderedSet(['a', 'b', 'r', 'c', 'd', 'x', 's', 'h', 'z', 'm'])

    >>> letters & set('aeiou')
    OrderedSet(['a'])

    >>> letters -= 'abcd'

    >>> letters
    OrderedSet(['r', 'x', 's', 'h', 'z', 'm'])

The `__getitem__()` method has been extended to accept any
iterable except a string, returning a list, to perform NumPy-like "fancy
indexing".

    >>> letters = OrderedSet('abracadabra')

    >>> letters[[0, 2, 3]]
    ['a', 'r', 'c']

    >>> letters.indexes(['a', 'r', 'c'])
    [0, 2, 3]

OrderedSet implements `__getstate__` and `__setstate__` so it can be pickled,
and implements the abstract base classes `collections.MutableSet` and
`collections.Sequence`.

OrderedSet can be used as a generic collection type, similar to the collections
in the `typing` module like List, Dict, and Set. For example, you can annotate
a variable as having the type `OrderedSet[str]` or `OrderedSet[Tuple[int,
str]]`.


# Authors

Please check the [Authors](AUTHORS.md) file.

# Comparisons

```
-- initialize a set --
Using Python dict time: 4.13
set time: 2.98
ordered_set.OrderedSet time: 15.77
orderly_set.OrderedSet time: 15.25
StableSet time: 4.78
OrderlySet time: 4.38
SortedSet time: 3.09

-- update a set --
Using Python dict: 6.77
set time: 2.46
ordered_set.OrderedSet time: 10.17
orderly_set.OrderedSet time: 10.06
StableSet time: 7.16
OrderlySet time: 6.77
SortedSet time: 2.46

-- update a set and get item --
ordered_set.OrderedSet time: 29.98
orderly_set.OrderedSet time: 29.57
StableSet time: 14.31
OrderlySet time: 14.23
SortedSet time: 9.03

-- set symmetric difference (xor) --
set time: 5.368663903005654
ordered_set.OrderedSet time: 39.25
orderly_set.OrderedSet time: 80.31
StableSet time: 42.81
OrderlySet time: 11.44
SortedSet time: 3.87

-- set difference (-) --
set time: 3.7398674299911363
ordered_set.OrderedSet time: 22.39
orderly_set.OrderedSet time: 38.00
StableSet time: 22.30
OrderlySet time: 8.92
SortedSet time: 3.03
```

Despite what you see in the benchmarks, in DeepDiff OrderlySet performed better than SortedSet.


A StableSet is a mutable set that remembers its insertion order.
Featuring: Fast O(1) insertion, deletion, iteration and membership testing.
But slow O(N) Index Lookup.

An OrderedSet is a mutable data structure that is a hybrid of a list and a set.
It remembers its insertion order so that every entry has an index that can be looked up. 
Featuring: O(1) Index lookup, insertion, iteration and membership testing.
But slow O(N) Deletion.

Both have similar interfaces but differ in respect of their implementation and performance.

The original implementation of OrderedSet was a [recipe posted to ActiveState
Recipes][recipe] by Raymond Hettiger, released under the MIT license.

[recipe]: https://code.activestate.com/recipes/576694-orderedset/

Hettiger's implementation kept its content in a doubly-linked list referenced by a
dict. As a result, looking up an item by its index was an O(N) operation, while
deletion was O(1).

This version of OrderedSet makes different trade-offs for the sake of efficient lookups. 
Its content is a standard Python list instead of a doubly-linked list. This
provides O(1) lookups by index at the expense of O(N) deletion, as well as
slightly faster iteration.
