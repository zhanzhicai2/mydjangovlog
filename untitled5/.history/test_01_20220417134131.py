data = ['ddd','naes']
pytest
def func(request):
  name = request.param
  print(name)

func(data)