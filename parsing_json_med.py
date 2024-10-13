from data_class_module.study_class import Main


if __name__ == "__main__":
    s = Main("data.json")

    s.fill_studies()
    #s.list_studies[0].protocolSection.identificationModule.fill_sec_id_info()
    b = s.list_studies

    #print(b[0].protocolSection.identificationModule.list_sec_id_info[0].type_sec)
    # print(b[0].protocolSection.statusModule.startDateStruct.date_start_date)
    print(b[0].protocolSection.statusModule.primaryCompletionDateStruct)

    pass
