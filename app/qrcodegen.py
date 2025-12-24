import qrcode
import os
import re

if not os.path.exists("qrcodes"):
    os.mkdir("qrcodes")
    

def safe_filename(text: str) -> str:
    # Replace anything not alphanumeric with _
    return re.sub(r'[^a-zA-Z0-9_-]', '_', text)


def generate_qr_code(url: str) -> str:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    base = safe_filename(url)
    i = 1
    filename = f"qrcodes/qrcode-{base}-{i}.png"

    while os.path.exists(filename):
        i += 1
        filename = f"qrcodes/qrcode-{base}-{i}.png"

    img.save(filename)
    return filename
