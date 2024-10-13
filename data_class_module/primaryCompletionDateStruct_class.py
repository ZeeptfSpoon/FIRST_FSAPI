class PrimaryCompletionDateStruct:
    date_prim_comp: object
    type_prim_comp: object

    def __init__(self, primary_comp_letion_as_dict):
        self.date_prim_comp = primary_comp_letion_as_dict.get("date")
        self.type_prim_comp = primary_comp_letion_as_dict.get("type")