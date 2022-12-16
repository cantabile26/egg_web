from django.shortcuts import render
from django.contrib.auth.models import User

def test(request):
  context = {}
  load_template = request.path.split('/')[-1]
  context['segment'] = load_template
  context['user'] = User
  print(User)
  return render(request, "test.html", context)

