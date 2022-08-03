#!/usr/bin/python3
# Import the command line module
# Import the base model module
# Import the datetime module
import cmd
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json
import re


# Declare the HBNBCommand class
class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point of the command interpreter
    """
    prompt = '(hbnb)'
    classes = {"BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"}

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

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        my_list = []
        objs = storage.all()
        if line:
            args = line.split(" ")
            if args[0] not in self.classes:
                # If the class name doesn’t exist,
                # print ** class doesn't exist **
                # (ex: $ all MyModel)
                print("** class doesn't exist **")
                return
            for key in objs:
                split_key = key.split(".")
                if split_key[0] == args[0]:
                    my_list.append(str(objs[key]))
            print(my_list)
        else:
            for key in objs:
                my_list.append(str(objs[key]))
            print(my_list)
            # The printed result must be a list of strings

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if line:
            args = line.split(" ")
# Usage: update <class name> <id> <attribute name> "<attribute value>"
# Only one attribute can be updated at the time
# You can assume the attribute name is valid (exists for this model)
# The attribute value must be casted to the attribute type
            if args[0] not in self.classes:
                # If the class name doesn’t exist,
                # print ** class doesn't exist **
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                # If the id is missing, print ** instance id missing **
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            objs = storage.all()
# If the instance of the class name doesn’t exist for the id,
# print ** no instance found ** (ex: $ update BaseModel 121212)
            if key not in objs:
                print("** no instance found **")
                return
            if len(args) < 3:
                # If the attribute name is missing,
                # print ** attribute name missing **
                print("** attribute name missing **")
                return
            if len(args) < 4:
                # If the value for the attribute name doesn’t exist,
                # print ** value missing **
                print("** value missing **")
                return
            if args[2] not in ['id', 'created_at', 'updated_at']:
                # id, created_at and updated_at cant’ be updated.
                # You can assume they won’t be passed
                # in the update command
                setattr(objs[key], args[2].replace('"', ''), eval(args[3]))
                objs[key].save()
# If the class name is missing, print ** class name missing **
# (ex: $ update)
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
