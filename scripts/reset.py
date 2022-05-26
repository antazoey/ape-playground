import shutil
from pathlib import Path
from tkinter.font import nametofont

import click
from ape import project


@click.command("reset")
def cli():
    click.echo("Resetting...")

    directories = [
        project.contracts_folder,
        project.tests_folder,
        project.scripts_folder,
    ]
    whitelisted_names = [
        n
        for n in (Path(__file__).parent.parent / "whitelist.txt")
        .read_text()
        .split("\n")
        if n
    ]
    for directory in directories:
        for file_path in directory.iterdir():
            if file_path.is_file() and file_path.name not in whitelisted_names:
                file_path.unlink()
            elif file_path.is_dir():
                shutil.rmtree(file_path)
