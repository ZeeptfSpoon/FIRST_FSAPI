import json


class Main:
    """
    json to obj with studies as list and nextPageToken as string

    """
    studies: list
    nextPageToken: str

    def __init__(self, file_name=None):
        file = None
        if file_name:
            try:
                file = json.load(open(file_name))
            except Exception as e:
                print(e)
            if file:
                if file.get('nextPageToken'):
                    self.nextPageToken = file.get('nextPageToken')
                if file.get('studies'):
                    self.studies = file.get('studies')


class Studies:
    protocolSection: dict
    derivedSection: dict
    hasResults: bool

    def __init__(self, studies_json_as_list: list):
        """
        "protocolSection" dict
        "derivedSection"dict
        "hasResults" bool
        :param studies_json_as_list:
        """
        for element in studies_json_as_list:
            if element.get("protocolSection"):
                self.protocolSection = element.get("protocolSection")
            if element.get("derivedSection"):
                self.protocolSection = element.get("derivedSection")
            if element.get("hasResults"):
                self.protocolSection = element.get("hasResults")


# class ProtocolSection:
#     identificationModule: dict
#     statusModule: dict
#     sponsorCollaboratorsModule: dict
#     descriptionModule: dict
#     conditionsModule: dict
#     designModule: dict
#     armsInterventionsModule: dict
#     outcomesModule: dict
#     eligibilityModule: dict
#     contactsLocationsModule: dict
#
#     def __init__(self, protocol_section_json_as_dict: dict):
#         for element in protocol_section_json_as_dict:
#             if element.get('identificationModule'):
#                 self.identificationModule = element.get('identificationModule')


if __name__ == "__main__":
    s = Main("data.json")
    #print(s.nextPageToken)
    a = Studies(s.studies)

   # pr_section = ProtocolSection(s.a.protocolSection)
    #print(pr_section.identificationModule)
    pass
