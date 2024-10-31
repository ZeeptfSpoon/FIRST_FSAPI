class PrimaryCompletionDateStruct:
    date_prim_comp: object
    type_prim_comp: object

    def __init__(self, primary_completion_as_dict):
        if primary_completion_as_dict is not None:
            self.date_prim_comp = primary_completion_as_dict.get("date")
            self.type_prim_comp = primary_completion_as_dict.get("type")

    def __str__(self):
        retval = f"{self.date_prim_comp} {self.type_prim_comp}"
        return retval
         #print(self.date_prim_comp)

    def print_value(self):
        #retval = f"{self.date_prim_comp} {self.type_prim_comp}"
        #print(retval)
        print(self.date_prim_comp)
