from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path


FILE_TYPE_FOLDERS = {
	"Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tif", ".tiff"},
	"Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"},
	"Videos": {".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"},
	"Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"},
	"Archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"},
	"Programs": {".exe", ".msi", ".bat", ".cmd", ".sh", ".py", ".jar"},
}


def get_downloads_folder(custom_path=None):
	if custom_path:
		return Path(custom_path).expanduser().resolve()

	user_profile = os.environ.get("USERPROFILE")
	if user_profile:
		return Path(user_profile) / "Downloads"

	return Path.home() / "Downloads"


def get_category(file_path):
	extension = file_path.suffix.lower()
	for category, extensions in FILE_TYPE_FOLDERS.items():
		if extension in extensions:
			return category
	return "Others"


def ensure_unique_path(destination_path):
	if not destination_path.exists():
		return destination_path

	stem = destination_path.stem
	extension = destination_path.suffix
	parent = destination_path.parent
	counter = 1

	while True:
		candidate = parent / f"{stem} ({counter}){extension}"
		if not candidate.exists():
			return candidate
		counter += 1


def collect_files(downloads_folder):
	if not downloads_folder.exists():
		raise FileNotFoundError(f"Downloads folder not found: {downloads_folder}")

	files = []
	for item in downloads_folder.iterdir():
		if item.is_file():
			files.append(item)
	return sorted(files, key=lambda path: path.name.lower())


def build_moves(downloads_folder):
	moves = []
	for file_path in collect_files(downloads_folder):
		category = get_category(file_path)
		destination_folder = downloads_folder / category
		destination_path = ensure_unique_path(destination_folder / file_path.name)
		moves.append((file_path, destination_path, category))
	return moves


def print_plan(moves, downloads_folder):
	if not moves:
		print(f"No files found in {downloads_folder}.")
		return

	print(f"Planned organization for: {downloads_folder}")
	for source_path, destination_path, category in moves:
		print(f"- {source_path.name} -> {category}/{destination_path.name}")
	print(f"Total files to move: {len(moves)}")


def confirm(prompt):
	response = input(prompt).strip().lower()
	return response in {"y", "yes"}


def move_files(moves):
	for source_path, destination_path, _ in moves:
		destination_path.parent.mkdir(parents=True, exist_ok=True)
		shutil.move(str(source_path), str(destination_path))


def parse_args():
	parser = argparse.ArgumentParser(description="Organize files in the Downloads folder by file type.")
	parser.add_argument(
		"--downloads",
		help="Optional path to a Downloads folder for testing or custom use.",
	)
	parser.add_argument(
		"--apply",
		action="store_true",
		help="Actually move files after showing the dry-run preview.",
	)
	return parser.parse_args()


def main():
	args = parse_args()
	downloads_folder = get_downloads_folder(args.downloads)

	try:
		moves = build_moves(downloads_folder)
	except FileNotFoundError as error:
		print(error)
		return

	print_plan(moves, downloads_folder)

	if not moves:
		return

	if not args.apply:
		print("Dry run only. Re-run with --apply to move the files.")
		return

	if confirm("Proceed with moving these files? (y/n): "):
		move_files(moves)
		print("File organization complete.")
	else:
		print("No files were moved.")


if __name__ == "__main__":
	main()