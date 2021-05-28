import json
import os

class JsonFileRw:
    def __init__(self):
        pass

    def getjsondata(self,string):
        filepath = './data/'+string
        # filepath = os.path.dirname(os.getcwd())+'/data/'+string
        # os.path.join()
        with open(filepath,'r') as f:
            json_data = json.load(f)
        # print(json_data)
        return json_data

if __name__ == '__main__':
    JsonFileRw().getjsondata('test.json')