from __future__ import annotations
import re
from pathlib import Path
from typing import Iterator, Tuple
import subprocess

class FindUML:
    def __init__(self, base: Path) -> None:
        self.base = base
        self.start_pattern = re.compile(r"@startuml *(.*)")

    def uml_file_iter(self) -> Iterator[tuple[Path, Path]]:
        for source in self.base.glob("**/*.uml"):
            if any(n.startswith(".") for n in source.parts):
                continue
            body = source.read_text()
            for output_name in self.start_pattern.findall(body):
                if output_name:
                    target = source.parent / output_name
                else:
                    target = source.with_suffix(".png")
                yield (
                    source.relative_to(self.base),
                    target.relative_to(self.base)
								)

class PlantUML:
	#conda_env_name = "py" # FIXME: Hardcoded
	#base_env = Path.home() / "miniconda3" / "envs" / conda_env_name # FIXME: Hardcoded
	base_env = Path('/')
	# FIXME: Hardcoded
	def __init__(
					self,
					graphviz: Path = Path("usr") / "local" / "bin" / "dot",
					plantjar: Path = Path.home() / "projects" / "plantuml.jar",
				) -> None:
			self.graphviz = self.base_env / graphviz
			self.plantjar = self.base_env / plantjar

	def process(self, source: Path) -> None:
			env = {
							"GRAPHVIZ_DOT": str(self.graphviz),
					}
			command = [
					"java", "-jar",
					str(self.plantjar), "-progress",
					str(source)
			]
			subprocess.run(command, env=env, check=True)
			print()

