"""Classes are the backbone of Object-Oriented Programming (OOP) in Python, just like in many
other programming languages. A class is a blueprint for creating objects (a particular data
structure), providing initial values for state (member variables or attributes),
and implementations of behavior (member functions or methods).

IMPORTANT REMARKS:
1. Classes are defined using the `class` keyword. Naming conventions suggest using CamelCase.
2. The `__init__` method is a constructor, called when a new instance is created.
3. The `self` parameter refers to the instance itself, used to access its attributes and methods.
4. Methods are functions defined within a class that operate on instances.
5. Attributes are variables that hold data associated with a class and its instances.
6. You can create multiple instances, each with its own set of attributes.
7. Classes can have class variables (shared) and instance variables (unique to each instance)."""


def attend_class() -> None:
    """General function — not tied to any specific student."""
    print("Attending class...")


class Student:
    """Represents a student with name, age, and study behaviors."""

    def __init__(self, name: str = "", age: int = 0) -> None:
        self.name = name
        self.age = age

    def study(self) -> None:
        """Student studies — uses self to know WHO is studying."""
        print(f"{self.name} is studying...")

    def take_exam(self) -> None:
        """Student takes an exam."""
        print(f"{self.name} is taking an exam...")

    def introduce(self) -> None:
        """Student introduces themselves."""
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


# Create instances with attributes set directly
student1 = Student("Sameh", 25)
student2 = Student("Hassan", 26)

# Call methods — each student performs their own action
attend_class()
student1.study()
student1.take_exam()
student1.introduce()

attend_class()
student2.study()
student2.take_exam()
student2.introduce()