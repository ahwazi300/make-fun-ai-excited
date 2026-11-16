"""Make the AI judge excited — entry program.

Copies the bundled image to /output/entry.png.
Deterministic: no network, no randomness, same bytes on every run.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.jpg"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
