# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
import io
import json
from pathlib import Path

from flask import Flask, jsonify, request, send_file
from PIL import Image, ImageDraw, ImageFont

from fonts import fonts
from validation import validate

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
app.url_map.strict_slashes = False


def generate(args):
    img = Image.new("RGBA", (args["size"], args["size"]), args["bgcolor"])
    fontpath = fonts.get((args["font"], args["style"]))
    with open(fontpath, "rb") as f:
        font = ImageFont.truetype(f, args["fontsize"])
    draw = ImageDraw.Draw(img)
    w, h = draw.textsize(args["input"], font=font)
    draw.text(
        # Calculate X, Y to center the textarea in the image
        (((args["size"] - w) // 2) + args["x"], ((args["size"] - h) // 2) + args["y"]),
        args["input"],
        args["color"],
        font=font,
    )
    buf = io.BytesIO()
    img.save(buf, format=args["format"])
    buf.seek(0)
    return buf


# @app.route("/update_icons/")
def update_icons():
    iconsfile = Path("./fonts/fontawesome-free-5.8.1-desktop/metadata/icons.json")
    metafile = Path("./fonts/favicodes-meta.json")
    with open(iconsfile) as f:
        icons = json.loads(f.read())

    meta = {
        name: {
            "unicode": attrs["unicode"],
            "styles": attrs["styles"],
            "search_terms": attrs["search"]["terms"],
        }
        for name, attrs in icons.items()
    }

    with open(metafile, "w") as f:
        f.write(json.dumps(meta))

    return "Done!"


@app.route("/", defaults={"left": None, "right": None, "icon_name": None})
@app.route("/fa/<icon_name>", defaults={"left": None, "right": None})
@app.route("/<left>", defaults={"right": None, "icon_name": None})
@app.route("/<left>/<right>", defaults={"icon_name": None})
def make_icon(left, right, icon_name):
    valid, args = validate((left, right), icon_name, request)
    if not valid:
        return jsonify(args)

    mime = "image/png" if args["format"] == "png" else "image/x-icon"
    return send_file(generate(args), mime)


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_python37_app]
