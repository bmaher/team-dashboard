import re

from data import data_store as ds
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<name>", methods=["GET", "POST"])
def grid_item(name):
    data = ds.load_data()

    if request.method == "POST":
        text = request.form["text"].strip().replace("\\n", "\n")
        lines = [item.strip() for item in re.split(r"[,\n]+", text) if item.strip()]
        data[name] = lines if len(lines) > 1 else (lines[0] if lines else "?")
        ds.save_data(data)

    is_list = isinstance(data[name], list)
    if is_list:
        text = "\n".join(data[name])
    else:
        text = data[name].strip() if data[name] else "?"

    if request.args.get("edit"):
        return render_template(
            "components/edit.html", name=name, text=text, is_list=is_list
        )

    return render_template(
        "components/display.html", name=name, text=data[name], is_list=is_list
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
