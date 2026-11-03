
from pathlib import Path
from PIL import Image

IMAGE_DIR = Path(__file__).resolve().parent / "images"
SIZES = [480, 768, 1200]
NAMES = ["python-web", "django", "flask", "fastapi"]

IMAGE_DIR.mkdir(exist_ok=True)
print("Папка изображений:", IMAGE_DIR)
print("Файлы в папке:")

for file in IMAGE_DIR.iterdir():
    print(file.name)

for name in NAMES:
    candidates = [
        IMAGE_DIR / f"{name}.png",
        IMAGE_DIR / f"{name}.jpg",
        IMAGE_DIR / f"{name}.jpeg",
    ]

    source = next((p for p in candidates if p.exists()), None)

    if source is None:
        print(f"Пропущено: не найден исходник для {name}")
        continue

    with Image.open(source) as original:
        image = original.convert("RGB")

        for width in SIZES:
            height = round(image.height * width / image.width)
            resized = image.resize(
                (width, height),
                Image.Resampling.LANCZOS
            )

            output = IMAGE_DIR / f"{name}-{width}.webp"
            resized.save(
                output,
                "WEBP",
                quality=85,
                method=6
            )

            print(f"Создано: {output} ({width}x{height})")

print("Готово!")
