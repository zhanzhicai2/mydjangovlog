data = ['ddd','naes']
def func(request):
  name = request.param
  print(name)

func(data)