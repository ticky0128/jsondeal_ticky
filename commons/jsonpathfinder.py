import json
from typing import List


class JsonPathFinder:
    def __init__(self, json_data, mode='key'):
        self.data = json_data
        self.mode = mode

    def iter_node(self, rows, road_step, target):
        if isinstance(rows, dict):
            key_value_iter = (x for x in rows.items())
        elif isinstance(rows, list):
            key_value_iter = (x for x in enumerate(rows))
        else:
            return
        for key, value in key_value_iter:
            current_path = road_step.copy()
            current_path.append(key)
            if self.mode == 'key':
                check = key
            else:
                check = value
            if check == target:
                yield current_path
            if isinstance(value, (dict, list)):
                yield from self.iter_node(value, current_path, target)

    def find_one(self, target: str) -> list:
        path_iter = self.iter_node(self.data, [], target)
        for path in path_iter:
            return path
        return []

    def find_all(self, target) -> List[list]:
        path_iter = self.iter_node(self.data, [], target)
        return list(path_iter)

    def find_keypath(self,key="",value=""):
        keypath_list = self.find_all(value)
        if isinstance(value,dict) or isinstance(value,list):
            return keypath_list
        # print(keypath_list)
        for key_list in keypath_list:
            if key_list[-1] == key:
                # print("key_list:{0}".format(key_list))
                return key_list
        return None






if __name__ == '__main__':
    with open('../data/test_samekeyandvalue.json','r' ) as f:
        json_data = json.load(f)
    finder = JsonPathFinder(json_data,'value')
    data = finder.data
    print(data)
    # # 先传要找到的被替换的值
    # key_list = finder.find_keypath("author","Evelyn Waugh")
    # print(key_list)
    # jsonpath_expr = finder.get_jsonpath_expr(key_list)
    # # 替换成对应的值
    # print(finder.change_value(data,jsonpath_expr,"ticky"))

    # print(finder.get_jsonpath_expr(key_list))
    # print(finder.change_value(data,key_list,"ticky"))

    # print('开始测试按 Key 搜索...')
    # finder = JsonPathFinder(json_data)
    # path_list = finder.find_all('category')
    # data = finder.data
    # for path in path_list:
    #     print(path)
    #
    # print('开始测试按 Value 搜索：...')
    #
    value_finder = JsonPathFinder(data, mode='value')
    item = 'fiction'
    item1 =[
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ]
    item2 ={ "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      }

    item3 = {
      "pro":"math",
      "score": 95
    }

    path_lits = value_finder.find_all(item3)
    print('path_lits is {0}'.format(path_lits))
    for path in path_lits:
        print('path: ', path)
        # value = json.loads(json_data)
        # for step in path:
        #     value = value[step]
        # assert value == 103
