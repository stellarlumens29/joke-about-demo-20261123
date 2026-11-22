"""Tests for joke-about-demo-20261123: run `python3 test.py`.

Validates the ENTRY constant in main.py directly (no shell writes needed
to check the text itself) and, when run in a healthy environment, also
runs main.py and checks the written entry.txt.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import main as entry_main  # noqa: E402


def test_entry_length():
    text = entry_main.ENTRY
    assert isinstance(text, str)
    assert 1 <= len(text) <= 280, f"length {len(text)} out of range 1-280"
    assert text.strip() == text, "entry has leading/trailing whitespace"
    assert "\n" not in text, "joke must be a single line"
    print(f"entry length: {len(text)} chars (OK, 1-280)")


def test_committed_output_matches():
    committed = ROOT / "output" / "entry.txt"
    assert committed.exists(), "output/entry.txt missing from repo"
    assert committed.read_text(encoding="utf-8") == entry_main.ENTRY, (
        "output/entry.txt does not match ENTRY in main.py"
    )


def test_main_writes_entry():
    subprocess.run([sys.executable, "main.py"], cwd=ROOT, check=True)
    written = ROOT / "output" / "entry.txt"
    assert written.exists(), "main.py did not write output/entry.txt"
    assert written.read_text(encoding="utf-8") == entry_main.ENTRY
    subprocess.run([sys.executable, "main.py"], cwd=ROOT, check=True)
    assert written.read_text(encoding="utf-8") == entry_main.ENTRY, (
        "entry is not deterministic"
    )


if __name__ == "__main__":
    test_entry_length()
    test_committed_output_matches()
    test_main_writes_entry()
    print("all tests passed")
