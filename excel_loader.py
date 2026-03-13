import pandas as pd
from config import EXCEL_PATH


def load_excel_data():

    # Force reload the Excel file every time
    df = pd.read_excel(EXCEL_PATH, sheet_name="DashboardData")

    df.columns = df.columns.str.strip()

    return df