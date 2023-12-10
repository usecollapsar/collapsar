from masonite.inertia import InertiaMiddleware
from masonite.helpers import optional


class HandleInertiaRequestsMiddleware(InertiaMiddleware):

    def resolve_validation_errors(self, request):
        """Get validation errors in flash session if any and serialize it to be easy to use
        client-side."""
        session = self.get_session(request)
        if not session.has("errors"):
            return None

        errors = session.get("errors")

        return errors.all() if hasattr(errors, "all") else errors

    def resolve_success_message(self, request):
        """Get success message in flash session if any and serialize it to be easy to use
        client-side."""
        session = self.get_session(request)
        if not session.has("success"):
            return None
        else:
            return session.get("success")

    def share(self, request):
        """Share for all requests:
        - validation errors
        - user data (when logged in)
        - active route name
        """
        errors = self.resolve_validation_errors(request)
        success = self.resolve_success_message(request)

        # user looks already shared in session by Auth module ?
        # user = {}
        # if request.user():
        #     user = user.serialize()

        active_route = optional(request.route)._name

        return {
            "errors": errors,
            "success": success,
            "active_route": active_route,
            # "user": user,
        }
