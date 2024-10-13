from data_class_module.protocolSection_class import ProtocolSection
import json


class Main:
    """
    json to obj with studies as list and nextPageToken as string

    """
    studies: list
    nextPageToken: str
    list_studies: list

    def __init__(self, file_name=None):
        # container list for class obj studies
        file = None
        self.list_studies = []
        if file_name:
            try:
                file = json.load(open(file_name))
            except Exception as e:
                print(e)
            if file:
                self.nextPageToken = file.get('nextPageToken')
                self.studies = file.get('studies')

    def fill_studies(self):
        for element in self.studies:
            hasResults = False
            protocolSection = ProtocolSection(element.get("protocolSection"))
            derivedSection = element.get("derivedSection")
            hasResults = element.get("hasResults")
            object_studies = Studies(protocolSection, derivedSection, hasResults)
            self.list_studies.append(object_studies)

    def fill_protocolSection(self):
        pass


class Studies:
    protocolSection: object
    derivedSection: dict
    hasResults: bool

    def __init__(self, protocolSection, derivedSection, hasResults):
        """
        "protocolSection" dict
        "derivedSection" dict
        "hasResults" bool
        :param
        """
        self.protocolSection = protocolSection
        self.derivedSection = derivedSection
        self.hasResults = hasResults