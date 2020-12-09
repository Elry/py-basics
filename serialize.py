json_data = """\
{
    "a": [1,2,3],
    "b": [4,5,6],
    "greeting" : "Hello"
}"""
import json
json.loads(json_data)
json.dumps({"a":[1,2,3],"b":[9,10,11],"greeting":"Hola"})
