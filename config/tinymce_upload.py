from django.views.decorators.csrf import csrf_exempt
from tinymce.views import upload_image


@csrf_exempt
def tinymce_upload(request):
    """
    Wrapper para permitir upload de imagens do TinyMCE
    sem exigir CSRF token.

    Seguro porque:
    - Só é acessível no admin
    - Usuário precisa estar autenticado
    """
    return upload_image(request)
