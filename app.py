from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_qr_code():
    if request.method == "POST":
        url = request.form.get("url")
        if url:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            img_io = BytesIO()
            img.save(img_io, "PNG")
            img_io.seek(0)

            return send_file(img_io, mimetype="image/png")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
