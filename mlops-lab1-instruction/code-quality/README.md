# Code Quality — Writing Clean and Maintainable ML Code

##  Overview

In MLOps, maintaining **high code quality** is essential to ensure that your machine learning project is:

* **Readable** → easy for others (and future you) to understand.
* **Maintainable** → easy to modify or extend without breaking existing code.
* **Consistent** → follows a unified style across the team and project.

In this section, you’ll learn how to **format**, **lint**, and **validate** your code using powerful tools like:

* **Black** — automatic code formatter
* **isort** — organizes your imports cleanly
* **Flake8** — checks code style and detects common errors
* **Pre-commit** — automates these checks each time you commit code

Learn more: [https://pre-commit.com](https://pre-commit.com)

---

## Getting Started

### Step 1 — Navigate to the Data Preprocessing Directory

```bash
cd lab1/src/lab1/data_preprocessing
```

Here, you’ll find your main preprocessing script — this is where you’ll practice code quality checks.

---

## Run Code Quality Checks Manually

Let’s start by running each tool **manually** to understand what it does.

---

### 1. Format Code with **Black**

```bash
black preprocessing.py
```

**What it does:**
Black reformats your Python code automatically to follow PEP8 standards (consistent indentation, spacing, line length, etc.).
It enforces a clean, uniform style — no debates about formatting!

> Tip: You don’t need to worry about style decisions — Black decides for you.

---

### 2. Sort Imports with **isort**

```bash
isort preprocessing.py
```

**What it does:**
isort organizes your `import` statements automatically:

* Groups standard library, third-party, and local imports.
* Removes duplicates.
* Keeps everything alphabetically sorted.

> Tip: Keeping imports clean avoids confusion when multiple developers work on the same project.

---

###  3. Lint Code with **Flake8**

```bash
flake8 preprocessing.py
```

**What it does:**
Flake8 analyzes your Python file and reports:

* Syntax errors
* Unused variables or imports
* Lines that are too long
* Poor naming conventions

> Tip: Read the warnings carefully — they often reveal bugs or bad practices early.

---

##  Run Code Quality Checks Automatically with **Pre-commit**

Manual checks are useful, but MLOps encourages **automation**.
That’s where **Pre-commit** comes in: it ensures your code is clean **before every commit**.

---

### Step 1 — Move to the Project Root

```bash
cd mlops-lab
```

---

### Step 2 — Configure `.pre-commit-config.yaml`

Check that your configuration file defines the necessary hooks. Ensure your `.pre-commit-config.yaml` file includes all necessary hooks (e.g., black, isort, flake8, end-of-file-fixer, etc.).

`Edit or complete it where indicated by ## your code here`

---

### Step 3 — Run Pre-commit Hooks Manually

You can trigger all code quality checks at once:

```bash
pre-commit run --all-files
```

or with Poetry:

```bash
poetry run pre-commit run --all-files
```

> If any hook fails, Pre-commit will show what needs fixing.
> Simply correct the issues, re-run the command, and ensure all checks pass.

---

## Automate Code Quality on Every Commit

### Step 4 — Install the Git Hook Scripts

Install pre-commit so that it runs automatically whenever you make a Git commit:

```bash
pre-commit install
```

or (if using Poetry):

```bash
poetry run pre-commit install
```

> After this step, every time you run `git commit`, Pre-commit will check your code first!

---

### Step 5 — Update Pre-commit Hooks Regularly

To ensure you’re using the latest versions of each hook:

```bash
pre-commit autoupdate
```

or with Poetry:

```bash
poetry run pre-commit autoupdate
```

---

### Pro Tip — Validate Everything Once

When you add new hooks or update existing ones, always run them on all files once to ensure consistency:

```bash
pre-commit run --all-files
```

or

```bash
poetry run pre-commit run --all-files
```
