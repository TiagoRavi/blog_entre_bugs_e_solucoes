from cloudinary.uploader import upload
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def tinymce_upload(request):
    """
    Upload handler do TinyMCE usando Cloudinary.

    - Não usa filesystem local
    - Compatível com Render Free
    - Retorna JSON (obrigatório para AJAX)
    - Segurança baseada em autenticação do usuário
    """

    if not request.user.is_authenticated or not request.user.is_staff:
        return JsonResponse({"error": "Unauthorized"}, status=403)

    if request.method != "POST" or "file" not in request.FILES:
        return JsonResponse({"error": "Invalid request"}, status=400)

    image = request.FILES["file"]

    result = upload(
        image,
        folder="posts",
        resource_type="image",
        use_filename=True,
        unique_filename=True,
    )

    return JsonResponse(
        {
            "location": result["secure_url"]
        }
    )
