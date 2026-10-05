# Topic 3: Installation and Setup

This guide installs Python and VS Code on Windows, checks the version, and
creates your first `.py` file.

---

## Step 1: Install Python on Windows

1. Go to <https://www.python.org/downloads/windows/>.
2. Download the **Latest Python 3 Release** installer (`.exe`).
3. Run the installer.
4. **Important:** tick the box at the bottom that says
   *Add python.exe to PATH* before clicking **Install Now**.
5. After installation, close and reopen PowerShell or Command Prompt.

Why the PATH box matters: it lets you type `python` from any folder
instead of typing the full path to `python.exe`.

---

## Step 2: Check the Python version

Open PowerShell and run:

```powershell
python --version
```

Expected output:

```text
Python 3.14.0
```

Useful variations:

| Command | What it does |
| --- | --- |
| `python --version` | Prints the version |
| `py --version` | Windows launcher, also works |
| `python -V` | Short form of `--version` |
| `where python` | Shows the path of the executable |

If you see *not recognized as an internal or external command*, Python is
not on your PATH. Reinstall it and tick the PATH box, then restart the
terminal.

---

## Step 3: Install VS Code

1. Download VS Code from <https://code.visualstudio.com/>.
2. Install it with the default options.
3. Launch VS Code.

---

## Step 4: Install the Python extension

1. Click the Extensions icon in the left sidebar (or press
   <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>X</kbd>).
2. Search for `Python` and install the extension published by **Microsoft**.

This extension adds syntax highlighting, IntelliSense, debugging and the
Run button.

---

## Step 5: Create a .py file

1. **File > New File...**
2. Type your program, for example:

   ```python
   print("Hello, World!")
   ```

3. Save the file with a `.py` extension, such as `hello.py`.

Tip: if VS Code does not treat the file as Python, click the language mode
in the bottom-right corner and choose **Python**.

---

## Step 6: Run the file

From VS Code: press the **Run Python File** play button in the top-right
corner, or press <kbd>Ctrl</kbd>+<kbd>F5</kbd>.

From a terminal:

```powershell
python hello.py
```

Output:

```text
Hello, World!
```

---

## Step 7: (Recommended) Select the interpreter

1. Press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>.
2. Run **Python: Select Interpreter**.
3. Choose the Python installation you created.

VS Code uses this interpreter to run and debug your code.

---

## Virtual environments (quick note)

Every project should have its own environment so packages stay separate.
Run these two commands inside your project folder:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Activate it again each time you open a new terminal for that project, and
deactivate with:

```powershell
deactivate
```

---

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `python` not found | Reinstall and tick *Add python.exe to PATH* |
| PowerShell blocks activation | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| Wrong version used | `py -3.14 hello.py` or set the interpreter in VS Code |
| Extension not loading | Restart VS Code, then re-select the interpreter |

---

## Checklist

- [ ] Python installed
- [ ] *Add python.exe to PATH* was ticked
- [ ] `python --version` prints `Python 3.x.x`
- [ ] VS Code installed
- [ ] Microsoft Python extension installed
- [ ] `hello.py` created and ran successfully