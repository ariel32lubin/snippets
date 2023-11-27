CREDENTIALS_FILE = r'credentials/google_credentials.json'
gc = gspread.service_account(filename=CREDENTIALS_FILE)
spreadsheet = gc.open_by_key('1L8bLAtXd4Fjym2tGqsDLvxtDmSRe-8NuIUyg5WMCJqU')
print(spreadsheet.worksheets())
