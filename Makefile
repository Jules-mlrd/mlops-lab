
# ======================================================================
# Makefile for MLOps Training Project (Lab 1)
# ======================================================================

# ---------------------------- VARIABLES --------------------------------
INPUT_PATH        ?= datastores/raw_csv_data/census.csv
OUTPUT_FILENAME   ?= clean_census.csv
CONDA_ENV         ?= mlops_env
SCRIPT            ?= lab1/src/lab1/data_preprocessing/preprocessing.py


# --------------------------- DEFAULT TARGETS ------------------------------
.PHONY: env-create env-update install-dependencies update-dependencies \
        export-dependencies install-hooks update-hooks run-hooks \
        clean-data test all

# ======================================================================
# ENVIRONMENT MANAGEMENT
# ======================================================================

# Create conda environment
env-create:
	@echo "=> Creating conda environment from conda.yaml (env: $(CONDA_ENV))"
	conda env create -f conda.yaml
	@echo "=> Conda environment '$(CONDA_ENV)' created successfully."

# Update conda environment
env-update:
	@echo "=> Updating conda environment from conda.yaml (env: $(CONDA_ENV))"
	conda env update -f conda.yaml
	@echo "=> Conda environment '$(CONDA_ENV)' updated successfully."

# ======================================================================
# DEPENDENCY MANAGEMENT
# ======================================================================

# Install project dependencies (Poetry)
install-dependencies:
	@echo "=> Installing project dependencies..."
	## your code here
	@echo "=> Dependencies installed successfully."

# Update all dependencies (Poetry)
update-dependencies:
	@echo "=> Updating project dependencies..."
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	@echo "=> Dependencies updated successfully."

# Export dependencies to requirements.txt
export-dependencies:
	@echo "=> Exporting dependencies to requirements.txt (without hashes)..."
	__________________________  # your code here
	@echo "=> Dependencies exported successfully."

# ======================================================================
# CODE QUALITY & GIT HOOKS
# ======================================================================

# Install pre-commit hooks
install-hooks:
	@echo "=> Installing pre-commit Git hooks..."
	## your code here
	@echo "=> Pre-commit hooks installed successfully."

# Update pre-commit hooks
update-hooks:
	@echo "=> Updating pre-commit hooks..."
	## your code here
	@echo "=> Pre-commit hooks updated successfully."

# Run all pre-commit hooks
run-hooks:
	@echo "=> Running all pre-commit hooks on all files..."
	## your code here
	@echo "=> Pre-commit hooks executed successfully."

# ======================================================================
# DATA PREPROCESSING & TESTING
# ======================================================================

# Run data preprocessing script
clean-data:
	@echo "=> Running data preprocessing..."
	## your code here
	@echo "=> Data preprocessing completed. Clean data saved to $(OUTPUT_FILENAME)."

# Run unit tests
test:
	@echo "=> Running unit tests..."
	## your code here
	@echo "=> Unit tests completed successfully."

# ======================================================================
# ALL-IN-ONE WORKFLOW
# ======================================================================

all: install-dependencies install-hooks update-dependencies update-hooks run-hooks clean-data test
	@echo "All tasks completed successfully."
