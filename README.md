# AirBnB Clone - The console

This project is part of the development of an AirBnB clone. The main goal of this project is to build a simple command-line interpreter that will allow us to manage objects for our AirBnB clone. This command-line interpreter will enable us to create, update, destroy, and show various objects such as users, states, cities, places, and more. Additionally, we will implement a file storage system for our objects.

## Getting Started

To get started with the project, you can follow the instructions below:

1. Clone the project repository from GitHub.
2. Navigate to the project directory.
3. Run the command-line interpreter using the provided script.

## Project Structure

The project is structured as follows:

- `console.py`: Contains the command-line interpreter code.
- `models/`: Directory containing the classes for different AirBnB objects.
- `models/base_model.py`: Defines the `BaseModel` class responsible for the initialization, serialization, and deserialization of instances.
- `models/user.py`: Contains the `User` class.
- `models/state.py`: Contains the `State` class.
- `models/city.py`: Contains the `City` class.
- `models/place.py`: Contains the `Place` class.
- `models/engine/`: Directory containing the storage engine implementation.
- `models/engine/file_storage.py`: Implements the file storage engine for the project.
- `tests/`: Directory containing all the unit tests for the project.

## How to Use the Console

The console is the primary interface for managing objects in our AirBnB clone. It supports various commands such as create, show, destroy, update, and all. The console allows us to interact with the different objects and perform necessary actions.

To use the console:

1. Run the `console.py` script.
2. Enter commands following the specified format for each action.

## Storage Engine

The project implements a file storage engine, allowing us to serialize and deserialize objects to and from JSON files. This storage engine is a simple implementation for now, and it may be extended or replaced with a more advanced database system in future iterations.

## Running Tests

To ensure the correctness of our classes and storage engine, we have provided unit tests. These tests validate the functionality of each class and the storage engine. To run the tests, execute the following command:

```
python -m unittest discover tests
```

## Authors

- [Agure Odeny]
- [Alex Kinyua]
