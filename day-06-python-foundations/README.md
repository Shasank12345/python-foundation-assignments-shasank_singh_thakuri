# Day 6: Python Foundations

## Topics Covered

- Decorators:
    - Writing basic decorators with `*args`/`**kwargs` pass-through
    - `functools.wraps` for preserving a wrapped function's `__name__` and `__doc__`
    - Parameterized decorators (decorator factories) — e.g. `retry(times, delay)`
    - Stacking multiple decorators and how execution order changes (`@timer @log_calls` vs `@log_calls @timer`)
    - Modifying arguments inside a wrapper before calling the original function (e.g. uppercasing string args)
    - Practical use-cases: timing, retrying, banner/greeting formatting, audit logging, role-based access control, and a simple routing table
- OOP:
    - `@property` / `@x.setter` for validated attribute access
    - Class-level (shared) attributes vs. instance attributes
    - `@classmethod` as an alternate constructor / factory method
    - Inheritance and method overriding with `super()`
    - Abstract base classes (`ABC`, `@abstractmethod`) and polymorphism
    - Custom exceptions for domain-specific error handling
    - Encapsulation using private, name-mangled attributes


## Exercises

### Decorators

1. Greeting Decorator — `shout` decorator that uppercases string arguments and wraps the output with "Greetings" / "!!!"
2. Banner Decorator — wraps a function's output with a line of `=` (40 characters) printed before and after
3. Timer Decorator — measures and prints how long the wrapped function took to run, using `functools.wraps` and `time.perf_counter()`
4. Property Decorator — a `Temperature` class whose `celcious` setter rejects values at or below absolute zero, plus a `farenheit` property that converts the stored value
5. Repeat Decorator — a parameterized `retry(times, delay)` decorator that reruns a function a set number of times with a delay between runs
6. Stacking Decorators — combining `@timer` and `@log_calls` in different orders to see how the order changes both behavior and measured execution time
7. Challenge: Mini Access-Controlled Router — `@route`, `@audit_log`, and `@requires_role` decorators layered on a `BankAccount` transfer function, with custom exceptions for negative balance, insufficient funds, and denied permissions

### OOP

1. Class Basics — a `BOOK` class using `@property`/`@setter` to store title and author as a validated tuple
2. Class Attribute — a `Book` class with a class-level `count` attribute that tracks how many books have been created
3. Abstract Shapes & Polymorphism — an abstract `Shape` base class with `Circle` and `Rectangle` subclasses, plus a custom exception for invalid input types
4. Bank Account — encapsulation with a private balance validated through `@property`, and custom exceptions for negative balance and insufficient funds
5. Classmethod Constructor — an alternate `Book.from_string()` constructor built with `@classmethod`
6. Inheritance — a `Vehicle` → `Car` → `SuperCar` chain demonstrating `super()` and method overriding
7. Polymorphism with an Abstract Base Class — a `PaymentMethod` ABC with `Esewa` and `MobileBanking` subclasses each implementing `pay()` differently
8. Challenge: Mini Library Management System — an abstract `LibraryItem` base class with `Book`, `DVD`, and `Magazine` subclasses, plus `Member` and `Library` classes and a `classmethod` factory (`from_catlog`) that builds the right item type from raw dictionary data

## How to Run

**Decorators**

```bash
python exercise-01-greetingdecorator.py
python exercise-02-bannerdecorator.py
python exercise-03-timerdecorator.py
python exercise-04-propertydecorator.py
python exercise-05-repeatdec.py
python exercise-06-stackingdec.py
python ChallengeExercise.py
```

**OOP**

```bash
python exercise-01-class.py
python exercise-02-countattribute.py
python exercise-03-polyshape.py
python exercise-04-bankaccount.py
python exercise-05-constructor.py
python exercise-06-inheritatnce.py
python exercise-07-polymorphism.py
python Challenge-exercise.py
```

## What I Learned

I learned how a decorator is really just a function that takes a function and returns a new one, and how `functools.wraps` keeps the wrapped function's identity intact instead of letting the wrapper's name and docstring leak through. Stacking decorators made it clear that order matters — the closest decorator to the function runs "innermost," which changes both behavior and what gets measured or logged. On the OOP side, I got more comfortable using `@property` to validate data on the way in rather than after the fact, using `@classmethod` as a factory for building objects from different input shapes, and using an abstract base class to force subclasses to implement a shared method while still letting each one behave differently (polymorphism).

## Challenges Faced

Getting the execution order right in the stacking-decorators exercise took some tracing through by hand — `@timer @log_calls` and `@log_calls @timer` look almost identical but wrap the function in the opposite order, which changes what each decorator actually measures. In the property-decorator exercise, I named my custom exception `ValueError`, the same as the built-in — that made it easy to accidentally shadow the built-in exception, so I had to be careful about which `ValueError` was actually being raised and caught. In the challenge exercises, keeping track of which custom exception should fire for which invalid action (already-checked-out item, insufficient balance, denied permission) took a bit of trial and error to get the exact conditions right.