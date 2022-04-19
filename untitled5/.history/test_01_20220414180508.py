data = ['ddd','naes']
@pytest.fixture()
def func(request):
  name = request.param
  print(name)

func(data)