"""
conftest.py
------------
Pytest configuration file for managing shared fixtures and global settings for tests.

This file centralizes reusable test utilities such as:
    - Common DataFrame fixtures for unit tests
    - Paths to test data files

Pytest automatically discovers fixtures defined here —
there’s no need to import them explicitly in test modules.
"""

import sys
from pathlib import Path

import pandas as pd
import pytest

# -------------------------------------------------------------------
#  Path configuration for importing project modules
# -------------------------------------------------------------------
PROJECT_ROOT: Path = Path(__file__).resolve().parents[3]
SRC_DIR: Path = PROJECT_ROOT / "lab1" / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

# -------------------------------------------------------------------
#  Global Constants and Configuration
# -------------------------------------------------------------------
DATASTORE_DIR: Path = PROJECT_ROOT / "datastores"

CENSUS_RAW_DATA_PATH: Path = DATASTORE_DIR / "raw_data" / "census.csv"
CLEAN_CENSUS_DATA_PATH: Path = DATASTORE_DIR / "clean_data" / "clean_census.csv"


# -------------------------------------------------------------------
#  Fixtures
# -------------------------------------------------------------------
@pytest.fixture(scope="session")
def raw_census_data_path() -> Path:
    """
    Provide the absolute path to the raw census dataset.

    Returns:
        Path: Absolute path to the CSV file in the raw data directory.

    Raises:
        pytest.UsageError: If the expected CSV file is missing.
    """
    if not CENSUS_RAW_DATA_PATH.exists():
        pytest.fail(f"[DataError] Raw CSV file not found at: {CENSUS_RAW_DATA_PATH}")
    return CENSUS_RAW_DATA_PATH


@pytest.fixture(scope="session")
def clean_census_data_path() -> Path:
    """
    Provide the absolute path to the cleaned census dataset CSV file.

    This fixture is scoped to the entire test session to ensure consistent
    access to a single shared data artifact across all tests.

    Returns:
        Path: Absolute path to the cleaned census data file.

    Raises:
        pytest.UsageError: If the file does not exist.
    """
    if not CLEAN_CENSUS_DATA_PATH.exists():
        pytest.fail(
            f"[DataError] Clean CSV file not found at: {CLEAN_CENSUS_DATA_PATH}"
        )
    return CLEAN_CENSUS_DATA_PATH


@pytest.fixture(scope="function")
def raw_census_data_df(raw_census_data_path) -> pd.DataFrame:
    """
    Load the census dataset into a pandas DataFrame for testing.

    This fixture provides a clean, in-memory DataFrame instance that can be safely
    modified by individual tests without affecting others.

    Args:
        raw_census_data_path (Path): Path to the raw census dataset.

    Returns:
        pd.DataFrame: The loaded census dataset.
    """
    try:
        df = pd.read_csv(raw_census_data_path)
        return df
    except Exception as e:
        pytest.fail(
            f"[DataLoadError] Failed to load CSV from {raw_census_data_path}: {e}"
        )


@pytest.fixture(scope="function")
def clean_census_data_df(clean_census_data_path) -> pd.DataFrame:
    """
    Load the cleaned census dataset into a pandas DataFrame for testing.

    This fixture provides a ready-to-use DataFrame
    representing the cleaned version of the dataset.

    Args:
        clean_census_data_path (Path): Path to the cleaned census dataset.

    Returns:
        pd.DataFrame: Cleaned census dataset.
    """
    try:
        return pd.read_csv(clean_census_data_path)
    except FileNotFoundError:
        pytest.fail(
            f"[DataLoadError] Clean CSV file not found at: {clean_census_data_path}"
        )
    except Exception as exc:
        pytest.fail(
            f"[DataLoadError] Failed to load cleaned CSV from {clean_census_data_path}: {exc}"
        )
