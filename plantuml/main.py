from uml import FindUML, PlantUML
from pathlib import Path

class GenerateImages:
		def __init__(self, base: Path) -> None:
			self.finder = FindUML(base)
			self.painter = PlantUML()

		def make_all_images(self) -> None:
			for source, target in self.finder.uml_file_iter():
					if (
							not target.exists()
							or source.stat().st_mtime > target.stat().st_mtime
						):
							print(f"Processing {source} -> {target}")
							self.painter.process(source)
					else:
							print(f"Skipping {source} -> {target}")

if __name__ == "__main__":
	generator = GenerateImages(Path.cwd())
	generator.make_all_images()