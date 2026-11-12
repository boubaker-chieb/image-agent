from pathlib import Path
from uuid import uuid4

class LocalImageStore:
    def __init__(self, directory:Path) -> None:
        self.directory = directory

    def save(self, image:bytes) ->Path :
        self.directory.mkdir(parents=True, exist_ok=True)
        path = self.directory / f"{uuid4().hex}.png"
        path.write_bytes(image)
        return path
