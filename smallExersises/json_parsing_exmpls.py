import json

jsonstring = '{"name":"Eric","age":38,"married":"True"}'
# person = json.loads(jsonstring)
# print(person['name'], 'is', person['age'], 'years old')
# print(person)


class Jsongparser():
    def __init__(self, jsonstring):
        self.person = json.loads(jsonstring)

    def output(self):
        print(self.person['name'], 'is', self.person['age'], 'years old')

    def orig_dict(self):
        print(self.person)
    # def __str__(self):
    #     return str(self.person)

p1 = Jsongparser(jsonstring)
# p1.orig_dict()
# p1.output()
print(p1)