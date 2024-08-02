0x00-python_variable_annotations


Type annotations in Python provide a way to indicate the expected types of variables, function arguments, and return values. They help improve code readability, documentation, and facilitate early error detection when using tools like mypy.

Basic Type Annotations
You can annotate variables and function signatures using built-in types like int, float, str, bool, and list.

Example:

python
code
# Annotating variables
age: int = 25
name: str = "John Doe"
is_student: bool = True

# Annotating function arguments and return values
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Example function call
print(greet("Alice"))  # Output: Hello, Alice!
Type Annotations for Collections
When working with collections, you can use the typing module to specify types for lists, tuples, dictionaries, and sets.

Example:

python
code
from typing import List, Tuple, Dict, Set

# Annotating a list of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Annotating a tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Annotating a dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Annotating a set of strings
unique_names: Set[str] = {"Alice", "Bob", "Charlie"}
Custom Types with Classes
You can also annotate types using custom classes.

Example:

python
code
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Annotating a variable with a custom type
person: Person = Person("Alice", 30)
Optional Types
Sometimes a variable or a return value can be None. You can use Optional from the typing module to indicate this.

Example:

python
Copy code
from typing import Optional

# Annotating an optional string
nickname: Optional[str] = None

def get_nickname(name: str) -> Optional[str]:
    if name == "Alice":
        return "Ally"
    return None

# Example function call
print(get_nickname("Alice"))  # Output: Ally
print(get_nickname("Bob"))    # Output: None
Duck Typing
Duck typing focuses on the behavior of objects rather than their explicit types. If an object behaves like a certain type (e.g., it has the necessary methods), it can be used as that type.

Example:

python
Copy code
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I can quack like a duck!"

def make_quack(duck_like: 'DuckType'):
    print(duck_like.quack())

# Using duck typing
make_quack(Duck())   # Output: Quack!
make_quack(Person()) # Output: I can quack like a duck!
Type Checking with mypy
mypy is a static type checker for Python. It can be used to validate your code against the provided type annotations, catching errors early.

Example:

python
Copy code
# Save this as example.py
def add(a: int, b: int) -> int:
    return a + b

# Running mypy on this file
# Command: mypy example.py
If you introduce a type error, mypy will catch it:

Example with error:

python
Copy code
def add(a: int, b: int) -> int:
    return a + b

result = add(1, "2")  # Type error: Argument 2 to "add" has incompatible type "str"; expected "int"

# Running mypy will produce an error message
# Command: mypy example.py
# Output: example.py:4: error: Argument 2 to "add" has incompatible type "str"; expected "int"
Learning Resources
Python 3 Typing Documentation
Mypy Cheat Sheet
By following these examples and utilizing the learning resources, you can effectively use type annotations in your Python code, making it more robust and easier to understand.
---------------------------

Certainly! Let's delve deeper into the differences between Iterable and Sequence, and how they are used in Python type annotations.

Iterable vs. Sequence
Iterable
An Iterable is a general concept that represents any object that can be iterated over. This means any object that can return its elements one at a time. The primary requirement for an object to be considered an iterable is that it implements the __iter__ method, which returns an iterator.

Examples of Iterables:

Lists: [1, 2, 3]
Tuples: (1, 2, 3)
Sets: {1, 2, 3}
Dictionaries: {'a': 1, 'b': 2, 'c': 3}
Generators: (x for x in range(3))
Strings: "abc"
Sequence
A Sequence is a more specific subtype of Iterable. In addition to being iterable, a sequence supports efficient element access using integer indices and has a defined order of elements. This means that sequences implement both the __iter__ method (making them iterables) and the __getitem__ method, which allows access to elements by their position.

Examples of Sequences:

Lists: [1, 2, 3]
Tuples: (1, 2, 3)
Strings: "abc"
