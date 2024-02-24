class OrgStudyIdInfo(id):
    id = None


class IndentificationModule(nctid, OrgStudyIdInfo):
    nctid = None
    OrgStudyIdInfo()


class Organisation():
    fullName = None
