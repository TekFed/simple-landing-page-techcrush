from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
FILES = ["index.html", "styles.css", "bg_logo.jpg"]

if DIST.exists():
    shutil.rmtree(DIST)

DIST.mkdir(parents=True, exist_ok=True)

for filename in FILES:
    src = ROOT / filename
    dst = DIST / filename
    if not src.exists():
        raise FileNotFoundError(f"Missing required file: {src}")
    shutil.copy2(src, dst)

print("✅ Build completed. Files copied to dist/")
