**Part 4: Unit Testing the Cones Module (`test_cones.py`)**

**Objective:**
Develop a robust unit testing suite using the `pytest` framework to validate the data structures and functional logic implemented in your `cones.py` module.

**Requirements:**

1. **Framework & Setup:** Create a new file named `test_cones.py` and import `pytest` alongside the `Cone` dataclass and functions (`distance`, `filter_by_color`, `sort_by_distance`, and `nearest`) from `cones.py`.
2. **Test Volume:** Write a minimum of **8 distinct test functions**. These tests should comprehensively evaluate standard inputs across all functions.
3. **Mandatory Edge Cases:** Your test suite must explicitly account for the following scenarios:
* **The Empty List:** Verify that the `nearest` function correctly handles an empty input list without throwing an exception, strictly returning `None`.
* **Equidistant Cones:** Test the behavior of `sort_by_distance` and `nearest` when provided with two or more cones that calculate to the exact same distance. Ensure the functions handle tie-states predictably without crashing.


4. **Data Isolation:** Ensure each test is isolated. You may construct sample `Cone` objects directly within the test functions or utilize `pytest` fixtures to supply standard test data.

**Deliverable:**
Submit the `test_cones.py` file. The file must execute successfully when running `pytest test_cones.py` in the terminal, yielding zero errors or failures across all 8+ tests.