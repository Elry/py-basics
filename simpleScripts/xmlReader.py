import xml.etree.ElementTree as ET

input = '''
<outer>
  <users>
    <user x="0">
      <id>001</id>
      <name>Nargaroth</name>
    </user>
    <user x="1">
      <id>002</id>
      <name>Morgoth</name>
    </user>
  </users>
</outer>
'''

try:
  users = ET.fromstring(input)
  lst = users.findall('users/user')

  print('User count:', len(lst))

  for item in lst:
    print("name:", item.find('name').text)
    print("id:", item.find('id').text)
    print("Attributes", item.get("x"))
except:
  print('Error')