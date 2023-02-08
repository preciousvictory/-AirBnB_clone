#!/usr/bin/python3
"""
A program that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Module defines the Cmd class
    Creating a command line interpreter is done by sub-classing the cmd.Cmd class.
    """
    prompt = '(hbnb) '

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
