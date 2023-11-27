gc = gspread.service_account(filename="credentials.json")
sh = gc.open_by_key('<your_key>')
ws = sh.sheet1
