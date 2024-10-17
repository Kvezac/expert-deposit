class InputDateError(Exception):
    detail = "Date is not correct, valid date dd.mm.yyyy"
    status_code = 400
