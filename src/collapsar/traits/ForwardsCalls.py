import re


class ForwardsCalls:
    """
    Forward a method call to the given object.
    """

    def forwards_call_to(self, target, method) -> any:
        """Forwards calls to the given object."""
        try:
            return getattr(target, method)
        except Exception as ex:
            pattern = r"^Call to undefined method (?P<class>[^:]+)::(?P<method>[^\(]+)\(\)$"

            matches = re.match(pattern, str(ex))

            if not matches:
                raise ex

            if (
                matches.group("class") != object.__class__.__name__
                or matches.group("method") != method
            ):
                raise ex

            raise AttributeError(f"Call to undefined method {method}() on {target}") from ex
