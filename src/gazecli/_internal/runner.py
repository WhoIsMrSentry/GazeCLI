from __future__ import annotations

import runpy
import sys
from contextlib import contextmanager
from pathlib import Path


def _looks_like_repo_root(path: Path) -> bool:
    return (path / "pyproject.toml").exists() or (path / "src" / "gazecli").exists()


def repo_root() -> Path:
    """Best-effort repo root discovery.

    Öncelik:
    1) Bu dosyanın konumuna göre (editable install senaryosu)
    2) Mevcut çalışma dizini ve üstleri
    """
    candidate = Path(__file__).resolve().parents[3]
    if _looks_like_repo_root(candidate):
        return candidate

    cwd = Path.cwd().resolve()
    for p in [cwd, *cwd.parents]:
        if _looks_like_repo_root(p):
            return p

    # En azından anlamlı bir varsayılan döndür.
    return candidate


@contextmanager
def _prepend_sys_path(path: Path):
    path_str = str(path)
    sys.path.insert(0, path_str)
    try:
        yield
    finally:
        # remove first occurrence (in case user had same path earlier)
        try:
            sys.path.remove(path_str)
        except ValueError:
            pass


def run_script(path: Path) -> None:
    """Run a python file like `python path/to/script.py`.

    Ensures the script directory is on sys.path for local imports.
    """
    script_path = path.resolve()
    if not script_path.exists():
        raise FileNotFoundError(f"Script bulunamadı: {script_path}")

    with _prepend_sys_path(script_path.parent):
        runpy.run_path(str(script_path), run_name="__main__")


def run_module(module_name: str) -> None:
    """Run a module like `python -m module_name`."""
    runpy.run_module(module_name, run_name="__main__")
