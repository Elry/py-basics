import json

data = '''
  [
    {
      "id": "001",
      "height": "2",
      "name": "Olarin"
    } , {
      "id": "002",
      "height": "3",
      "name": "Balrog"
    }     
  ]
'''

try:
  info = json.loads(data)
  print(info[0]['name'])
except:
  print('Error')