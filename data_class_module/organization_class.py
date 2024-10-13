class Organization:
    fullName: object
    org_class: object

    def __init__(self, org_as_dict):
        self.fullName = org_as_dict.get("fullName")
        self.org_class = org_as_dict.get("class")