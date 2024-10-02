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
        :param
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
        if protocol_section_json_as_dict.get('statusModule'):
            self.statusModule = StatusModule(protocol_section_json_as_dict.get('statusModule'))
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

    def __init__(self, inf_o):                          #inf_o is dict from Prot section
        #self.obj = inf_o
        self.list_sec_id_info = []
        if inf_o.get("nctId"):
            self.nctId = inf_o.get("nctId")
        if inf_o.get("orgStudyIdInfo"):
            self.orgStudyIdInfo = OrgstudyIdInfo(inf_o.get("orgStudyIdInfo"))
        if inf_o.get("secondaryIdInfos"):
            self.secondaryIdInfos = inf_o.get("secondaryIdInfos")
        if inf_o.get("organization"):
            self.organization = Organization(inf_o.get("organization"))
        if inf_o.get("briefTitle"):
            self.briefTitle = inf_o.get("briefTitle")
        if inf_o.get("officialTitle"):
            self.officialTitle = inf_o.get("officialTitle")
    # def __str__(self):
    #     print(self.obj)

    def fill_sec_id_info (self):
        for element in self.secondaryIdInfos:
            if element.get("id"):
                id_sec = element.get("id")
            #if element.get("type"):                       #todo: add mark that not every sec_id_info has type and domain
            type_sec = element.get("type", None)
            if element.get("domain"):
                domain = element.get("domain")
            object_sec_id_info = SecondaryIdInfos(id_sec, type_sec, domain)
            self.list_sec_id_info.append(object_sec_id_info)

class OrgstudyIdInfo:
    id: object

    def __init__(self, orgstudy_as_dict):
        if orgstudy_as_dict.get("id"):
            self.id =  orgstudy_as_dict.get("id")

class SecondaryIdInfos:

    id_sec: object
    type_sec: object
    domain: object

    def __init__(self, id, type, domain):
        self.id_sec = id
        self.type_sec = type
        self.domain = domain

class Organization:
    fullName: object
    org_class: object

    def __init__(self, org_as_dict):
        if org_as_dict.get("fullName"):
            self.fullName = org_as_dict.get("fullName")
        if org_as_dict.get("class"):
            self.org_class = org_as_dict.get("class")

class StatusModule:
    statusVerifiedDate: object
    overallStatus: object
    expandedAccessInfo: object
    startDateStruct: object
    primaryCompletionDateStruct: object
    completionDateStruct: object
    studyFirstSubmitDate: object
    studyFirstSubmitQcDate: object
    studyFirstPostDateStruct: object
    lastUpdateSubmitDate: object
    lastUpdatePostDateStruct: object

    def __init__(self, status_module_dict):
        if status_module_dict.get("statusVerifiedDate"):
            self.statusVerifiedDate = status_module_dict.get("statusVerifiedDate")
        if status_module_dict.get("overallStatus"):
            self.overallStatus = status_module_dict.get("overallStatus")
        if status_module_dict.get("expandedAccessInfo"):
            self.expandedAccessInfo = ExpandedAccessInfo(status_module_dict.get("expandedAccessInfo"))
        if status_module_dict.get("startDateStruct"):
            self.startDateStruct = status_module_dict.get("startDateStruct")
        if status_module_dict.get("primaryCompletionDateStruct"):
            self.primaryCompletionDateStruct = status_module_dict.get("primaryCompletionDateStruct")
        if status_module_dict.get("completionDateStruct"):
            self.completionDateStruct = status_module_dict.get("completionDateStruct")
        if status_module_dict.get("studyFirstSubmitDate"):
            self.studyFirstSubmitDate = status_module_dict.get("studyFirstSubmitDate")
        if status_module_dict.get("studyFirstSubmitQcDate"):
            self.studyFirstSubmitQcDate = status_module_dict.get("studyFirstSubmitQcDate")
        if status_module_dict.get("studyFirstPostDateStruct"):
            self.studyFirstPostDateStruct = status_module_dict.get("studyFirstPostDateStruct")
        if status_module_dict.get("lastUpdateSubmitDate"):
            self.lastUpdateSubmitDate = status_module_dict.get("lastUpdateSubmitDate")
        if status_module_dict.get("lastUpdatePostDateStruct"):
            self.lastUpdatePostDateStruct = status_module_dict.get("lastUpdatePostDateStruct")

class ExpandedAccessInfo:
    hasExpandedAccess: bool

    def __init__(self, expanded_access_info_as_dict):
        #if expanded_access_info_as_dict.get("hasExpandedAccess", ):
        self.hasExpandedAccess = expanded_access_info_as_dict.get("hasExpandedAccess", True)

if __name__ == "__main__":
    s = Main("data.json")

    s.fill_studies()
    s.list_studies[0].protocolSection.identificationModule.fill_sec_id_info()
    b = s.list_studies

    #print(b[0].protocolSection.identificationModule.list_sec_id_info[2].type)
    print(b[0].protocolSection.statusModule.expandedAccessInfo.hasExpandedAccess)

    # a = s.list_studies
    # print(s.nextPageToken)
    # a =
    # print(a.derivedSection)
    #pr_section = ProtocolSection(s.list_studies.protocolSection)
    # print(pr_section.identificationModule)
    pass
