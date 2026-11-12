from openai import OpenAI
from base64 import b64decode

class OpenAiGenerator():
    def __init__(self, client: OpenAI) -> None:
        self.client = client

    def generate(self, prompt:str) -> bytes:
        response = self.client.images.generate(
            model="gpt-image-2.5-flare",
            prompt=prompt,
            size="1024x1024",
            quality="low",
            output_format="png",
            n=1
        )
        encoded = response.data[0].b64_json if response.data else None
        if not encoded:
            raise RuntimeError("The api returned no image data")
        return b64decode(encoded)