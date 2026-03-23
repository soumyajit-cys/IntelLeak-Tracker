import os

DATA_PATH = "data/sample_breach.txt"

def fetch_breach_data():
    if not os.path.exists(DATA_PATH):
        return []

    with open(DATA_PATH, "r") as file:
        return file.readlines()