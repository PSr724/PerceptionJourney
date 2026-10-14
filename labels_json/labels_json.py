import json

json_string = """
{
  "objects": [
    {
      "classTitle": "blue_cone",
      "points": {
        "exterior": [[10, 20], [50, 100]]
      }
    },
    {
      "classTitle": "yellow_cone",
      "points": {
        "exterior": [[120, 45], [165, 130]]
      }
    },
    {
      "classTitle": "orange_cone",
      "points": {
        "exterior": [[300, 250], [270, 190]]
      }
    }
  ]
}
"""
data = json.loads(json_string)

for obj in data["objects"]:
    print("Class Title is " + obj["classTitle"])
    print("Width is " + str(abs(obj["points"]["exterior"][0][0]-obj["points"]["exterior"][1][0])))
    print("Height is " + str(abs(obj["points"]["exterior"][0][1]-obj["points"]["exterior"][1][1])))
    

