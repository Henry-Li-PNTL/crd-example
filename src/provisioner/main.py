from os import path as os_path
from typing import Any, Mapping
import markdown
import os

import kopf



@kopf.on.startup()
async def op_startup(logger: kopf.Logger, **kwargs: Any) -> None:
    logger.info("Markdown transformer provisioner started.")


@kopf.on.create("markdowns", retries=3, backoff=30.0)
async def create_event_trigger(
    logger: kopf.Logger, spec: Mapping, name: str | None, namespace: str | None, **kwargs: Any
):
    if not name or not namespace:
        return {"status_code": 400, "message": f"Invalid name or namespace: {namespace}/{name}"}

    logger.info(f"receive eventtriggers {namespace}/{name} spec={spec}")

    with open(f"archive/{namespace}-{name}.html", "w", encoding="utf-8") as f:
        f.write(markdown.markdown(spec["content"]))

    return {"status_code": 200}


@kopf.on.delete("markdowns", retries=3, backoff=30.0)
async def delete_event_trigger(
    logger: kopf.Logger, name: str | None, namespace: str | None, **kwargs: Any
):
    if not name or not namespace:
        return {"status_code": 400, "message": f"Invalid name or namespace: {namespace}/{name}"}

    logger.info(f"receive eventtriggers delete {namespace}/{name}")

    os.remove(f"archive/{namespace}-{name}.html")

    return {"status_code": 200}
