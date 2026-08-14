# Day 4: Python Foundations

## Topics Covered

- Exceptions Handling
    - try,except,else,finally
    - Custom Exceptions
- Logging
    - DEBUGG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
## Exercises

1. Line & Word Counter
2. Inventory Value from Csv
3. Filtering a json Library
4. Custom Exceptiion
5. Order Pipeline with Logging

## How to Run

Run each file using:

```bash
python exercise-01-line-and-word-counter.py
python exercise-02-inventory-value-csv.py
python exercise-03-filtering-json.py
python exercise-04-custom-exception.py
python exercise-05-pipeline-logging.py
```

## What I Learned

I learned how to handle errors properly using try, except, else, and finally, instead of letting a program crash on bad input or a missing file. I also practiced creating custom exception classes for situations that Python's built-in exceptions didn't quite fit, which helped me understand how exceptions can carry more specific, meaningful information about what went wrong. On the logging side, I learned the difference between the five logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) and when each one is appropriate, and how logging is a much better tool than print statements for tracking what a real program is doing.

## Challenges Faced

Reading CSV and JSON files safely was trickier than expected, since I had to account for missing fields, invalid data types, and files that might not exist at all, without letting any single bad record crash the whole program. Deciding where to use try/except versus where to validate data before it even reaches that point took some trial and error, and figuring out the right balance between catching errors too broadly versus too narrowly was a real challenge.