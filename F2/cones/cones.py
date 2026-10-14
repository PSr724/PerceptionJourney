from dataclasses import dataclass
from math import sqrt

@dataclass
class Cone:
    color: str
    x: float
    y: float

# Calculates distance between 2 cones using pythagorean theorem
def distance(cone1: Cone, cone2: Cone) -> float:
    return sqrt((cone1.x - cone2.x)**2 + (cone1.y - cone2.y)**2)

# Filters through given list of cones finds the one matching the color and returns new list
def filter_by_color(cone_list: list[Cone], cone_color: str) -> list[Cone]:
    cone_list2 = []
    for cone in cone_list:
        if cone.color == cone_color:
            cone_list2.append(cone)
    return cone_list2

# Sorts list by distance to specified reference cone and returns a new list
def sort_by_distance(cone_list: list[Cone], reference_cone: Cone) -> list[Cone]:
    return sorted(cone_list, key=lambda current_cone: distance(reference_cone, current_cone))

# Returns the cone that is closest to the reference point; if empty, returns None
def nearest(cone_list: list[Cone], reference_cone: Cone) -> Cone | None:
    if not cone_list:
        return None
    
    sorted_cones = sort_by_distance(cone_list, reference_cone)
    return sorted_cones[0]