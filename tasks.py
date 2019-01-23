"""

Make-like task automation for Windows using python invoke

Supports:

inv clean
inv build
inv show
inv push <message>

Based on:

    https://github.com/mini-kep/parser-rosstat-kep/blob/dev/tasks.py

Original Windows workaround for invoke:

    https://github.com/pyinvoke/invoke/issues/371#issuecomment-259711426

"""
import sys
import os
import shutil


from sys import platform
from os import environ
from pathlib import Path

from invoke import Collection, task


def remove(path):
    if os.path.isfile(path):
        os.unlink(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


def remove_folder(folder, exclude=[".git", ".nojekyll"]):
    for path in os.listdir(folder):
        if path not in exclude:
            fullpath = os.path.join(folder, path)
            print("Deleting:", fullpath)
            remove(fullpath)


def walk_files(directory: Path):
    for _insider in directory.iterdir():
        if _insider.is_dir():
            subs = walk_files(_insider.resolve())
            for _sub in subs:
                yield _sub.resolve()
        else:
            yield _insider.resolve()


def yield_python_files(folder):
    for file in filter(lambda x: x.suffix == ".py", walk_files(folder)):
        yield file


@task
def pep8(ctx, folder=''):
    #path = PROJECT_DIR / 'src' / folder
    for f in yield_python_files(Path(".")):
        print("Formatting", f)
        # FIXME: may use 'import autopep8' without console
        ctx.run("autopep8 --aggressive --aggressive --in-place {}".format(f))


@task
def clean(ctx):
    """Wipe html documentation (not implemented)"""
    remove_folder("gh-pages")


def run(ctx, cmd):
    return ctx.run(cmd, hide=False, warn=True)


def run_all(ctx, commands):
    cmd = " && ".join(commands)
    return run(ctx, cmd)


@task
def ls(ctx):
    """List current directory"""
    run(ctx, "dir /b")


@task
def html(ctx):
    """Build html documentation with `sphinx-build`"""
    # WONT FIX: output is colorless
    run(ctx, "sphinx-build -b html docs gh-pages -c .")


@task
def pdf(ctx):
    pass


def quote(s):
    QUOTECHAR = '"'  # this is "
    return f"{QUOTECHAR}{s}{QUOTECHAR}"


@task
def push(ctx, message="build html"):
    """Build html documentation"""
    commands = ["cd gh-pages",
                "git add .",
                "git commit -am%s" % quote(message),
                "git push",
                "cd .."]
    run_all(ctx, commands)


@task
def show(ctx):
    """Show documentation in default browser"""
    run(ctx, "start gh-pages/index.html")


ns = Collection()
for t in [ls, clean, html, show, push, pdf, pep8]:
    ns.add_task(t)


# Workaround for Windows execution
if platform == 'win32':
    # This is path to cmd.exe
    ns.configure({'run': {'shell': environ['COMSPEC']}})