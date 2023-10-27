"""User Add Command."""
from getpass import getpass

from masonite.commands.Command import Command
from masonite.facades.Hash import Hash

class UserAddCommand(Command):
    """
    Installs collapsar

    collapsar:user
    """

    def __init__(self, application):
        super().__init__()
        self.app = application

    def handle(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = getpass("Enter your password: ")

        from app.models.User import User
        User().create({"name": name, "email": email, "password": Hash.make(password)})

        self.info("User created successfully")
