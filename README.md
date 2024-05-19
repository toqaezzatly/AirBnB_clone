# AirBnB_clone
AirBnB_clone
# AirBnB Clone Project

Welcome to the AirBnB clone project! This project is the first step towards building a full web application, the AirBnB clone. This initial phase involves creating a command interpreter to manage AirBnB objects.

## Project Description

The AirBnB clone project aims to build a simplified version of the AirBnB web application. In this first step, we will develop a command interpreter that will enable us to:

- Manage the creation, updating, and deletion of AirBnB objects such as Users, Places, States, and Cities.
- Serialize and deserialize objects to and from a JSON file.
- Implement a parent class, `BaseModel`, to handle object initialization, serialization, and deserialization.
- Develop unit tests to ensure the functionality of all classes and the storage engine.

## Command Interpreter

### How to Start It

1. **Clone the Repository**: Clone this repository to your local machine using:
   ```sh
   git clone https://github.com/your-username/AirBnB_clone.git
   ```
2. **Navigate to the Project Directory**:
   ```sh
   cd AirBnB_clone
   ```
3. **Run the Command Interpreter**:
   ```sh
   ./console.py
   ```

### How to Use It

The command interpreter provides a simple way to interact with your AirBnB objects. You can enter commands to create, update, delete, and perform other operations on objects.

#### Commands

- `help`: Displays a list of available commands.
- `create <class_name>`: Creates a new instance of the specified class.
- `show <class_name> <id>`: Displays the details of an instance based on its class and ID.
- `destroy <class_name> <id>`: Deletes an instance based on its class and ID.
- `all [<class_name>]`: Displays all instances of the specified class, or all instances if no class is specified.
- `update <class_name> <id> <attribute_name> <attribute_value>`: Updates an instance's attribute based on its class, ID, attribute name, and attribute value.

### Examples

#### Creating a New Object

To create a new User:
```sh
(hbnb) create User
```

#### Showing an Object

To show the details of a User with ID `1234-5678-9012`:
```sh
(hbnb) show User 1234-5678-9012
```

#### Destroying an Object

To delete a User with ID `1234-5678-9012`:
```sh
(hbnb) destroy User 1234-5678-9012
```

#### Updating an Object

To update the `name` attribute of a User with ID `1234-5678-9012`:
```sh
(hbnb) update User 1234-5678-9012 name "John Doe"
```

#### Showing All Objects

To show all User objects:
```sh
(hbnb) all User
```

To show all objects of all classes:
```sh
(hbnb) all
```

### Conclusion

This command interpreter is a foundational part of the AirBnB clone project, setting the stage for further development involving web frameworks, databases, and front-end integration. Each part of this project builds on the previous one, creating a comprehensive and functional clone of the AirBnB platform.
