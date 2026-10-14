**Project Assignment: Spatial Data Processing with Command-Line Interfaces**

**Objective:**
Develop a Python script named `gt_csv.py` that reads, processes, and filters spatial coordinate data for a track of colored cones. The script must utilize standard library modules to parse command-line arguments and handle CSV file operations.

**Requirements:**

1. **File I/O (`csv` module):**
* The script must read an input CSV file containing three columns: `color`, `x`, and `y`.
* You must strictly use Python's built-in `csv` module for reading and writing the data (do not use external libraries like `pandas`).


2. **Command-Line Interface (`argparse` module):**
* Implement a CLI using the `argparse` module.
* The script must accept one positional argument: the path to the input CSV file (e.g., `track.csv`).
* The script must accept an optional argument `--color` (e.g., `--color blue`) to filter the data by a specific cone color.


3. **Data Processing & Sorting:**
* When the `--color` argument is provided, the script must filter the dataset to include only cones of the specified color.
* Calculate the Euclidean distance of each filtered cone from the origin $(0,0)$ using the formula $d = \sqrt{x^2 + y^2}$.
* Output the filtered list of cones to the console, sorted in ascending order by their distance from the origin.



**Example Usage:**
Given a file named `track.csv` with the required format, executing the following command:

```bash
python gt_csv.py track.csv --color blue

```

*Expected Behavior:* The script reads `track.csv`, isolates all rows where the color is "blue", calculates their distance from the origin, and prints the sorted results to the terminal.

**Deliverables:**
Submit the `gt_csv.py` source code file. Ensure your code is well-commented, includes proper error handling for missing files, and adheres to standard Python styling (PEP 8).