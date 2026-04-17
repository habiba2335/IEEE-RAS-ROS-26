import json

def initialize_system():
    filename = "config.json"
    try:
        with open(filename, "r") as file:
            json.load(file)
        print("System Ready.")
    except FileNotFoundError:
        default_settings = {"theme": "dark", "language": "English"}
        with open(filename, "w") as file:
            json.dump(default_settings, file)
        print("Config file missing. Created with default settings.")

initialize_system()