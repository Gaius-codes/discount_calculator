# Rectangle and Square Classes

A Python project demonstrating object-oriented programming (OOP) concepts through the implementation of `Rectangle` and `Square` classes.

## Features

- Create `Rectangle` objects with customizable width and height.
- Create `Square` objects that inherit from `Rectangle`.
- Calculate:
  - Area
  - Perimeter
  - Diagonal length
- Update dimensions using setter methods.
- Generate an ASCII representation of a shape.
- Determine how many smaller shapes fit inside a larger rectangle.
- Meaningful string representations for both classes.

## Technologies

- Python 3

## Project Structure

```
.
└── main.py
```

## Example

```python
rectangle = Rectangle(10, 5)

print(rectangle.get_area())        # 50
print(rectangle.get_perimeter())   # 30
print(rectangle.get_diagonal())    # 11.18...

square = Square(5)

print(square.get_area())           # 25

square.set_side(8)
print(square)                      # Square(side=8)
```

## Methods

### Rectangle

- `set_width(width)`
- `set_height(height)`
- `get_area()`
- `get_perimeter()`
- `get_diagonal()`
- `get_picture()`
- `get_amount_inside(shape)`

### Square

- `set_side(side)`
- `set_width(width)`
- `set_height(height)`

## Concepts Demonstrated

- Object-Oriented Programming (OOP)
- Classes and Objects
- Inheritance
- Method Overriding
- Constructor Chaining
- Encapsulation
- Polymorphism
- ASCII Art Generation