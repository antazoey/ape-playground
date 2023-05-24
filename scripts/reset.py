import shutil
from pathlib import Path
from tkinter.font import nametofont

import click
from ape import project


def delete_directories():
    directories = [
        project.contracts_folder,
        project.tests_folder,
        project.scripts_folder,
        project.local_project._cache_folder,
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


def reset_config_file():
    config_file = project.path / "ape-config.yaml"
    if config_file.is_file():
        config_file.unlink()

    config_file.touch()


@click.command("reset")
def cli():
    click.echo("Resetting...")
    delete_directories()
    reset_config_file()
