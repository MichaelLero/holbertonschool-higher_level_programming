#!/usr/bin/env python3

import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as file:
        # Your code here to serialize and save data to the specified filed
        json.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, "r") as file:
        # Your code here to load and deserialize data from the specified file
        return json.load(file)
