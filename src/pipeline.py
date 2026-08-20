from datetime import datetime, timedelta
import numpy as np
import pandas as pd


def generate_energy_data():
    # 1. Generate 24 hours of simulated electricity market data
    start_time = datetime(2026, 8, 20, 0, 0)
    timestamps = [start_time + timedelta(hours=i) for i in range(24)]

    # Simulated prices (€/MWh) and grid load (MW)
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

    # 2. Add analytics: 3-hour rolling average & peak flag
    df["rolling_avg_price"] = (
        df["price_eur_mwh"].rolling(window=3, min_periods=1).mean().round(2)
    )
    df["high_demand_flag"] = df["grid_load_mw"] > 28000

    return df


if __name__ == "__main__":
    df = generate_energy_data()
    df.to_csv("energy_market_summary.csv", index=False)
    print("Energy market data pipeline executed successfully.")
    print(df.head())
