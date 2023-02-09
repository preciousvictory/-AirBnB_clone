#!/usr/bin/python3
"""
A program that contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Module defines the Cmd class
    Creating a command line interpreter is done by sub-classing the
    cmd.Cmd class.
    """
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User']

    def do_quit(self, arg):
        """The quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """The  EOF (end of file) command to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def help_quit(self):
        """help documentation for quit command"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """help documentation for EOF command"""
        print("EOF command to exit the program\n")

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id
        """
        args = args.split()
        if len(args) != 1:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new = eval(args[0] + "()")
        new.save()
        print(new.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the
        class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = args.split()
        if len(args) < 1 or len(args) > 3:
            print("** class name missing **")
            return
        elif len(args) != 2:
            print("** instance id missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if all_objs[obj_id].id == args[1]:
                obj = all_objs[obj_id]
                print(obj)
                return
        print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = args.split()
        if len(args) < 1 or len(args) > 3:
            print("** class name missing **")
            return
        elif len(args) != 2:
            print("** instance id missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if all_objs[obj_id].id == args[1]:
                key = "BaseModel." + args[1]
                del storage._FileStorage__objects[key]
            storage.save()
        print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on
        the class name.
        Ex: $ all BaseModel or $ all
        """
        args = args.split()
        if len(args) == 1:
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

        all_objs = storage.all()
        all_ = []
        for obj_id in all_objs.values():
            obj = str(obj_id)
            all_.append(obj)

        print(all_)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = args.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        elif len(args) == 1 and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        all_objs = storage.all()
        c = 0
        for obj_id in all_objs.keys():
            if all_objs[obj_id].id == args[1]:
                c += 1
        if c == 0:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        args = args[:4]
        for obj_id, objc in all_objs.items():
            class_name = objc.__class__.__name__
            if class_name == args[0] and objc.id == args[1]:
                setattr(objc, args[2], args[3])
                storage.save()

        all_objs = storage.all()
        for obj_id in all_objs.values():
            obj = str(obj_id)
            print(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
