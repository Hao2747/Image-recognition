from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class ImagePath:
    root_path: Path = Path(__file__).parent
    generated_digits_path: Path = root_path / "output" / "generated_digits"
    generated_models_path: Path = root_path / "output" / "generated_models"
