# DSA8401 Credit Lab

This repository contains the DSA8401 applied machine learning lab scaffold.

## Structure

- `src/` - Python source code and reusable modules
- `data/` - datasets (ignored by Git)
- `notebooks/` - Jupyter notebooks for exploratory work
- `.venv/` - isolated Python environment (ignored by Git)
- `requirements.txt` - package requirements for this lab

## Setup

1. Create and activate the virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   ```
2. Install packages:
   ```powershell
   pip install -r requirements.txt
   ```
3. Register the kernel:
   ```powershell
   python -m ipykernel install --user --name dsa8401 --display-name "Python (dsa8401)"
   ```
4. Open VS Code:
   ```powershell
   code .
   ```
5. Select the interpreter at `.\.venv\Scripts\python.exe` and use the `Python (dsa8401)` kernel in notebooks.
