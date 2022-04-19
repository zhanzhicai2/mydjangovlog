data = ['ddd','naes']
import pytest
def func(request):
  name = request.param
  print(name)

func(data)