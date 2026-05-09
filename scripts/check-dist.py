from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
REQUIRED = ["index.html", "styles.css", "bg_logo.jpg"]

missing = [str(file) for file in (DIST / filename for filename in REQUIRED) if not file.exists()]

if missing:
    print("Build verification failed. Missing files:")
    for file in missing:
        print(f"- {file}")
    raise SystemExit(1)

print("✅ Build verification passed. All expected files exist in dist/")
