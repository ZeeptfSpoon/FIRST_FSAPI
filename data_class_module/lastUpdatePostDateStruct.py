class LastUpdatePostDateStruct:
    last_update_post_date: object
    last_update_post_type: object


    def __init__(self, lastUpdatePostDateStruct_as_dict):
        self.last_update_post_date = lastUpdatePostDateStruct_as_dict.get("date")
        self.last_update_post_type = lastUpdatePostDateStruct_as_dict.get("type")