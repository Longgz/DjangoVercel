from django.shortcuts import render, HttpResponseRedirect
from .forms import ImageForm
from .models import Image
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


def home(request):
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html', {'img': img, 'form': form})


def post_img(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.cleaned_data['note']
            instances = []
            for pt in request.FILES.getlist('photo'):
                instance = Image(note=note, photo=pt)
                instance.save()
                instances.append(instance)
            ser_instances = serializers.serialize('json', instances)
            # return HttpResponseRedirect('/')
            return JsonResponse({'instance': ser_instances}, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)

    return JsonResponse({"error": ""}, status=400)


def delete_img(request, id):
    img = Image.objects.filter(pk=id).first()
    if img:
        img.delete()
    return HttpResponseRedirect('/')


def update_note(request, id):
    if request.method == 'POST':
        img_update = Image.objects.filter(pk=id).first()
        if img_update:
            img_update.note = request.POST['note_update']
            img_update.save()
            ser_instance = serializers.serialize('json', [img_update, ])
            return JsonResponse({'instance': ser_instance}, status=200)
    
    return JsonResponse({"error": ""}, status=400)
