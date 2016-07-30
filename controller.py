from flask import Flask, render_template, request
from wtforms import Form, TextField, validators
from scaled import scaled

app = Flask(__name__)

# Model
class InputForm(Form):
    r = TextField(validators=[validators.InputRequired()])

# View
@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = scaled(r)
        return render_template("view_output.html", form=form, s=s)
    else:
        return render_template("view_input.html", form=form)

if __name__ == '__main__':
	app.run(debug=True)