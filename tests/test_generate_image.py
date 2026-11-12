from pathlib import Path

from image_agent.generate_image import GenerateImage
from image_agent.local_image_store import LocalImageStore


class FakeImageGenerator:
    def generate(self, prompt: str) -> bytes:
        assert prompt == "A fox"
        return b"test image bytes"


def test_generate_image_saves_bytes(tmp_path: Path) -> None:
    use_case = GenerateImage(FakeImageGenerator(), LocalImageStore(tmp_path))

    path = use_case.execute("  A fox  ")

    assert path.parent == tmp_path
    assert path.suffix == ".png"
    assert path.read_bytes() == b"test image bytes"