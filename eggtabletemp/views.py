from django.shortcuts import render

def bootstrapTables(request):
  context = {}
  
  load_template = request.path.split('/')
  context['segment'] = load_template
  
  return render(request, "bootstrap-tables.html", context)