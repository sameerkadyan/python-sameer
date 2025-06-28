#           Variables and Data Types



#         Comments and Escape Sequence

# Single line comment :-

            # This is a comment
print("Hello!")  # This prints a greeting



# Multiline Comment :-

"""
This looks like a multi-line comment
but is actually a multi-line string
that isn't assigned to a variable.
"""


# What are Escape Sequences in Python?

"""

Escape sequences are special characters used to represent things like newlines, tabs, or quotes inside a string.
They begin with a backslash (\).


Escape              Meaning

\n                  New line
\t                  Tab
\\                  Backlash(\)
\'                  single quote(')
\"                  Double quote(")
\b                  Backspace

"""


#   What is a Variable in Python?

"""
A variable in Python is a name that refers to a value stored in memory.
It lets you store, use, and change data in your program.

"""

#    Key Rules for Python Variables:

"""
1.  No need to declare a type (Python is dynamically typed)


    x = 10        # int
    x = "hello"   # now it's a string!


2.  Variable names:

    Must start with a letter or _

    Can include letters, digits, and _

    Are case-sensitive (Name and name are different)

    Can't be Python keywords (if, for, class, etc.)

3.  Invalid names:

    1name = "wrong"     # Do not starts with number
    my-name = "oops"    # Do not contains dash

"""


# What is a Data Type?
"""

A data type tells Python what kind of value a variable holds and what operations can be done with it.

"""

# Python Data Types Structure

"""
Python Data Types
├── 1. Primitive Data Types (Built-in, Simple Types)
│   ├── int        → Integer numbers (e.g., 5, -3)
│   ├── float      → Decimal numbers (e.g., 3.14)
│   ├── complex    → Complex numbers (e.g., 2 + 3j)
│   ├── bool       → Boolean (True / False)
│   ├── str        → Text strings (e.g., "hello")
│   └── NoneType   → Special type with value None
│
└── 2. Non-Primitive Data Types (Data Structures / Collections)
    ├── list       → Ordered, mutable collection (e.g., [1, 2, 3])
    ├── tuple      → Ordered, immutable collection (e.g., (1, 2))
    ├── dict       → Key-value pairs (e.g., {"a": 1})
    ├── set        → Unordered, unique elements (e.g., {1, 2, 3})
    └── frozenset  → Immutable version of set


"""
