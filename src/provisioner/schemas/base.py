from abc import ABC
from dataclasses import dataclass
from typing import Generic, Mapping, Type, TypeVar

from app.provisioner.errors import ProvisionerPermanentError


@dataclass
class SpecSchema:
    pass


TSchema = TypeVar("TSchema", bound=SpecSchema)


class SchemaValidator(ABC, Generic[TSchema]):
    def __init__(self, data: Mapping, schema: Type[TSchema]) -> None:
        self.data = data
        self.schema = schema

    def validate(self) -> TSchema:
        for key, value in self.data.items():
            if validate_func := getattr(self, f"validate_{key}", None):
                validate_func(key, value)

        try:
            return self.schema(**self.data)
        except TypeError as err:
            raise ProvisionerPermanentError(str(err))
