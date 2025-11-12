"""
test_preprocessing.py
------------
Unit tests for data preprocessing functions: load_data, clean_data, and save_data.

This test suite ensures:
    - Data is correctly loaded from CSV
    - Cleaning operations (strip, dropna, deduplicate) are applied correctly
    - Cleaned data is properly saved to disk

Each test uses fixtures defined in `conftest.py` for reproducibility.
"""

import pandas as pd
from lab1.data_preprocessing.preprocessing import clean_data, load_data, save_data

# -------------------------------------------------------------------
#  Expected Columns (for validation)
# -------------------------------------------------------------------
expected_columns = [
    "age",
    "workclass",
    "fnlgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "salary",
]


# -------------------------------------------------------------------
#  Test: Load Data
# -------------------------------------------------------------------
def test_load_data(raw_census_data_path):
    """Ensure load_data() correctly loads CSV into a valid DataFrame."""

    # Load data from pytest fixture
    df = load_data(raw_census_data_path)

    assert isinstance(df, pd.DataFrame), "Loaded data is not a DataFrame"

    assert df.shape[0] > 0, "DataFrame is empty"

    assert df.shape[1] == len(
        expected_columns
    ), "DataFrame has unexpected number of columns"


# -------------------------------------------------------------------
#  Test: Clean Data
# -------------------------------------------------------------------
def test_clean_data(raw_census_data_df):
    """Ensure clean_data() removes duplicates, strips whitespace, and drops NaNs."""

    cleaned_df = clean_data(raw_census_data_df)

    assert all(
        col == col.strip() for col in cleaned_df.columns
    ), "Column names contain whitespace"
    assert cleaned_df.duplicated().sum() == 0, "Duplicates were not removed"
    assert cleaned_df.isna().sum().sum() == 0, "Missing values remain after cleaning"


# -------------------------------------------------------------------
#  Test: Save Data
# -------------------------------------------------------------------
def test_save_data(clean_census_data_df, clean_census_data_path):
    """Ensure save_data() writes cleaned data correctly to expected path."""

    output_filename = "test_clean_output.csv"
    output_path = save_data(clean_census_data_df, output_filename)

    assert output_path.exists(), "Output file was not created"

    saved_df = pd.read_csv(output_path)
    try:
        assert all(
            col == col.strip() for col in saved_df.columns
        ), "Saved column names contain whitespace"
        assert saved_df.duplicated().sum() == 0, "Saved dataset contains duplicates"
        assert saved_df.isna().sum().sum() == 0, "Saved dataset contains missing values"
    finally:
        output_path.unlink(missing_ok=True)
