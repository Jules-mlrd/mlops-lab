
# Lab 1 — Code Versioning with Git

## Overview

**Code versioning** tracks and manages changes to your source code using a Version Control System (VCS), most commonly **Git**.
Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.
It is essential for **collaborative, reproducible, and auditable** workflows in MLOps and Data Science.


## Objectives

By the end of this lab, you will be able to:

* Use **Git fundamentals**: commits, branches, merges, tags
* Understand **staged vs unstaged** changes
* Explore code evolution with **diffs and logs**
* Write and run **unit tests** with `pytest`
* Apply **clean version control** with `.gitignore`
* Build a **reproducible preprocessing script**
* Follow a workflow aligned with **MLOps best practices**

---

## Prerequisites

Make sure the following are installed:

* Git
* Python (familiarity with functions, DataFrames, pytest)
* Resources:

  * [About Git](https://git-scm.com/about)
  * [Git Cheat Sheet](https://git-scm.com/cheat-sheet)
  * [Pandas Documentation](https://pandas.pydata.org/docs/reference/index.html)

---

## Part I — Preprocessing Script

### Step 1 — Navigate to the Notebook

```bash
cd notebook
```

### Step 2 — Complete the Notebook

Open:

```
eda.ipynb
```

Fill in the `"your code here"` placeholders.

### Step 3 — Check Git Status

```bash
git status
```

### Step 4 — Stage the Notebook

```bash
git add eda.ipynb
```

### Step 5 — Commit Changes

```bash
git commit -m "notebook: data preprocessing remove duplicates and strip whitespace"
```

---

### Step 6 — Modularize Notebook Code

Navigate to the preprocessing script directory:

```bash
cd lab1/src/lab1/data_preprocessing
```

### Step 7 — Complete the Preprocessing Script

Open:

```
preprocessing.py
```

Fill in `"your code here"` placeholders.

### Step 8 — Run the Script

```bash
python preprocessing.py --input_data_path ../../../../datastores/raw_csv_data/census.csv --output_data_filename clean_census.csv
```

Or using Poetry:

```bash
poetry run python eda.py --input_data_path ../../../datastores/raw_data/census.csv --output_data_filename clean_census.csv
```

Verify that a cleaned dataset is generated.

---

## Part II — Git Versioning

### Step 9 — Check Git Status

```bash
git status
```

### Step 10 — Stage Script

```bash
git add preprocessing.py
```

### Step 11 — Commit Script

```bash
git commit -m "data preprocessing: remove duplicates and strip whitespace in DataFrame"
```

### Step 12 — Check Status Again

```bash
git status
```

> Tip: Use clear commit messages: **`<scope>: <concise description>`**

---

## Part III — Explore Changes

### Step 13 — View Unstaged/Staged Changes

```bash
git diff
```

### Step 14 — Explore Commit History

```bash
git log --oneline
git log --oneline --stat
```

---

## Part IV — Push to Remote Repository

### Step 15 — Push Changes

```bash
git push origin master
```
This command sends your local commits on the master branch to the remote repository named origin.

Next Step:

Go to your remote repository on GitHub in a browser to verify that your changes have been successfully uploaded. You should see your latest commits and updated files

---

## Part V — Unit Tests

### Step 16 — Navigate to Tests Directory

```bash
cd lab1/tests
```

### Step 17 — Complete Test Scripts

Fill in `"your code here"` in:

* `test_preprocessing.py`
* `conftest.py`

### Step 18 — Run Tests

```bash
pytest -vv tests/unit_tests/
```

Or using Poetry:

```bash
poetry run pytest -vv unit_tests/
```

Fix failing tests until all pass.

---

## Part VI — Commit & Push Tests

### Step 19 — Stage and Commit Tests

```bash
git add unit_tests/conftest.py unit_tests/test_preprocessing.py
git commit -m "add pytest configuration and preprocessing unit tests"
```

### Step 20 — Review and Push

```bash
git diff
git log --oneline --stat
git log --oneline --graph --decorate --all
git push origin master
```

---

## Key Configuration Files

| File           | Purpose                                                   |
| -------------- | --------------------------------------------------------- |
| `.gitignore`   | Excludes unnecessary files (`__pycache__/`, `.env`, logs) |
| `~/.gitconfig` | Global Git configuration                                  |
| `.git/config`  | Local repository configuration                            |

---

## Learn More

Learn about **branches, tags, and merges** to collaborate and manage repositories like a professional **MLOps engineer**: [About Git](https://git-scm.com/about)

You can collaborate with different groups of people in different ways simultaneously within the same project
