from django.shortcuts import render, redirect
import os
import torch
import io
from PIL import Image
from django.views.decorators.csrf import csrf_exempt


def eggdetectTables(request):
  context = {}

  load_template = request.path.split('/')
  context['segment'] = load_template

  return render(request, "eggdetect-tables.html", context)




def find_model():
    for f  in os.listdir():
        if f.endswith(".pt"):
            return f
    print("please place a model file in this directory!")
    


def get_prediction(img_bytes):
    model_name = find_model()
    model =torch.hub.load("WongKinYiu/yolov7", 'custom',model_name)

    model.eval()

    img = Image.open(io.BytesIO(img_bytes))
    imgs = [img]  

    results = model(imgs, size=640)
    return results

#@app.route('/', methods=['GET', 'POST'])
@csrf_exempt
def predict(request):
    if request.method == 'POST':
        context = {}
        model_name = find_model()
        model =torch.hub.load("WongKinYiu/yolov7", 'custom',model_name)

        model.eval()

        if 'file' not in request.FILES:
            return redirect(request.url)
        file = request.FILES.get('file')
        if not file:
            return
            
        img_bytes = file.read()
        results = get_prediction(img_bytes)
        results.save(save_dir='static')
        filename = 'image0.jpg'
        context["result_image"] = filename
        context["model_name"] = model_name
        return render(request, 'result__detect.html', context)

    return render(request, 'index_detect.html')