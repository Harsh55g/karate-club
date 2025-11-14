Project: Karate Club Modularity Assignment

This repository contains code to perform recursive spectral modularity partitioning on Zachary's Karate Club graph.

Files of interest:
- `DSC212_Assignment_HarshSuthar_fixed.ipynb` — Repaired notebook (run interactively in Jupyter/VS Code).
- `run_assignment.py` — Non-interactive runner that executes the same analysis and writes visualization PNGs.
- `requirements.txt` — Python dependencies.

Quick run (Windows PowerShell):

1. Create and activate virtualenv (optional but recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the script (headless; produces images and console output):

```powershell
python run_assignment.py
```

4. Output images will be saved as `visual_*.png` and `betweenness_evolution.png` in the project folder.

If you prefer to open the notebook and run interactively, open `DSC212_Assignment_HarshSuthar_fixed.ipynb` in VS Code or Jupyter and run all cells.

Notes
- I repaired a corrupted notebook and provided a working script for headless execution to guarantee reproducible outputs.
- If you'd like, I can also create a short GitHub Actions workflow to run the script and attach generated artifacts automatically on push.