from PIL import Image
from pathlib import Path


if __name__ == "__main__":
    key = Path("public_key.pem")
    image = Path("image.png")
    result = key.with_name("public_key.png")

    Image.open(image)
    result.write_bytes(image.read_bytes() + key.read_bytes())
    Image.open(result)
