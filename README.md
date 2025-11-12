# MLOps Foundations – Day 1: Local or On-Prem MLOps

## Lab Overview

In this lab, you will learn the core foundations of MLOps, including:

* **Code versioning** using Git
* **Data versioning** with DVC
* **Pipeline modularity**
* **Best practices** in Python: logging, type hints, docstrings, CLI, and code quality with pre-commit hooks
* **Continuous Integration (CI)** automation using GitHub Actions
* **Environment management** with Conda and Poetry
* **Unit testing** using Pytest

By the end of the lab, you will be able to set up a full local MLOps pipeline and automate testing and code quality checks.

---

## Prerequisites

Before starting, ensure the following are installed:

* **Git** – [Git official site](https://git-scm.com/about)
* **Python 3.11 or higher**
* **Miniconda / Anaconda** – [Installation guide](https://www.anaconda.com/docs/getting-started/miniconda/main)

## Step 1: Fork the Repository

Forking allows you to have your own GitHub copy to push changes and experiment safely.

1. Go to the GitHub repository: `https://github.com/TouyeAchille/mlops-lab`
2. Click **Fork** in the top-right corner.
3. Clone your forked repository locally using the command in Step 2.

---

## Step 2: Clone the Repository

```bash
git clone https://github.com/TouyeAchille/mlops-lab.git
```

---

## Step 3: Change Directory

```bash
cd mlops-lab
```

---

## Step 3: Check Repository Status

```bash
git status
```

This ensures your local repository is correctly initialized and tracks your changes.

---


## Lab 1 Structure

Follow instructions in `mlops-lab1-instruction` and complete the lab in order:

1. **Environment Management & Packages**
2. **Code Versioning**
3. **Code Quality**
4. **Data Versioning**
5. **CI Automation**

**Recommended workflow**:
```
environment-management-package -> code-versioning -> code-quality -> data-versioning -> automation-ci
```
---
Directory structure for Lab 1

```
├── conda.yaml               # Conda environment definition with packages and Python version
├── datastores               # Folder to store datasets (raw and processed)
│   ├── raw_csv_data         # Raw CSV data folder
│   │   └── census.csv       # Example raw CSV dataset
│   └── raw_text_data        # Raw text data folder
│       └── journal.txt      # Example raw text dataset
├── lab1                     # Lab 1 project folder
│   ├── src                  # Source code for Lab 1
│   │   └── lab1
│   │       ├── **init**.py  # Python package initializer
│   │       └── data_preprocessing
│   │           └── preprocessing.py  # Data preprocessing functions
│   └── tests                 # Unit tests for Lab 1
│       ├── **init**.py       # Python package initializer for tests
│       └── unit_tests
│           ├── **init**.py  # Python package initializer for unit tests
│           ├── conftest.py  # Pytest configuration and fixtures
│           └── test_preprocessing.py  # Unit tests for preprocessing.py
├── LICENSE                  # Project license file
├── Makefile                 # Automation tasks for environment setup, testing, etc.
├── mlops-lab1-instruction   # Instructions and guidance for Lab 1
│   ├── automatisation-ci
│   │   └── README.md        # CI/CD lab instructions
│   ├── code-quality
│   │   └── README.md        # Code quality lab instructions
│   ├── code-versioning
│   │   └── README.md        # Git/code versioning instructions
│   ├── data-versioning
│   │   └── README.md        # DVC/data versioning instructions
│   └── environement-management-package
│       └── README.md        # Conda/Poetry environment setup instructions
├── mlops-lab2-instruction   # Instructions for Lab 2
│   ├── docker
│   │   └── README.md        # Docker lab instructions
│   └── fastapi
│       └── README.md        # FastAPI lab instructions
├── notebook                 # Jupyter notebooks
│   └── eda.ipynb            # Exploratory Data Analysis notebook
├── poetry.lock              # Poetry lock file for reproducible dependencies
├── pyproject.toml           # Poetry project configuration
└── README.md                # Main README for the repository
```
---

## Git Remote Repositories

A **remote repository** is a hosted version of your Git project, enabling collaboration, backup, and CI/CD.

### Common Types

1. **Open-Source / Public Platforms**

   * **GitHub** – Most widely used; supports public/private repos, pull requests, issues, and GitHub Actions.
   * **GitLab** – Supports similar features and offers self-hosted options with strong CI/CD pipelines.

2. **Cloud / Enterprise Repositories**

   * **Azure Repos** – Part of Azure DevOps; integrates with pipelines and work item tracking.
   * **AWS CodeCommit** – Managed Git repos on AWS, fully private.
   * **Google Cloud Source Repositories** – Integrated with GCP services for CI/CD.

---

### Why GitHub for This Lab

We use **GitHub** because:

* Free and easy to set up for students and small teams.
* Integrates seamlessly with CI/CD pipelines via GitHub Actions.
* Supports collaborative development with pull requests and code reviews.
* Public visibility allows sharing and contributing to open-source projects.
