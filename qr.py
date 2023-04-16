from flask import Flask, jsonify, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route("/qr", methods=["GET"])
def generate_qr():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png", as_attachment=True, attachment_filename="qr_code.png")

if __name__ == "__main__":
    app.run()
