class PrimaryCompletionDateStruct:
    date_prim_comp: object
    type_prim_comp: object

    def __init__(self, primary_completion_as_dict):
        self.date_prim_comp = primary_completion_as_dict.get("date")
        self.type_prim_comp = primary_completion_as_dict.get("type")