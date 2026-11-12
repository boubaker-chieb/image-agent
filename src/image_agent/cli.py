import argparse

from pathlib import Path
from openai import OpenAI

from image_agent.generate_image import GenerateImage
from image_agent.local_image_store import LocalImageStore
from image_agent.openai_generator import OpenAiGenerator


def main() -> None:
    print("image agent started...")
    parser = argparse.ArgumentParser(description="The prompt to generate Image")
    parser.add_argument("prompt", help="Describe the image you want to generate")
    args = parser.parse_args()

    prompt = args.prompt.strip()

    if not prompt:
        parser.error("Prompt can't be empty")

    with OpenAI() as client:
        use_case = GenerateImage(
            generator=OpenAiGenerator(client=client),
            store= LocalImageStore(directory=Path("generated")),
        )
        print(use_case.execute(prompt))