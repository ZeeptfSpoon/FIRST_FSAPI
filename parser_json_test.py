import json


class Main:
    """
    json to obj with studies and nextPageToken

    """
    studies: list
    nextPageToken: str

    def __init__(self, file_name):
        file = json.load(open(file_name))
        if file:
            self.nextPageToken = file.get('nextPageToken')
            self.studies = file.get('studies')

    # def unpuck(self, key_index, key_word):
    #     file = key_index
    #     com_data = file.get(key_word)
    #     print(com_data)
    #
    #     for key, value in com_data.items():
    #         print(value)


class Studies:
    protocolSection: list
    derivedSection: list
    hasResults: bool

    def __init__(self, main_brunch_name):
        for element in main_brunch_name.studies:
            if element == "protocolSection":
                self.protocolSection = element
        # print(self.protocolSection)
        # self.derivedSection =
        # self.hasResults =


if __name__ == "__main__":
    s = Main("data.json")
    print(s.nextPageToken)
    a = Studies(Main)
    a
    print(a.protocolSection)
    pass
