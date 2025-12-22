from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt


@staff_member_required
@csrf_exempt
def tinymce_image_upload(request):
    """
    Endpoint de upload de imagens para o TinyMCE.

    - Acessível apenas por usuários do admin
    - Usa o storage padrão (Cloudinary)
    - Retorna JSON no formato esperado pelo TinyMCE
    """

    if request.method != "POST" or "file" not in request.FILES:
        return JsonResponse({"error": "Upload inválido"}, status=400)

    image = request.FILES["file"]

    # Salva usando o storage configurado (Cloudinary)
    path = default_storage.save(f"posts/{image.name}", image)
    url = default_storage.url(path)

    return JsonResponse({"location": url})
