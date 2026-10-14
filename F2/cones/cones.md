**Project Question:**

Create a Python module named `cones.py`. Within this module, complete the following requirements:

1. Define a `@dataclass` named `Cone` with the attributes `color` (`str`), `x` (`float`), and `y` (`float`).
2. Implement a function `distance` that calculates the distance between two `Cone` objects.
3. Implement a function `filter_by_color` that filters a list of `Cone` objects by a given color.
4. Implement a function `sort_by_distance` that sorts a list of `Cone` objects by their distance to a specific reference point.
5. Implement a function `nearest` that returns the closest `Cone` to a specific reference point from a list, or returns `None` if the list is empty.