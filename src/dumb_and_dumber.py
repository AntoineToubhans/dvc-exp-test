import random
import json

random.seed = 42
dumbest = random.random()

with open("data/dumbest.json", "w") as f:
    json.dump({"dumbest": dumbest}, f)
