from django.core.exceptions import ValidationError


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    print(ext)
    valid_extensions = ['.jpg', '.png', '.mp4', '.ico']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
