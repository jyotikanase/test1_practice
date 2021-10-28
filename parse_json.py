import json
dics='{"k1":"val1","k2":"val2"}'
json_result = json.loads(dics)
print(json_result)
print(json_result['k2'])