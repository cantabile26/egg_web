from django.shortcuts import render


def main(request):
  context = {}
  load_template = request.path.split('/')[-1]
  context['segment'] = load_template
  return render(request, "index.html", context)

