from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/")
def main(request):
  context = {}
  load_template = request.path.split('/')[-1]
  context['segment'] = load_template
  return render(request, "index.html", context)

