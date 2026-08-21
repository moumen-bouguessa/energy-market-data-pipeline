# European Energy Market Data Pipeline

![Build Status](https://github.com/moumen-bouguessa/energy-market-data-pipeline/actions/workflows/test.yml/badge.svg?branch=main)

Automated data processing pipeline built in Python to simulate, clean, and analyze 24-hour European electricity market data. Includes rolling price averages, grid load alert flags, and automated continuous integration testing via GitHub Actions.

## Features
* **Automated Data Processing:** Generates structured hourly energy prices and grid demand metrics.
* **Business Logic Analytics:** Calculates 3-hour rolling price averages and flags high-demand grid load thresholds (>28,000 MW).
* **Automated Testing:** Unit test suite built with `pytest` covering data schema, row counts, and calculation integrity.
* **CI/CD Pipeline:** Automated GitHub Actions workflow running tests on every code push.

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute Pipeline:**
   ```bash
   python src/pipeline.py
   ```

3. **Run Test Suite:**
   ```bash
   python -m pytest
   ```
