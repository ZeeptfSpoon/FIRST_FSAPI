from data_class_module.expandedAcessInfo_class import ExpandedAccessInfo
from data_class_module.startDateStuct_class import StartDateStruct
from data_class_module.primaryCompletionDateStruct_class import PrimaryCompletionDateStruct



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
        self.statusVerifiedDate = status_module_dict.get("statusVerifiedDate")
        self.overallStatus = status_module_dict.get("overallStatus")
        self.expandedAccessInfo = ExpandedAccessInfo(status_module_dict.get("expandedAccessInfo"))
        self.startDateStruct = StartDateStruct(status_module_dict.get("startDateStruct"))
        self.primaryCompletionDateStruct = PrimaryCompletionDateStruct(status_module_dict.get("primaryCompletionDateStruct"))
        self.completionDateStruct = status_module_dict.get("completionDateStruct")
        self.studyFirstSubmitDate = status_module_dict.get("studyFirstSubmitDate")
        self.studyFirstSubmitQcDate = status_module_dict.get("studyFirstSubmitQcDate")
        self.studyFirstPostDateStruct = status_module_dict.get("studyFirstPostDateStruct")
        self.lastUpdateSubmitDate = status_module_dict.get("lastUpdateSubmitDate")
        self.lastUpdatePostDateStruct = status_module_dict.get("lastUpdatePostDateStruct")