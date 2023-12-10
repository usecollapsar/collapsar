"""A AuthController Module."""
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request
from masonite.authentication import Auth
from ..helpers.DashboardHelper import DashboardHelper


class AuthController(Controller):
    """AuthController Controller Class."""

    def index(self, dashboard_helper: DashboardHelper):
        """Handle AuthController request."""
        return dashboard_helper.render('auth/Login')

    def login(self, request: Request, response: Response, auth: Auth):
        """Handle login."""

        if (auth.attempt(request.input("email"), request.input("password"))):
            return response.redirect('/collapsar/')

        return response.redirect('/collapsar/auth/login').with_errors({"global": "Invalid credentials. Try again."})

    def logout(self, response: Response, auth: Auth):
        """Handle logout."""

        auth.logout()

        return response.redirect('/collapsar/auth/login')
