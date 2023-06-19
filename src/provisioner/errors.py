from kopf import PermanentError


class ProvisionerPermanentError(PermanentError):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)
