from pydantic import BaseModel, create_model
from collection import generate_collection


real_art =  {
    "background": {
        "red": 60,     # 60%
        "green": 20,   # 20%
        "blue": 10,    # 10%
        "yellow": 10,  # 10%
    },
    "shape": {
        "circle":   10,  # 10%
        "retangle": 10,  # 10%
        "triangle": 70,  # 80%
        "pentagono": 10  # 80%
    },
    "quantity": {
        "1": 30,  # 30%
        "2": 30,  # 30%
        "3": 40,  # 40%
    }
}
c = generate_collection("RealArt", real_art, 1000)


with open("metadata.json", "w") as file:
    file.write(c.json())