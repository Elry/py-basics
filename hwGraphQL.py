import graphene

class Query(graphene.ObjectType):
  sk = graphene.String(name=graphene.String(default_value="Sekai"))

  def resolve_sk(self, info, name):
    return 'Kono subarashi ' + name

try:
  schema = graphene.Schema(query=Query)
  result = schema.execute('{sk}')
  print(result)
except:
  print('Error')