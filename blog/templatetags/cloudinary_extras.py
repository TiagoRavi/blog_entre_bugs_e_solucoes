from django import template

register = template.Library()


@register.simple_tag
def cloudinary_image(resource, width, height, crop="fill"):
    if not resource:
        return ""

    return resource.build_url(
        width=width,
        height=height,
        crop=crop,
        gravity="auto",
        quality="auto",
        fetch_format="auto",
        secure=True,
    )