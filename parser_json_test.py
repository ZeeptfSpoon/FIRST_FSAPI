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
                if file.get('nextPageToken'):
                    self.nextPageToken = file.get('nextPageToken')
                if file.get('studies'):
                    self.studies = file.get('studies')

    def fill_studies(self):
        for element in self.studies:
            hasResults = False
            if element.get("protocolSection"):
                protocolSection = ProtocolSection(element.get("protocolSection"))
            if element.get("derivedSection"):
                derivedSection = element.get("derivedSection")
            if element.get("hasResults"):
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
        :param studies_json_as_list:
        """
        self.protocolSection = protocolSection
        self.derivedSection = derivedSection
        self.hasResults = hasResults


class ProtocolSection:
    identificationModule: object
    statusModule: object
    sponsorCollaboratorsModule: object
    descriptionModule: object
    conditionsModule: object
    designModule: object
    armsInterventionsModule: object
    outcomesModule: object
    eligibilityModule: object
    contactsLocationsModule: object

    def __init__(self, protocol_section_json_as_dict: dict):
        # for element in protocol_section_json_as_dict:
        if protocol_section_json_as_dict.get('identificationModule'):
            self.identificationModule = IdentificationModule(protocol_section_json_as_dict.get('identificationModule'))
            """
            activate next pages when Classes are ready 
            """
        # if protocol_section_json_as_dict.get('statusModule'):
        #     self.statusModule = StatusModule(protocol_section_json_as_dict.get('statusModule'))
        # if protocol_section_json_as_dict.get('sponsorCollaboratorsModule'):
        #     self.sponsorCollaboratorsModule = SponsorCollaboratorsModule(
        #         protocol_section_json_as_dict.get('sponsorCollaboratorsModule'))
        # if protocol_section_json_as_dict.get('descriptionModule'):
        #     self.descriptionModule = DescriptionModule(protocol_section_json_as_dict.get('descriptionModule'))
        # if protocol_section_json_as_dict.get('conditionsModule'):
        #     self.conditionsModule = ConditionsModule(protocol_section_json_as_dict.get('conditionsModule'))
        # if protocol_section_json_as_dict.get('designModule'):
        #     self.designModule = DesignModule(protocol_section_json_as_dict.get('designModule'))
        # if protocol_section_json_as_dict.get('armsInterventionsModule'):
        #     self.armsInterventionsModule = ArmsInterventionsModule(
        #         protocol_section_json_as_dict.get('armsInterventionsModule'))
        # if protocol_section_json_as_dict.get('outcomesModule'):
        #     self.outcomesModule = OutcomesModule(protocol_section_json_as_dict.get('outcomesModule'))
        # if protocol_section_json_as_dict.get('eligibilityModule'):
        #     self.eligibilityModule = EligibilityModule(protocol_section_json_as_dict.get('eligibilityModule'))
        # if protocol_section_json_as_dict.get('contactsLocationsModule'):
        #     self.contactsLocationsModule = ContactsLocationsModule(
        #         protocol_section_json_as_dict.get('contactsLocationsModule'))


class IdentificationModule:
    nctId: object
    orgStudyIdInfo: object
    secondaryIdInfos: object
    organization: object
    briefTitle: object
    officialTitle: object

    def __init__(self, inf_o):
        self.obj = inf_o


if __name__ == "__main__":
    s = Main("data.json")

    s.fill_studies()
    print(s.list_studies[0])

    print(s.nextPageToken)
    a = Studies()
    print(a.derivedSection)
    pr_section = ProtocolSection(s.a.protocolSection)
    print(pr_section.identificationModule)
    pass
