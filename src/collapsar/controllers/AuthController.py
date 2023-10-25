"""A AuthController Module."""
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request
from masonite.authentication import Auth


class AuthController(Controller):
    """AuthController Controller Class."""

    def login(self, request: Request, response: Response, auth: Auth):
        """Handle login."""

        if (auth.attempt(request.input("email"), request.input("password"))):
            return response.redirect('/collapsar/')

        return response.redirect('/collapsar/auth/login')

    def logout(self, response: Response, auth: Auth):
        """Handle logout."""

        auth.logout()

        return response.redirect('/collapsar/auth/login')
