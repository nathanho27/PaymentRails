"""
We need this to export the final analytics tables for Tableau consumption.

No business logic should live here.
"""

import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# The export_market_metrics function connects to the MySQL database queries the market_metrics view, and writes the results to a CSV file that can be consumed by Tableau or Excel.
def export_market_metrics(db_uri, output_path="data/analytics/market_metrics.csv"):
    engine = create_engine(db_uri)
    query = "SELECT * FROM market_metrics"
    df = pd.read_sql(query, engine)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Exported market_metrics to {output_path}")


# The main function defines the database connection string and calls the export_market_metrics function to perform the export.
def main():
    db_uri = "mysql+mysqlconnector://root:mypassword@localhost:3306/paymentrails"
    export_market_metrics(db_uri)

# The script can be run directly to refresh the analytics export.
if __name__ == "__main__":
    main()