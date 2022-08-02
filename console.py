#!/usr/bin/python3
# Import the command line module
# Import the base model module
# Import the datetime module
import cmd
from models.base_model import BaseModel
from models import storage
from datetime import datetime


# Declare the HBNBCommand class
class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point of the command interpreter
    """
    prompt = '(hbnb)'
    classes = {"BaseModel"}

# quit and EOF to exit the program

    def do_EOF(self, line):
        """
        End-Of-File command to exit the program
        """
        return true

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Example: $ create BaseModel
        """
# If the class name is missing, print ** class name missing ** (ex: $ create)
# If the class name doesn’t exist, print ** class doesn't exist **
# (ex: $ create MyModel)
        try:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
