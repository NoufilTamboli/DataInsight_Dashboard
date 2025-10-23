import pandas as pd

def test_csv_load():
    df = pd.read_csv("data/sample_data.csv")
    expected_columns = ["Date", "Region", "Sales", "Profit", "Quantity"]
    assert all(col in df.columns for col in expected_columns)
    assert len(df) > 0
