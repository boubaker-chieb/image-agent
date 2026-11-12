from pathlib import Path
from typing import Protocol

class ImageGenerator(Protocol):
    def generate(self, prompt) -> bytes: ...

class ImageStore(Protocol):
    def save(self, image: bytes) -> Path: ...

class GenerateImage:
    def __init__(self, generator: ImageGenerator, store: ImageStore) -> None:
        self.generator = generator
        self.store = store

    def execute(self, prompt: str) -> Path:
        prompt = prompt.strip()
        if not prompt:
            raise ValueError("The prompt cannot be empty")
        image = self.generator.generate(prompt)
        return self.store.save(image=image)
    