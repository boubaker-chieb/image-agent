import argparse

from pathlib import Path
from openai import OpenAI

from image_agent.generate_image import GenerateImage
from image_agent.local_image_store import LocalImageStore
from image_agent.openai_generator import OpenAiGenerator

from image_agent.agent import run_agent


def main() -> None:
    print("image agent started...")
    parser = argparse.ArgumentParser(description="The prompt to generate Image")
    parser.add_argument("prompt", help="Describe the image you want to generate")
    parser.add_argument("--direct", action="store_true", help="Skip the chat model.")
    args = parser.parse_args()

    prompt = args.prompt.strip()

    if not prompt:
        parser.error("Prompt can't be empty")

    with OpenAI() as client:
        use_case = GenerateImage(
            generator=OpenAiGenerator(client=client),
            store= LocalImageStore(directory=Path("generated")),
        )
        if args.direct:
            print(use_case.execute(prompt))
        else:
            print(run_agent(prompt, use_case))