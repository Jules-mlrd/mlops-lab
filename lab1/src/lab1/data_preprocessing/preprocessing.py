"""
data_preprocessing.py

A clean, modular data preprocessing script for MLOps pipelines.

This script:
- Loads raw data from CSV
- Cleans columns (trims whitespace, removes duplicates, drops NaNs)
- Saves the cleaned dataset to a standardized datastore path

Usage Example:
    python data_preprocessing.py \
        --input_data_path data/raw/raw_dataset.csv \
        --output_data_path clean_dataset.csv
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Union

import pandas as pd

# -------------------------------------------------------------------
#  Global Configuration
# -------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[4]
DATASTORE_DIR = PROJECT_ROOT / "datastores"

OUTPUT_DIR = DATASTORE_DIR / "clean_data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

LOG_DIR = DATASTORE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------------
#  Logging Configuration
# -------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(f"{LOG_DIR}/data_preprocessing.log", mode="a"),
    ],
)
logger = logging.getLogger("data_preprocessing")

logger.info(f"PROJECT_ROOT: {PROJECT_ROOT}")


# -------------------------------------------------------------------
#  Functions
# -------------------------------------------------------------------
def load_data(input_data_path: Union[str, Path]) -> pd.DataFrame:
    """
    Loads a CSV file into a Pandas DataFrame.

    Args:
        input_data_path (Union[str, Path]): Path to the input CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    logger.info("Loading raw dataset...")
    try:
        input_path = Path(input_data_path)
        logger.info(f"Loading raw data from: {input_path}")
        df = pd.read_csv(input_path)
        logger.info(f"Successfully loaded dataset with shape {df.shape}")
        return df

    except FileNotFoundError:
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    except Exception as e:
        logger.error(f"Error loading data: {e}")
        sys.exit(1)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the provided dataset by stripping column names,
    removing duplicates, and dropping missing values.

    Args:
        df (pd.DataFrame): The raw dataset.

    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    logger.info("Cleaning dataset...")
    cleaned_df = df.copy()
    cleaned_df.columns = cleaned_df.columns.str.strip()
    cleaned_df = cleaned_df.drop_duplicates()
    cleaned_df = cleaned_df.dropna()
    logger.info(f"Cleaned dataset shape: {cleaned_df.shape}")
    return cleaned_df


def save_data(df: pd.DataFrame, output_data_filename: str) -> Path:
    """
    Saves the cleaned DataFrame as a CSV to the standardized data directory.

    Args:
        df (pd.DataFrame): Cleaned dataset to save.
        output_data_filename (str): Name of the output CSV file.

    Returns:
        Path: The path where the cleaned file was saved.
    """
    output_path = OUTPUT_DIR / output_data_filename
    df.to_csv(output_path, index=False)
    logger.info(f"Saved cleaned dataset to: {output_path}")
    return output_path


# -------------------------------------------------------------------
#  CLI Interface
# -------------------------------------------------------------------
def parse_arguments() -> argparse.Namespace:
    """
    Parses CLI arguments for the preprocessing step.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Data Preprocessing - Clean raw dataset for MLOps pipeline"
    )

    parser.add_argument(
        "--input_data_path",
        type=str,
        required=True,
        help=(
            "Path to the raw input CSV file (e.g., ../datastores/raw_data/data.csv)."
        ),
    )

    parser.add_argument(
        "--output_data_filename",
        type=str,
        required=True,
        default="clean_census.csv",
        help=("Output filename (will be stored under ../datastores/clean_data/)"),
    )

    return parser.parse_args()


# -------------------------------------------------------------------
#  Main Entry Point
# -------------------------------------------------------------------
def main() -> None:
    """
    Main function for CLI execution.
    Loads, cleans, and saves data in one reproducible pipeline step.
    """
    args = parse_arguments()

    raw_df = load_data(args.input_data_path)
    cleaned_df = clean_data(raw_df)
    save_data(cleaned_df, args.output_data_filename)


if __name__ == "__main__":
    main()
