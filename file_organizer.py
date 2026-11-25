
import shutil
from pathlib import Path

print("AUTOMATIC FILE ORGANIZER")
print("=" * 35)

# Folder containing files to organize
folder = Path("unsorted_files")
folder.mkdir(exist_ok=True)

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".doc"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
}

print(f"\nOrganizing files in: {folder}")

moved_count = 0
failed_count = 0

for file in folder.iterdir():

    if not file.is_file():
        continue

    category = "Others"

    for name, extensions in categories.items():
        if file.suffix.lower() in extensions:
            category = name
            break

    destination = folder / category

    try:
        destination.mkdir(exist_ok=True)

        new_location = destination / file.name

        # Avoid overwriting existing files
        counter = 1

        while new_location.exists():
            new_location = destination / f"{file.stem}_{counter}{file.suffix}"
            counter += 1

        shutil.move(str(file), str(new_location))

        print(f"Moved: {file.name} -> {category}")
        moved_count += 1

    except OSError as error:
        print(f"Could not move {file.name}: {error}")
        failed_count += 1

print("\n" + "=" * 35)
print("ORGANIZATION SUMMARY")
print(f"Files moved successfully: {moved_count}")
print(f"Files failed: {failed_count}")
print("Organization completed!")
