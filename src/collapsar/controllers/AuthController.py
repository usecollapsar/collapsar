"""A AuthController Module."""
from masonite.controllers import Controller
from masonite.response import Response
from masonite.authentication import Auth
from masonite.facades import Gate

from ..CollapsarRequest import CollapsarRequest
from ..helpers.DashboardHelper import DashboardHelper


class AuthController(Controller):
    """AuthController Controller Class."""

    def index(self, dashboard_helper: DashboardHelper):
        """Handle AuthController request."""
        return dashboard_helper.render('auth/Login')

    def login(self, request: CollapsarRequest, response: Response, auth: Auth):
        """Handle login."""

        user = request.collapsar.get_user_model().where('email', request.input("email")).first()

        if not Gate.for_user(user).allows('view-collapsar'):
            return response.redirect('/collapsar/auth/login').with_errors({"global": "User unauthorized. Try again."})

        if (auth.attempt(request.input("email"), request.input("password"))):
            return response.redirect('/collapsar/')

        return response.redirect('/collapsar/auth/login').with_errors({"global": "Invalid credentials. Try again."})

    def logout(self, response: Response, auth: Auth):
        """Handle logout."""

        auth.logout()

        return response.redirect('/collapsar/auth/login')
