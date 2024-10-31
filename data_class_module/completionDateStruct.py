


class CompletionDateStruct:
    comp_date_date: object
    comp_date_type: object


    def __init__(self, completionDateStruct_as_dict ):
        self.comp_date_date = completionDateStruct_as_dict.get("date")
        self.comp_date_type = completionDateStruct_as_dict.get("type")
