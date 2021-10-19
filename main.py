from flask import Flask, render_template, request
from sheets import get_colors

website = Flask(__name__)

color = "Deco Blue"
yesno = "Ja!"

df = get_colors()


@website.route("/")
def home():
    return render_template("index.html", color=color, yesno=yesno)


@website.route('/', methods=['POST'])
def my_form_post():
    text = request.form['search']
    return color(text)


@website.route("/search-bar")
def search_bar():
    return render_template("search-bar.html")


@website.route("/<color>")
def color(color):
    return render_template("index.html", color=
    df.loc[df['path_variable'] == color].iloc[0]['Fargenavn'], yesno=
                           df.loc[df['path_variable'] == color].iloc[0][
                               'Bomull'], hex=
                           df.loc[df['path_variable'] == color].iloc[0][
                               'HEX'])


@website.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    website.run()
