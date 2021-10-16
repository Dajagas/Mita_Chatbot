import gspread

def GsheetDataStore(user_name,user_age,user_email,user_run_hist,confirm_exercise,exercise,user_sleep,stress):
    gc = gspread.service_account(filename="creds.json")
    sh = gc.open_by_key('1_OT4IdZV2A9ZxhKx9gQj6dfbR3ocpXpuUraYcgUDu4M')
    worksheet = sh.sheet1
    data_in = [user_name,user_age,user_email,user_run_hist,confirm_exercise,exercise,user_sleep,stress]
    result = worksheet.append_row(data_in)

