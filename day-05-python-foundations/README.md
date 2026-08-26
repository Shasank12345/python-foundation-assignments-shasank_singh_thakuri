# Day 5: Python Foundations

Covers three subfolders: lambda/functional programming, generators & iterators, and list/dict/set comprehensions.

```
day-05-python-foundations/
├── README.md
├── generator-and-iterators/
├── lambda-function/
└── list-set-dict-comprehension/
```

## Part 1: Lambda & Functional Programming

**Topics:** `lambda`, `map()`, `filter()`, `sorted()` with a `key`, `functools.reduce()`, dispatch tables, custom exceptions

1. `exercise-01-fun-and-lamda-func.py` — comparing a regular function vs. an equivalent one-line lambda
2. `exercise-02-map-filter.py` — squaring and filtering a list with `map()`/`filter()`, then the same logic rewritten as comprehensions
3. `exercise-03-sort.py` — sorting a word list alphabetically, by length, and by length descending using `sorted(key=lambda ...)`
4. `exercise-04-dict.py` — sorting a list of dicts by age, and finding the youngest/oldest with `min()`/`max()` + `key=lambda`
5. `exercise-05-dispatch.py` — a calculator using a dispatch table (`{'add': lambda ...}`) instead of `if/elif`, with a custom `InvalidChoice` exception
6. `exercise-06-reduce.py` — using `functools.reduce()` to compute a product and to flatten a nested list
7. `exercise-07-max-using-reduce.py` — reimplementing `max()` from scratch using `reduce()` and a `key`
8. `challenge-exercise.py` — a data processing pipeline: `map`/`filter`/`reduce`/`sorted` on sales records, a generator to stream surviving products, and a dispatch-table formatter (short/verbose/json/csv) driven by an interactive menu

## Part 2: Generators & Iterators

**Topics:** `iter()`/`next()`/`StopIteration`, generator functions, generator expressions vs. list comprehensions, custom iterator classes, lazy file streaming

1. `exercise-01-iter-list.py` — manually iterating a list with `iter()` and `next()`
2. `exercise-02-generator.py` — a generator function counting up to a user-given number
3. `exercise-03-gen-even.py` — a generator yielding even numbers up to a limit
4. `exercise-04-gen-comp.py` — comparing memory usage of a list comprehension vs. a generator expression with `sys.getsizeof()`
5. `exercise-05-sliding-window.py` — a generator-based sliding window (prev/current/next value tracking)
6. `exercise-06-gen-class.py` — a custom iterator built as a class with `__iter__`/`__next__`
7. `exercise-07-read-file-gen.py` — reading a file in fixed-size line chunks using a generator
8. `challenge-exercise-part-A.py` — a menu-driven log processor: read raw lines, parse log fields with regex, or filter to error-only records, all via generators
9. `challenge-exercise-part-B.py` — an infinite Fibonacci generator paired with a `take()` helper to pull a limited number of values

## Part 3: List / Dict / Set Comprehensions

**Topics:** list, dict, and set comprehensions; nested comprehensions; comprehensions with `if` filters; comprehension key-collision behavior

1. `exercise-01-list-of-cubes.py` — list of cubes from 1–10 using a list comprehension
2. `exercise-02-clean-string.py` — stripping whitespace from a list of strings via comprehension
3. `exercise-03-set-of-unique-vowel.py` — a set comprehension for unique vowels in a string
4. `exercise-04-mapping-number-checking-condition.py` — dict comprehension mapping each number to whether it's even
5. `exercise-05-dict-with-word-mapped-to-lenght.py` — dict comprehension mapping word length to word, filtered by length
6. `exercise-06-array-conversion.py` — flattening a matrix into a vector with a nested comprehension, filtered to even numbers
7. `exercise-07-swap-key-value.py` — swapping dictionary keys and values with a comprehension, and noting how duplicate values get silently overwritten
8. `exercise-08-dict-map-log-with-count.py` — dict comprehension mapping log level to line length, then a corrected version using length as the key to avoid overwriting duplicate levels
9. `challenge-exercise.py` — a mini log analyzer: extracting error-only lines, a set of unique users, and a list of (user, message) tuples for failed logins, all built with list/set comprehensions and small helper functions

## How to Run

```bash
python exercise-01-fun-and-lamda-func.py
python exercise-02-map-filter.py
python exercise-03-sort.py
python exercise-04-dict.py
python exercise-05-dispatch.py
python exercise-06-reduce.py
python exercise-07-max-using-reduce.py
python challenge-exercise.py          

python exercise-01-iter-list.py
python exercise-02-generator.py
python exercise-03-gen-even.py
python exercise-04-gen-comp.py
python exercise-05-sliding-window.py
python exercise-06-gen-class.py
python exercise-07-read-file-gen.py
python challenge-exercise-part-A.py
python challenge-exercise-part-B.py

python exercise-01-list-of-cubes.py
python exercise-02-clean-string.py
python exercise-03-set-of-unique-vowel.py
python exercise-04-mapping-number-checking-condition.py
python exercise-05-dict-with-word-mapped-to-lenght.py
python exercise-06-array-conversion.py
python exercise-07-swap-key-value.py
python exercise-08-dict-map-log-with-count.py
python challenge-exercise.py          
```

## What I Learned

I learned when to reach for a `lambda` (short, throwaway, inline logic like a sort key) versus a proper `def` function, and built dispatch tables to replace `if/elif` chains with dictionary lookups. On the generator side, I learned how `yield` and `iter()`/`next()`/`StopIteration` actually work, confirmed with `sys.getsizeof()` that generators stay constant in memory while list comprehensions grow, and built a class-based iterator to see what a `for` loop does internally. With comprehensions, I practiced list/dict/set forms, nested comprehensions for flattening data, and ran into real key-collision behavior when two items map to the same dictionary key.

## Challenges Faced

Getting the sliding-window and dispatch-table exercises right took a few iterations — mainly bugs from mutable default arguments, indexing a dict incorrectly, and functions/variables shadowing each other by sharing the same name. The comprehension exercises surfaced a subtle bug class of their own: using a value that isn't unique (like log level) as a dictionary key silently overwrites earlier entries, which pushed me to pick keys more carefully.