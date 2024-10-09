from FIRST_FSAPI.parsing_json_med import IdentificationModule

from FIRST_FSAPI.parsing_json_med import StatusModule


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
        self.identificationModule = IdentificationModule(protocol_section_json_as_dict.get('identificationModule'))
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
