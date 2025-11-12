# Simple Python Scripts Collection

A small collection of standalone Python scripts intended for learning, testing, and utility tasks. Each script is independent and can be run on its own.

## Quick start
1. Install Python 3.x (3.7+ recommended).
2. (Optional) Create and activate a virtual environment:
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows
3. Run a script:
   python 1prg.py

## Scripts
Open the individual files to see details and any required input. Each entry below gives a short description; inspect the script headers for usage examples.

- 1prg.py — simple input/output example script; demonstrates basic Python I/O.
- 2prg.py — basic arithmetic or control-flow example (see file for exact behavior).
- 3prg.py — string/sequence manipulation example.
- 4prg.py — demonstrates use of functions and/or basic data structures.
- 5prg.py — small utility or algorithm example (check top of file for usage).
- 6prg.py — file or data processing example.
- 7prg.py — example showing loops and conditionals.
- 8prg.py — miscellaneous utility or example script.

Tip: Add a one-line description at the top of each script (as a comment) so the README can be updated with precise summaries.

## Requirements
- Python 3.x
- If a script needs third-party packages, add a `requirements.txt` and install with:
  pip install -r requirements.txt

## Run examples
Run a single script:
python 1prg.py

Run all scripts in the folder (bash):
for f in *.py; do python "$f"; done

Run all scripts in PowerShell:
Get-ChildItem -Filter *.py | ForEach-Object { python $_.FullName }

## Contributing
- Update the script list above with concise descriptions after inspecting each file.
- If you add scripts that depend on packages, update `requirements.txt`.
- File formatting: keep scripts small and self-contained; include usage notes in comments.

## License & contact
- Add a LICENSE file to state the project's license (MIT, Apache-2.0, etc.).
- For questions or improvements, add a brief contact or project maintainer line here.

<!-- End of README -->