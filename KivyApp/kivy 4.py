import io
from kivy.core.image import Image as CoreImage
data = io.BytesIO(open("A:\Mini Project\image.png", "rb").read())
im = CoreImage(data, ext="png")