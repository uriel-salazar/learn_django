from PIL import Image
from io import BytesIO

def image_resize_800(file):

    image = Image.open(file)
            
    image.thumbnail((800, 800))
    
    output = BytesIO()
    image.save(output, format=image.format or "JPEG",quality=85)
    output.seek(0)
    return output