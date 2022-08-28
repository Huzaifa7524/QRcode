from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO

# Create your views here.
def qrCode(request):
    data = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""), image_factory=factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        data["svg"] = stream.getvalue().decode()
    return render(request, "home.html", context=data)