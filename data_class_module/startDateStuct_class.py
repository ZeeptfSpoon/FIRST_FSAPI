class StartDateStruct:
    date_start_date: object

    def __init__(self, start_date_as_dict):
        self.date_start_date = start_date_as_dict.get("date")