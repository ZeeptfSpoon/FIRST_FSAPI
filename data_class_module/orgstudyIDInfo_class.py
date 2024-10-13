class OrgstudyIdInfo:
    id: object

    def __init__(self, orgstudy_as_dict):
        self.id = orgstudy_as_dict.get("id")