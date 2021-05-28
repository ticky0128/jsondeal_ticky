from commons.jsonpathfinder import JsonPathFinder
from commons.jsondeal import JsonDeal
from commons.jsonfilerw import JsonFileRw


def test(filename,key="",value="",target=""):
    test_data = JsonFileRw().getjsondata(filename)
    # find jsonpath by value
    value_finder = JsonPathFinder(test_data,'value')
    print(value_finder.data)
    #find jsonpath by key
    # key_finder = JsonPathFinder(test_data)
    key_list = value_finder.find_keypath(key,value)
    print(key_list)
    jsonpath_expr = JsonDeal().get_jsonpath_expr(key_list)
    # print(jsonpath_expr)
    need_deal_data = value_finder.data
    # print(need_deal_data)
    JsonDeal().set_value_by_jsonpath(need_deal_data, jsonpath_expr, target)
    return need_deal_data

if __name__ == '__main__':
    # parameters:filename,key,value,target
    # value means the value that should be changed
    item = [{
      "pro":"math",
      "score": 95
    },
    {
      "pro":"Chinese",
      "score": 94
    }]

    item1 = [{
      "pro":"math",
      "score": 123
    },
    {
      "pro":"Chinese",
      "score": 94
    }]

    item2 = {
      "pro":"math",
      "score": 95
    }

    item3 = {
      "pro":"math",
      "score": 1234
    }

    print(test('test_samekeyandvalue.json',"",item2,item3))

