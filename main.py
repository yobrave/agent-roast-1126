"""Package the one-line agent roast for the make.fun gate.

Reads entry.txt beside this file, validates the 200-character cap,
and copies the artifact into $MAKEFUN_OUTPUT_DIR with a JSON receipt.
"""
import json
import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
TAG = "agent-roast-1126"


def load_line():
    text = (ROOT / "entry.txt").read_text(encoding="utf-8")
    body = text.strip()
    if not body:
        raise SystemExit("entry line is blank")
    if len(body) > 200:
        raise SystemExit("entry line exceeds 200 characters")
    return body


def ship(line):
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8", newline="\n")
    receipt = {
        "artifact": "entry.txt",
        "chars": len(line),
        "tag": TAG,
        "verdict": "shipped",
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    ship(load_line())
