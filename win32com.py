import pandas as pd
import win32com.client
from typing import List, Union
import datetime

def push_df_to_excel_worksheet(df: pd.DataFrame, excel_file_path: str, sheet_name: str) -> None:
    """
    Pushes a Pandas DataFrame to a specific Excel worksheet and refreshes connections.

    Args:
        df (pd.DataFrame): The DataFrame to be pushed to Excel.
        excel_file_path (str): The file path of the Excel workbook where the DataFrame will be pushed.
        sheet_name (str): The name of the Excel sheet where the DataFrame will be pushed.

    Returns:
        None

    Example:
        push_df_to_excel_worksheet(my_dataframe, 'C:\\path\\to\\my_excel_file.xlsx', 'Sheet1')
    """
    try:
        # Opening Excel software using the win32com
        excel_app = win32com.client.Dispatch("Excel.Application")

        # Optional line to show the Excel software
        excel_app.Visible = 1

        # Opening the specified workbook
        logger.info(f"Opening Excel workbook: {excel_file_path}")
        workbook = excel_app.Workbooks.Open(excel_file_path)

        # Check if the sheet exists, create it if not
        sheet_exists = False
        for sheet in workbook.Sheets:
            if sheet.Name == sheet_name:
                sheet_exists = True
                break
        
        if not sheet_exists:
            workbook.Sheets.Add().Name = sheet_name

        # Get the target worksheet
        worksheet = workbook.Sheets(sheet_name)
        if False:
            # Clear existing data in the worksheet
            logger.info(f"Clearing existing data in worksheet: {sheet_name}")
            worksheet.Cells.Clear()

            # Write the header of the DataFrame to the worksheet
            logger.info(f"Writing header to worksheet: {sheet_name}")
            for col_idx, header_value in enumerate(df.columns):
                worksheet.Cells(1, col_idx + 1).Value = header_value

            # Write the DataFrame data to the worksheet
            logger.info(f"Writing DataFrame to worksheet: {sheet_name}")
            for row_idx, row in enumerate(df.values):
                for col_idx, value in enumerate(row):
                    worksheet.Cells(row_idx + 2, col_idx + 1).Value = value

        # Refreshing all the sheets
        logger.info("Refreshing all sheets in the workbook")
        # workbook.Save()
        workbook.RefreshAll()
        # excel_app.CalculateUntilAsyncQueriesDone() 
        
        # Wait for the last refresh to be within the past minute
        last_refresh_sheet = workbook.Sheets("last_refresh")
        # TODO user a macro to execute refresh etc. 
        while True:
            last_refresh_time_cell = last_refresh_sheet.Cells(2, 1)
            last_refresh_time = last_refresh_time_cell.Value

            if last_refresh_time is not None:
                last_refresh_time = datetime.datetime.fromisoformat(last_refresh_time)

            time_difference = (datetime.datetime.now() - last_refresh_time).total_seconds()

            logger.info(f"Last refresh time: {last_refresh_time}, Time difference: {time_difference} seconds")

            if last_refresh_time is not None and time_difference <= 20:
                break

            time.sleep(10)  # Wait for 10 seconds before checking again

        # Saving the Workbook
        time.sleep(20)  # Wait for 10 seconds before saving
        logger.info(f"Saving workbook: {excel_file_path}")
        workbook.Save()

        # Closing the Excel File
        logger.info("Closing Excel file")
        excel_app.Quit()
        
        logger.info("Data pushed to Excel successfully.")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
