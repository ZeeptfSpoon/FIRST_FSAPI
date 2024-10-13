from data_class_module.study_class import Main



# class ProtocolSection:
#     identificationModule: object
#     statusModule: object
#     sponsorCollaboratorsModule: object
#     descriptionModule: object
#     conditionsModule: object
#     designModule: object
#     armsInterventionsModule: object
#     outcomesModule: object
#     eligibilityModule: object
#     contactsLocationsModule: object
#
#     def __init__(self, protocol_section_json_as_dict: dict):
#         # for element in protocol_section_json_as_dict:
#         self.identificationModule = IdentificationModule(protocol_section_json_as_dict.get('identificationModule'))
#         self.statusModule = StatusModule(protocol_section_json_as_dict.get('statusModule'))
#         # if protocol_section_json_as_dict.get('sponsorCollaboratorsModule'):
#         #     self.sponsorCollaboratorsModule = SponsorCollaboratorsModule(
#         #         protocol_section_json_as_dict.get('sponsorCollaboratorsModule'))
#         # if protocol_section_json_as_dict.get('descriptionModule'):
#         #     self.descriptionModule = DescriptionModule(protocol_section_json_as_dict.get('descriptionModule'))
#         # if protocol_section_json_as_dict.get('conditionsModule'):
#         #     self.conditionsModule = ConditionsModule(protocol_section_json_as_dict.get('conditionsModule'))
#         # if protocol_section_json_as_dict.get('designModule'):
#         #     self.designModule = DesignModule(protocol_section_json_as_dict.get('designModule'))
#         # if protocol_section_json_as_dict.get('armsInterventionsModule'):
#         #     self.armsInterventionsModule = ArmsInterventionsModule(
#         #         protocol_section_json_as_dict.get('armsInterventionsModule'))
#         # if protocol_section_json_as_dict.get('outcomesModule'):
#         #     self.outcomesModule = OutcomesModule(protocol_section_json_as_dict.get('outcomesModule'))
#         # if protocol_section_json_as_dict.get('eligibilityModule'):
#         #     self.eligibilityModule = EligibilityModule(protocol_section_json_as_dict.get('eligibilityModule'))
#         # if protocol_section_json_as_dict.get('contactsLocationsModule'):
#         #     self.contactsLocationsModule = ContactsLocationsModule(
#         #         protocol_section_json_as_dict.get('contactsLocationsModule'))


# class IdentificationModule:
#     nctId: object
#     orgStudyIdInfo: object
#     secondaryIdInfos: object
#     organization: object
#     briefTitle: object
#     officialTitle: object
#
#     def __init__(self, inf_o):                          #inf_o is dict from Prot section
#         #self.obj = inf_o
#         self.list_sec_id_info = []
#         self.nctId = inf_o.get("nctId")
#         self.orgStudyIdInfo = OrgstudyIdInfo(inf_o.get("orgStudyIdInfo"))
#         self.secondaryIdInfos = inf_o.get("secondaryIdInfos")
#         self.organization = Organization(inf_o.get("organization"))
#         self.briefTitle = inf_o.get("briefTitle")
#         self.officialTitle = inf_o.get("officialTitle")
#     # def __str__(self):
#     #     print(self.obj)
#
#     def fill_sec_id_info (self):
#         for element in self.secondaryIdInfos:
#
#             id_sec = element.get("id")
#             type_sec = element.get("type", None)
#             domain = element.get("domain", None)
#             object_sec_id_info = SecondaryIdInfos(id_sec, type_sec, domain)
#             self.list_sec_id_info.append(object_sec_id_info)

# class OrgstudyIdInfo:
#     id: object
#
#     def __init__(self, orgstudy_as_dict):
#
#         self.id =  orgstudy_as_dict.get("id")
#
# class SecondaryIdInfos:
#
#     id_sec: object
#     type_sec: object
#     domain: object
#
#     def __init__(self, id, type, domain):
#         self.id_sec = id
#         self.type_sec = type
#         self.domain = domain
#
# class Organization:
#     fullName: object
#     org_class: object
#
#     def __init__(self, org_as_dict):
#         self.fullName = org_as_dict.get("fullName")
#         self.org_class = org_as_dict.get("class")

# class StatusModule:
#     statusVerifiedDate: object
#     overallStatus: object
#     expandedAccessInfo: object
#     startDateStruct: object
#     primaryCompletionDateStruct: object
#     completionDateStruct: object
#     studyFirstSubmitDate: object
#     studyFirstSubmitQcDate: object
#     studyFirstPostDateStruct: object
#     lastUpdateSubmitDate: object
#     lastUpdatePostDateStruct: object
#
#     def __init__(self, status_module_dict):
#         self.statusVerifiedDate = status_module_dict.get("statusVerifiedDate")
#         self.overallStatus = status_module_dict.get("overallStatus")
#         self.expandedAccessInfo = ExpandedAccessInfo(status_module_dict.get("expandedAccessInfo"))
#         self.startDateStruct = StartDateStruct(status_module_dict.get("startDateStruct"))
#         self.primaryCompletionDateStruct = status_module_dict.get("primaryCompletionDateStruct")
#         self.completionDateStruct = status_module_dict.get("completionDateStruct")
#         self.studyFirstSubmitDate = status_module_dict.get("studyFirstSubmitDate")
#         self.studyFirstSubmitQcDate = status_module_dict.get("studyFirstSubmitQcDate")
#         self.studyFirstPostDateStruct = status_module_dict.get("studyFirstPostDateStruct")
#         self.lastUpdateSubmitDate = status_module_dict.get("lastUpdateSubmitDate")
#         self.lastUpdatePostDateStruct = status_module_dict.get("lastUpdatePostDateStruct")

# class ExpandedAccessInfo:
#     hasExpandedAccess: bool
#
#     def __init__(self, expanded_access_info_as_dict):
#
#         self.hasExpandedAccess = expanded_access_info_as_dict.get("hasExpandedAccess", True)
#
#
# class StartDateStruct:
#     date_start_date: object
#
#     def __init__(self, start_date_as_dict):
#         self.date_start_date = start_date_as_dict.get("date")
#
# class PrimaryCompletionDateStruct:
#     date_prim_comp: object
#     type_prim_comp: object
#
#     def __init__(self, primary_comp_letion_as_dict):
#         self.date_prim_comp = primary_comp_letion_as_dict.get("date")
#         self.type_prim_comp = primary_comp_letion_as_dict.get("type")


if __name__ == "__main__":
    s = Main("data.json")

    s.fill_studies()
    #s.list_studies[0].protocolSection.identificationModule.fill_sec_id_info()
    b = s.list_studies

    #print(b[0].protocolSection.identificationModule.list_sec_id_info[0].type_sec)
    # print(b[0].protocolSection.statusModule.startDateStruct.date_start_date)
    print(b[0].protocolSection.statusModule.primaryCompletionDateStruct)

    # a = s.list_studies
    # print(s.nextPageToken)
    # a =
    # print(a.derivedSection)
    #pr_section = ProtocolSection(s.list_studies.protocolSection)
    # print(pr_section.identificationModule)
    pass
