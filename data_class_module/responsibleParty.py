class ResponsibleParty:
    resp_party_type: object


    def __init__(self, responsibleParty_as_dict):
        if responsibleParty_as_dict is not None:
            self.resp_party_type = responsibleParty_as_dict.get("type")

    def __str__(self):
            retval = f"{self.resp_party_type} "
            return retval