from jsonpath_ng import jsonpath, parse
from commons.jsonpathfinder import JsonPathFinder
class JsonDeal:
    def __init__(self):
        pass

    def get_jsonpath_expr(self,key_list):
        str_final = '$'
        if len(key_list)>1:
            key_list = key_list[0]
        for path in key_list:
            if isinstance(path,str):
                str_final = str_final + '.'+path
            elif isinstance(path,int):
                str_final = str_final + '.['+str(path)+']'
            else:
                raise Exception('There Are Some Illegal Elements in key_list:{0}'.format(key_list))
        # print(str_final)
        return str_final

    def set_value_by_jsonpath(self,json_data,jsonpath_expr,target):
        final_json = parse(jsonpath_expr)
        final_json.find(json_data)
        final_json.update(json_data, target)
        return json_data

if __name__ == '__main__':
    # JsonDeal().get_jsonpath_expr([1,'23','aaa',(1,2)])
    print(JsonDeal().set_value_by_jsonpath({"a":123,"b":1234},"$.a","sss"))