**Project Task: FSOCO Label Parsing and Dimensional Analysis**

**Objective:**
Develop a Python script (`labels_json.py`) that demonstrates the ability to generate, parse, and mathematically process standardized computer vision annotation data.

**Project Question:**
How can we implement a Python script that manually constructs a JSON data structure simulating three bounding box annotations according to the FSOCO dataset specification, parses this structure using the built-in `json` module, and systematically computes and outputs the class title, width, and height of each object based on its exterior bounding coordinates (`[[x1, y1], [x2, y2]]`)?

**Deliverable Requirements:**

* **Data Construction:** Hardcode a JSON string or dictionary representing three distinct objects (e.g., `blue_cone`, `yellow_cone`). The schema must strictly mirror the FSOCO format: `{"objects": [{"classTitle": "string", "points": {"exterior": [[x1, y1], [x2, y2]]}}]}`.
* **Data Parsing:** Utilize Python's standard `json` library to load and iterate through the `objects` array.
* **Geometric Calculation:** For each object, extract the exterior coordinate points and calculate the absolute width ($\vert{}x_2 - x_1\vert{}$) and height ($\vert{}y_2 - y_1\vert{}$) of the bounding box.
* **Execution Output:** Print a formatted terminal output displaying the extracted `classTitle`, computed `width`, and computed `height` for all three simulated objects.