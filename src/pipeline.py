# Energy market data pipeline
from datetime import datetime, timedelta
import numpy as np
import pandas as pd


def generate_market_data():
    start_time = datetime(2026, 8, 20, 0, 0)
    timestamps = [start_time + timedelta(hours=i) for i in range(24)]

    np.random.seed(42)
    base_price = 60 + 20 * np.sin(np.linspace(0, 2 * np.pi, 24))
    prices = np.round(base_price + np.random.normal(0, 5, 24), 2)

    grid_load_mw = np.random.randint(15000, 35000, size=24)

    df = pd.DataFrame(
        {
            "timestamp": timestamps,
            "price_eur_mwh": prices,
            "grid_load_mw": grid_load_mw,
        }
    )

    df["rolling_avg_price"] = (
        df["price_eur_mwh"].rolling(window=3, min_periods=1).mean().round(2)
    )
    df["high_demand_flag"] = df["grid_load_mw"] > 28000

    df.to_csv("energy_market_summary.csv", index=False)
    return df


if __name__ == "__main__":
    generate_market_data()