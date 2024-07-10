FILEPATH = "todos.txt"


# Only functions with a return value need to be assigned to a variable, see get_todos below
def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns the list
     of to-do items inside the file.
    """
    with (open(filepath, 'r') as file_local):
        todos_local = file_local.readlines()
    return todos_local


# Functions that don't return anything don't need to be assigned to a variable, see write_todos below
def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())

