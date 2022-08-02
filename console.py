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

    def do_show(self, line):
        """
        Prints the string representation
        of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        if line:
            args = line.split(" ")
            if args[0] not in self.classes:
                print("** class doesn't exist **")
# If the class name doesn’t exist, print ** class doesn't exist **
# (ex: $ show MyModel)
                return
            if len(args) < 2:
                print("** instance id missing **")
# If the id is missing, print ** instance id missing **
# (ex: $ show BaseModel)
                return
            key = args[0] + "." + args[1]
            obje = storage.all()
            if key not in obje:
                print("** no instance found **")
# If the instance of the class name doesn’t exist for the id,
# print ** no instance found ** (ex: $ show BaseModel 121212)
                return
            print(obje[key])
        else:
            print('** class name missing **')
# If the class name is missing, print ** class name missing **
# (ex: $ show)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        if line:
            args = line.split(" ")
            if args[0] not in self.classes:
                # If the class name doesn’t exist,
                # print ** class doesn't exist **
                # (ex:$ destroy MyModel)
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                # If the id is missing,
                # print ** instance id missing **
                # (ex: $ destroy BaseModel)
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            obje = storage.all()
            if key not in obje:
                # If the instance of the class name
                # doesn’t exist for the id
                # print ** no instance found **
                # (ex: $ destroy BaseModel 121212)
                print("** no instance found **")
                return
            del obje[key]
            storage.save()
        else:
            # If the class name is missing,
            # print ** class name missing **
            # (ex: $ destroy)
            print('** class name missing **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
