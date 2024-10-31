class StudyFirstPostDateStruct:
    study_frst_post_date: object
    study_frst_post_type: object


    def __init__(self, studyFirstPostDateStruct_as_dict):
        self.study_frst_post_date = studyFirstPostDateStruct_as_dict.get("date")
        self.study_frst_post_type = studyFirstPostDateStruct_as_dict.get("type")
