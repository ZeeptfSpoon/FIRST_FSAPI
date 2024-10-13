from orgstudyIDInfo_class import OrgstudyIdInfo
from organization_class import Organization
from secondaryIdInfos_class import SecondaryIdInfos



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
        self.nctId = inf_o.get("nctId")
        self.orgStudyIdInfo = OrgstudyIdInfo(inf_o.get("orgStudyIdInfo"))
        self.secondaryIdInfos = inf_o.get("secondaryIdInfos")
        self.organization = Organization(inf_o.get("organization"))
        self.briefTitle = inf_o.get("briefTitle")
        self.officialTitle = inf_o.get("officialTitle")
    # def __str__(self):
    #     print(self.obj)

    def fill_sec_id_info (self):
        for element in self.secondaryIdInfos:

            id_sec = element.get("id")
            type_sec = element.get("type", None)
            domain = element.get("domain", None)
            object_sec_id_info = SecondaryIdInfos(id_sec, type_sec, domain)
            self.list_sec_id_info.append(object_sec_id_info)