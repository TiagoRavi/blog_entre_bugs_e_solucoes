from cloudinary.uploader import upload
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required


@csrf_exempt
@staff_member_required
def tinymce_upload(request):
    """
    Upload handler do TinyMCE usando Cloudinary.

    - Não usa filesystem local
    - Compatível com Render Free
    - Restrito a usuários staff
    """
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
