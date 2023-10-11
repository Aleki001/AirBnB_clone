#!/usr/bin/python3

""" AirBnB console """

import cmd

class HBNBCommand(cmd.Cmd):
    """Enables commandline interpretter """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """Exits the program on ctrl + D """
        return True

    def emptyline(self):
        """Ignores empty lines/spaces """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

