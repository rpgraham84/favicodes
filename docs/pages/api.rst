========================
Available GET Parameters
========================

size
=========

- Specifies the size of the image in square pixels
- Must be an integer <= 256
- Default is 256


color
=========

- Specifies the color of the text
- Must be a CSS3 color name, hexcode, or comma-separated RGBA (eg. "skyblue", "0,0,0,0", or "112233"), case-insensitive
- Supported CSS3 names can be found at: https://en.wikipedia.org/wiki/Web_colors#HTML_color_names
- Hexcodes must be exactly 6 nybbles, without the hash in front eg. "ff6600"
- All RGBA values must be in the range 0-255, including the alpha (in CSS it is usually a float but, in PIL it's 0-255) 
- Default is black


bgcolor
=========

- Specifies the color of the background, same restrictions as 'color'
- Default is 0,0,0,0 


font
=========

- Specifies the font family to use
- Must be either "notosans" or "fontawesome" case-insensitive
- Defaults to "notosans"


style
=========

- Specifies the font style to use
- Different for different families of fonts
- Default is "regular"
- For Noto fonts these are:
    - black
    - blackitalic
    - bold
    - bolditalic
    - brands
    - condensed
    - condensedblack
    - condensedblackitalic
    - condensedbold
    - condensedbolditalic
    - condensedextrabold
    - condensedextrabolditalic
    - condensedextralight
    - condensedextralightitalic
    - condenseditalic
    - condensedlight
    - condensedlightitalic
    - condensedmedium
    - condensedmediumitalic
    - condensedsemibold
    - condensedsemibolditalic
    - condensedthin
    - condensedthinitalic
    - extrabold
    - extrabolditalic
    - extracondensed
    - extracondensedblack
    - extracondensedblackitalic
    - extracondensedbold
    - extracondensedbolditalic
    - extracondensedextrabold
    - extracondensedextrabolditalic
    - extracondensedextralight
    - extracondensedextralightitalic
    - extracondenseditalic
    - extracondensedlight
    - extracondensedlightitalic
    - extracondensedmedium
    - extracondensedmediumitalic
    - extracondensedsemibold
    - extracondensedsemibolditalic
    - extracondensedthin
    - extracondensedthinitalic
    - extralight
    - extralightitalic
    - italic
    - light
    - lightitalic
    - medium
    - mediumitalic
    - regular
    - semibold
    - semibolditalic
    - semicondensed
    - semicondensedblack
    - semicondensedblackitalic
    - semicondensedbold
    - semicondensedbolditalic
    - semicondensedextrabold
    - semicondensedextrabolditalic
    - semicondensedextralight
    - semicondensedextralightitalic
    - semicondenseditalic
    - semicondensedlight
    - semicondensedlightitalic
    - semicondensedmedium
    - semicondensedmediumitalic
    - semicondensedsemibold
    - semicondensedsemibolditalic
    - semicondensedthin
    - semicondensedthinitalic
    - solid
    - thin
    - thinitalic
- For FontAwesome, there are:
    - solid
    - regular
    - brands

fontsize
=========

- Specifies the font size
- Must be an integer <= 256
- Defaults to 192


format
=========

- Specifies the format of the output image
- Must be either "png" or "ico"
- Defaults to "png"


x
=========

- Specifies an X-axis offset from center to draw the text
- Must be between -128 and 128, since the max size is 256
- Defaults to 0


y
=========

- Specifies an Y-axis offset from center to draw the text
- Must be between -128 and 128, since the max size is 256
- Defaults to 0