# Lab 1 - Data Versioning

## Overview

This practical lab introduces the **core foundations of MLOps**: data versioning using **DVC (Data Version Control)**.

**Data Version Control (DVC)** is a powerful tool that allows you to:

- Track and version **data (images, audio, text files, etc..) and models** just like code in Git
- organize your ML modeling process into a reproducible workflow.
- Store datasets **locally or remotely** (cloud, shared drives, etc.)
- Easily **switch between different dataset versions**

**Common use cases:**
dataset snapshots, restoring previous versions, experiment reproducibility, and tracking evolving metrics.

Learn more: [Versioning Data and Models with DVC](https://dvc.org/doc/use-cases/versioning-data-and-models)

**Ressources:**

- [About Git](https://git-scm.com/about)
- [About DVC](https://dvc.org/doc/starthttps://dvc.org/doc/start)

---

## Getting Started

### Step 1 – Change to the Project Directory

```bash
cd mlops-lab
```

---

## Step 1 – Initialize DVC

```bash
dvc init
git commit -m "Initialize DVC"
```

### Configure Auto-Staging

Automatically stage DVC-tracked files for Git commits:

```bash
dvc config core.autostage true
```

---

## Step 2 – Track a Dataset with DVC

1. Track a data file:

```bash
dvc add datastores/raw_text_data/journal.txt
git commit -m "Track original data datastores/raw_text_data/journal.txt"
```

2. Tag this version for reference:

```bash
git tag v0.0 -m "Track original journal.txt"
```

---

## Step 3 – Modify the Data

- Open the file:
  `datastores/raw_text_data/journal.txt`
- Add or remove a few lines
- Save the file

---

## Step 4 – Check Data Status

```bash
dvc status
```

This command shows whether any tracked files have been modified.

---

## Step 5 – Version the Change

```bash
dvc add datastores/raw_text_data/journal.txt
git commit -m "Track change of file datastores/raw_data/journal.txt"
git tag -a v0.1 -m "Track change in journal.txt"
```

---

## Step 6 – Navigate Between Data Versions

Return to the **initial version**:

```bash
git checkout v0.0
dvc checkout
```

Check that the file `datastores/raw_text_data/journal.txt` matches the original content.

Return to the **latest version**:

```bash
git checkout v0.1
dvc checkout
```

---

## Step 7 – Add a Local Remote and Share Data

1. Create a local storage directory:

```bash
mkdir ./dvc_storage
```

2. Add a remote storage location:

```bash
dvc remote add -d localremote ./dvc_storage
git add .dvc/config
git commit -m "Add remote storage"
```

3. Push data to the remote storage:

```bash
dvc push
```

4. Remove the local file to test restoration:

```bash
rm -rf datastores/raw_data/journal.txt
```

5. Retrieve the data from remote:

```bash
dvc pull
```

Check that the file `journal.txt` has been restored correctly.

---

## III – Key Concepts

| Concept              | Command(s)                            | Description                                              |
| -------------------- | ------------------------------------- | -------------------------------------------------------- |
| Track data version   | `dvc add`                             | DVC tracks large files without bloating Git repositories |
| Record reference     | `git commit`                          | Git commits the DVC metadata for versioning              |
| Snapshot tagging     | `git tag`                             | Marks a specific data version for future reference       |
| Switch data versions | `git checkout <tag>` + `dvc checkout` | Restore a previous dataset version                       |
| Remote sharing       | `dvc remote add` + `dvc push`         | Share datasets with your team via local or cloud storage |
