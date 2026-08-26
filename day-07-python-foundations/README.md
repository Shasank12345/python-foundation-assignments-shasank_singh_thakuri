# Day 7: Python Foundations

## Topics Covered

- Pandas fundamentals:
    - Reading data with `read_csv()`
    - `count()`, `sum()`, `isnull()`/`isna()`, `notnull()`/`notna()`
    - `apply()` with `lambda` functions for cleaning columns
    - Handling missing data with fallback values
    - `groupby()` and `mean()`/`sum()` aggregations
    - `sort_values()` and `idxmax()`
    - Merging DataFrames with `pd.merge()`
- Working with APIs:
    - Making GET requests with the `requests` library
    - Passing query parameters safely
    - Parsing JSON responses
    - Custom exceptions for clean error handling
    - Fallback/backup data when an API call returns nothing
- `assert` statements for validating logic during development

## Beyond the Class Material

For exercises 3 and 5, I also solved the aggregation using generators and manual dictionary accumulation (`dict.get()` for running totals/counts) alongside the `groupby()` approach — this wasn't taught in class, I did it to understand what `groupby()` is actually doing under the hood.

## Exercises

1. Load and Get — counting total checkouts and books not yet returned, validated with `assert`
2. Clean Data — creating an `is_returned` flag and filling missing `late_fee` values
3. Genre — average late fee per genre, solved two ways: a manual generator + dictionary approach, and a `groupby().mean()` approach
4. Lookup API — fetching book facts from the Open Library API, with a custom `BookNotFound` exception and a backup dictionary fallback
5. Merge — merging checkout records with book metadata, then calculating total late fees per author using both a generator/dictionary approach and a `groupby().sum()` approach
s
## How to Run

Run each file using:

```bash
python exercise-01-load-and-get.py
python exercise-02-clean-data.py
python exercise-03-genre.py
python exercise-04-lookupAPI.py
python exercise-05-merge.py
```

## What I Learned

I learned how to clean messy data with `isnull()`/`fillna()`, aggregate it with `groupby()`, and merge two DataFrames on a shared key. I also learned how to call a real external API with `requests`, parse JSON responses, and handle missing results gracefully using a custom exception and a backup dataset.

## Challenges Faced

Replacing `NaN` with `None` early on broke later arithmetic, and I hit a `KeyError` when an API response didn't come back in the shape I expected — both fixed by checking data more defensively before using it.