from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image
from .drive_utils import upload_file_to_drive, get_public_url
from django.http import HttpResponse

def home(request):
    return render(request, 'upload.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            try:
                drive_id = upload_file_to_drive(image_instance.image.path, image_instance.image.name)
                image_instance.drive_id = drive_id
                image_instance.public_url = get_public_url(drive_id)
                print(f"Public URL: {image_instance.public_url}") 
                image_instance.save()
            except Exception as e:
                
                return HttpResponse(f"Error uploading file: {e}", status=500)
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})


def image_list(request):
    images = Image.objects.all()
    for image in images:
        print(f"Image URL: {image.public_url}") 
    return render(request, 'image_list.html', {'images': images})

def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('image_list')
