import webbrowser, os


def build_translated_menu(line_to_image):
    h = ""  # html string
    h += "<html>"
    h += "<h1>Translated menu</h1>"
    h += "<table>"
    for line in line_to_image:
        h += "<tr>"

        h += "<td>"
        h += "<p>{}</p>".format(line[1])
        h += "</td>"

        h += "<td>"
        h += "<img src={}>".format(line[0])
        h += "</td>"

        h += "</tr>"

    h += "</table>"
    h += "</html>"

    html_file = open("menu.html", "w")
    html_file.write(h)
    html_file.close()

    webbrowser.open('file://' + os.path.realpath("menu.html"))
