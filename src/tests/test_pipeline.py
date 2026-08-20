import os
import pandas as pd
import pytest
from src.pipeline import generate_market_data


def test_pipeline_execution():
    """Runs the pipeline and verifies the output CSV exists."""
    generate_market_data()
    assert os.path.exists("energy_market_summary.csv")


def test_pipeline_structure():
    """Verifies the CSV has exactly 24 hours and all required columns."""
    df = pd.read_csv("energy_market_summary.csv")

    assert len(df) == 24
    expected_columns = [
        "timestamp",
        "price_eur_mwh",
        "grid_load_mw",
        "rolling_avg_price",
        "high_demand_flag",
    ]
    assert list(df.columns) == expected_columns


def test_business_logic():
    """Verifies the high_demand_flag correctly evaluates grid load."""
    df = pd.read_csv("energy_market_summary.csv")

    for _, row in df.iterrows():
        if row["grid_load_mw"] > 28000:
            assert row["high_demand_flag"] is True
        else:
            assert row["high_demand_flag"] is False
