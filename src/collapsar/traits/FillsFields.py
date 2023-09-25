from typing import List
from ..Field import Field


class FillsFields:
    @classmethod
    def fill(cls, request, model):
        """Fill the model with request parameters"""
        return FillsFields.fill_fields(
            request, model, cls(model).creation_fields_without_readonly()
        )

    # @staticmethod
    # def fill_for_update(request, model):
    #     return FillsFields.fill_fields(
    #         request, model, type(model)().update_fields_without_readonly(request)
    #     )

    # @staticmethod
    # def fill_pivot(request, model, pivot):
    #     instance = type(model)()
    #     return FillsFields.fill_fields(
    #         request, pivot, instance.creation_pivot_fields(request, request.related_resource)
    #     )

    # @staticmethod
    # def fill_pivot_for_update(request, model, pivot):
    #     instance = type(model)()
    #     return FillsFields.fill_fields(
    #         request, pivot, instance.update_pivot_fields(request, request.related_resource)
    #     )

    @classmethod
    def fill_fields(cls, request, model, fields: List[Field]) -> List:
        """Fill the model with request parameters"""
        return [
            model,
            list(
                map(lambda field: field.fill(request, model), fields),
            ),
        ]
