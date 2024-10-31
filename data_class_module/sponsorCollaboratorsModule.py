from FIRST_FSAPI.data_class_module.responsibleParty import ResponsibleParty
from FIRST_FSAPI.data_class_module.collaborators import Collaborators

class SponsorCollaboratorsModule:
    responsibleParty: object
    leadSponsor: object
    collaborators: list

    def __init__(self, sponsorCollaboratorsModule_as_dict):
        self.list_of_collaborators = []
        self.responsibleParty = ResponsibleParty(sponsorCollaboratorsModule_as_dict.get("responsibleParty"))
        self.collaborators = sponsorCollaboratorsModule_as_dict.get("collaborators")
        self.leadSponsor = sponsorCollaboratorsModule_as_dict.get("leadSponsor")

    def fill_collaborrators(self):
        if self.collaborators:
            for element in self.collaborators:
                collaborators_name = element.get("name", None)
                collaborators_class = element.get("class", None)
                object_collaborators = Collaborators(collaborators_name, collaborators_class)
                self.list_of_collaborators.append(object_collaborators)
