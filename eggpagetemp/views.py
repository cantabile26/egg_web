from django.shortcuts import render


def signInView(request):
  context = {}
  load_template = request.path.split('/')
  context['segment'] = load_template
  print("test")
  return render(request, "sign-in.html", context)

def signOutView(request):
  context = {}
  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "sign-up.html", context)

def forgotPassView(request):
  context = {}
  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "forgot-pass.html", context)

def resetPassView(request):
  context = {}
  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "reset-pass.html", context)

def pageLockView(request):
  context = {}
  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "lock.html", context)

def page403View(request):
  context = {}
  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "page-403.html", context)

def page404View(request):
  context = {}
  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "page-404.html", context)

def page500View(request):
  context = {}
  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "page-500.html", context)

