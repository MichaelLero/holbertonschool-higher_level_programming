#!/usr/bin/env python3

import pickle


def serialize_and_save_to_file(data, filename):
    with open(filename, "wb") as file:
        # Your code here to serialize and save data to the specified filed
        pickle.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, "rb") as file:
        # Your code here to load and deserialize data from the specified file
        return pickle.load(file)
