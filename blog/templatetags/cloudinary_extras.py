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


@register.simple_tag
def cloudinary_srcset(resource, widths="480,768,1200", aspect_ratio="1.905"):
    """
    Gera um srcset para Cloudinary.

    Exemplo:
        {% cloudinary_srcset post.featured_image as srcset %}
    """

    if not resource:
        return ""

    entries = []

    for w in [int(x.strip()) for x in widths.split(",")]:
        h = round(w / float(aspect_ratio))

        url = resource.build_url(
            width=w,
            height=h,
            crop="fill",
            gravity="auto",
            quality="auto",
            fetch_format="auto",
            secure=True,
        )

        entries.append(f"{url} {w}w")

    return ", ".join(entries)