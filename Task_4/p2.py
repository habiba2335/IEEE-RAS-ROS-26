import json

def save_inventory(data):
    with open("inventory.json", "w") as file:
        json.dump(data, file)

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


astro_store = {
    "Telescope": 5, 
    "Star Chart": 20, 
    "Astro-Camera": 3,
    "Tripod": 10
}

save_inventory(astro_store)

loaded_store = load_inventory()
print(loaded_store)