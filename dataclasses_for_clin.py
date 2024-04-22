import json
from dataclasses import dataclass

class Studies():
    protocolSection:list
    derivedSection:list
    hasResults:bool

    def unpuck(self, file_name):
        try:
            file = json.load(open(file_name))
        except Exception as e:
            print(e)
        return file
    def unpuck_protocol_section(self, file_name, keyword):
        file = json.load(open(file_name))
        com_data = file.get("studies")
        counter = 0
       # com_data = file.get("studies")[0].get("protocolSection").get("identificationModule")
        for element in com_data:
            ps = element.get("protocolSection")
            im = ps.get("identificationModule")
            key_get = im.get(keyword)
            counter = counter + 1

        print(counter)
        print(key_get)
@dataclass
class ProtocolSection():
    identificationModule:dict
    statusModule:dict
    sponsorCollaboratorsModule:dict
    descriptionModule:dict
    conditionsModule:dict
    designModule:dict
    armsInterventionsModule:dict
    outcomesModule:dict
    eligibilityModule:dict
    contactsLocationsModule:dict

class IdentificationModule():
    nctId:str
    orgStudyIdInfo:dict
    secondaryIdInfos:list
    organization:dict
    briefTitle:str
    officialTitle:str

if __name__ == "__main__":
    s = Studies()
    #f = s.unpuck("data.json")
    s.unpuck_protocol_section("data.json","officialTitle")
