import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Provisioner settings."""

    EVENTING_HOST: str
    CREATE_EVENT_TRIGGER_ENDPOINT: str = "event-triggers"

    class Config:
        """Meta config."""

        env_file = (
            os.environ.get("MAVIS_CONFIG")  # check if the path specified.
            if os.environ.get("MAVIS_CONFIG") is not None
            else "./.env"
        )
        env_file_encoding = "utf-8"
        case_sensitive = True


provisioner_settings = Settings()  # type: ignore
