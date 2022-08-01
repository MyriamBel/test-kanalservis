import gspread


class Gsheet:
    service_account = gspread.service_account()
    doc = None

    def __init__(self, doc_name):
        self.doc = self.service_account.open(doc_name)

    def __str__(self):
        return self.doc

    def open_sheet_name_or_first(self, sheet_name=None):
        if sheet_name is None:
            workbook = self.doc.sheet1
        else:
            workbook = self.doc.worksheet(str(sheet_name))
        return workbook
