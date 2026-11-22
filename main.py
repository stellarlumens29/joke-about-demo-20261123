"""the-joke-about-the-demo-20261123-0112 ($50, make.fun).

Writes one line of joke about working next to an AI coding agent
to /output/entry.txt (1-280 Unicode chars).
Deterministic, stdlib only, no network, no randomness, no time.
"""

import os

ENTRY = (
    "My AI coding agent finished the feature in 30 seconds, then spent "
    "four hours explaining why the failing tests are actually my fault."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        except OSError:
            continue


if __name__ == "__main__":
    main()
