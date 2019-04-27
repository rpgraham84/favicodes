import json
from collections import defaultdict
from pathlib import Path

import webcolors

from fonts import fonts


def get_icon_by_name(name):
    metafile = Path("./fonts/favicodes-meta.json")
    with open(metafile) as f:
        meta = json.loads(f.read())
    return meta.get(name)


def validate(characters, icon_name, request):
    defaults = {
        "input": "",
        "size": 256,
        "color": (0, 0, 0, 255),
        "bgcolor": (0, 0, 0, 0),
        "font": "fontawesome" if icon_name else "notosans",
        "style": "regular",
        "fontsize": 192,
        "format": "png",
        "x": 0,
        "y": 0,
    }
    errors = defaultdict(list)

    def validate_characters():
        for char in characters:
            if char:
                try:
                    assert (
                        len(char) <= 8
                    ), "unicode hex string can be no longer than 8 nibbles XXXXXXXX"
                    if len(char) > 2:
                        char = chr(int(char, 16))
                except (ValueError, AssertionError) as e:
                    errors["input"].append(str(e))
                else:
                    defaults["input"] += char
                    if len(defaults["input"]) == 2:
                        break

    def validate_colors(params=["color", "bgcolor"]):
        param = params.pop()
        color = request.args.get(param)
        if color:
            color = color.lower()
            if color in webcolors.CSS3_NAMES_TO_HEX:
                defaults[param] = tuple(list(webcolors.name_to_rgb(color)) + [255])
            elif "," in color:
                try:
                    color = tuple(map(int, color.split(",")))
                    assert len(color) == 4, "RGBA color must be in the form 'R,G,B,A'"
                    assert all(
                        0 <= v <= 255 for v in color
                    ), "All RGBA values must be in the range 0-255"
                except (ValueError, AssertionError) as e:
                    errors[param].append(str(e))
                else:
                    defaults[param] = color
            elif len(color) == 6:
                try:
                    color = tuple(list(webcolors.hex_to_rgb(f"#{color}")) + [255])
                except ValueError as e:
                    errors[param].append(str(e))
                else:
                    defaults[param] = color
            else:
                errors[param].append(str("Color must be a CSS3 name, hexcode, or RGBA"))

        if params:
            validate_colors(params)

    # These functions run in alphabetical order, which is important for
    # defaults['style'] to be set properly
    def validate_font_and_style():
        font = request.args.get("font", defaults["font"])
        style = request.args.get("style", defaults["style"])
        try:
            fontnames = set(f[0] for f in fonts)
            assert font in fontnames, f"Font must be one of {fontnames}"
        except (ValueError, AssertionError) as e:
            errors["font"].append(str(e))
            return
        else:
            defaults["font"] = font.lower()

        try:
            valid_styles = set(k[1] for k, v in fonts.items() if font == k[0])
            assert (
                style in valid_styles
            ), f"Style must be one of {valid_styles} if font is {font}"
        except (ValueError, AssertionError) as e:
            errors["style"].append(str(e))
        else:
            defaults["style"] = style

    def validate_format():
        frmat = request.args.get("format")
        valid_formats = ["png", "ico"]
        if frmat:
            try:
                assert frmat in valid_formats, "format must be one of ['png', 'ico']"
            except AssertionError as e:
                errors["input"].append(str(e))

    def validate_icon():
        style = request.args.get("style")
        if icon_name:
            icon = get_icon_by_name(icon_name)
            if not icon:
                errors["icon_name"].append(f"'{icon_name}' is not a valid icon name")
            else:
                if style not in icon["styles"]:
                    defaults["style"] = icon["styles"][0]
                defaults["input"] += chr(int(icon["unicode"], 16))

    def validate_lte_256(params=["size", "fontsize"]):
        param = params.pop()
        size = request.args.get(param)
        if size:
            try:
                size = abs(int(size))
                assert size <= 256, "Size must be <= 256"
            except (ValueError, AssertionError) as e:
                errors[param].append(str(e))
            else:
                defaults[param] = size

        if params:
            validate_lte_256(params)

    def validate_offset(params=["x", "y"]):
        param = params.pop()
        value = request.args.get(param)
        if value:
            try:
                value = int(value)
                assert -128 <= value <= 128, "value must satisfy -128 <= value <= 128"
            except (ValueError, AssertionError) as e:
                errors[param].append(str(e))
            else:
                defaults[param] = value

        if params:
            validate_offset(params)

    for name, validator in sorted(locals().items()):
        if name.startswith("validate_") and callable(validator):
            print(name)
            validator()

    if errors:
        return False, errors

    return True, defaults
