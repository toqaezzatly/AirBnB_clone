#!/usr/bin/python3
#!/usr/bin/env python3
import cmd
import sys
import models

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")  # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(cls, args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(cls, args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objs = models.storage.all()
        if not arg:
            print([str(objs[obj]) for obj in objs])
        else:
            try:
                print([str(objs[obj]) for obj in objs if obj.startswith(arg)])
            except KeyError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = args[0]
            if cls not in models.storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(cls, args[1])
            if key not in models.storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr = args[2]
            value = args[3]
            obj = models.storage.all()[key]
            setattr(obj, attr, value)
            obj.save()
        except KeyError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

