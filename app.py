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


            # the above 3 lines of code can be replaced with the following line of code
            img.save("./static/images/qr_code.png")

            return render_template("index.html",qr_code=True)
    

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
