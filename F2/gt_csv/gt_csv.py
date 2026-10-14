import csv
import argparse
import sys
from pathlib import Path

#imports cones from the parent folder F2 then to cones file
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "cones"))

from cones import Cone, distance, filter_by_color, sort_by_distance


def read_cones(path: str) -> list[Cone]:
    #"""Read the CSV file and convert each row into a Cone."""
    cones = []
    with open(path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cones.append(Cone(
                color=row["color"].strip().lower(),
                x=float(row["x"]),  #CSV file values are strings, so convert
                y=float(row["y"]),
            ))
    return cones

def parse_args() -> argparse.Namespace:
    #creating parser
    parser = argparse.ArgumentParser(description="Filter Cones by color.")
    #absolutely needs the filepath so a positional arguement called "csv_file" is added
    parser.add_argument("csv_file", help="path to the input CSV file")
    #optional info so optional arguement to get color is added
    parser.add_argument("--color", help="only show cones of this color")
    #takes all the info returns the objects holding the values
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    filtered_cone = []

    try:
        raw_cones = read_cones(args.csv_file)
    except FileNotFoundError:
        sys.exit(f"Error: file '{args.csv_file}' not found.")

    #if --color arguement was given the script filters and prints the filtered data set as a list of distance from origin in order
    if args.color:
        print("Filtering for " + args.color.strip().lower())
        filtered_cone = filter_by_color(raw_cones, args.color.strip().lower())
        print(sort_by_distance(filtered_cone, Cone("origin", 0,0)))
    else:
        print("No filter, showing everything")
        print(sort_by_distance(raw_cones, Cone("origin", 0,0)))

if __name__ == "__main__":
    main()
   