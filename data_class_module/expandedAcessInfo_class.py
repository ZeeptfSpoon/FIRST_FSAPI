class ExpandedAccessInfo:
    hasExpandedAccess: bool

    def __init__(self, expanded_access_info_as_dict):

        self.hasExpandedAccess = expanded_access_info_as_dict.get("hasExpandedAccess", True)