import pandas as pd
import win32com.client
from bs4.element import Tag
from typing import List, Union
from bs4 import BeautifulSoup
import pandas as pd
import logging
import time
import datetime

def get_df_from_html_table(table: Tag) -> pd.DataFrame:
    """
    Extracts data from an HTML table and converts it into a Pandas DataFrame.

    Args:
        table (bs4.element.Tag): The BeautifulSoup Tag object representing the HTML table.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the HTML table.

    Example:
        html_table = soup.find('table')  # Assume 'soup' is a BeautifulSoup object
        data_df = get_data_from_html_table(html_table)
    """
    table_data = []

    if isinstance(table, Tag) and table.name == 'table':
        for row in table.find_all('tr'):
            row_data = []
            for cell in row.find_all(['td', 'th']):
                row_data.append(cell.get_text(strip=True))  # Add cell data to the row
            table_data.append(row_data)  # Add the row to the table data

        if len(table_data) > 0:
            header = table_data[0]
            data = table_data[1:]
            data_df = pd.DataFrame(data, columns=header)
            return data_df

    return pd.DataFrame()  # Return an empty DataFrame if no valid table is found
