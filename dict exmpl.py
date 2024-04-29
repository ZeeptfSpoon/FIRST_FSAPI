import json


class Jsonparser_exersise_1():
    def unpuck(self, file_name, key_word, search_key):
        d1 = json.load(open(file_name))
        # print(d1)
        com_data = d1.get(key_word)
        print(com_data)
        for a in com_data:
            if a == search_key:
                print(com_data[a])
            if a != search_key:
                print("ERROR there is no such key")
            exit()


if __name__ == "__main__":
    s = Jsonparser_exersise_1()
    s.unpuck("dict_for_ex.json", "human", "json")
