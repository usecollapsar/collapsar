"""A CollapsarProvider Service Provider."""
from masonite.facades import Gate
from .CollapsarProvider import CollapsarProvider


class CollapsarApplicationProvider(CollapsarProvider):
    """
    A service provider for the Collapsar package.
    """
    def register_gates(self):
        """Define gates."""

        Gate.define("view-collapsar", lambda user: user.email in ["eduardo@aguad.dev"])
