import oyaml as yaml
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    website_data = yaml.load(open('_config.yaml', encoding='utf8'),Loader=yaml.SafeLoader)

    return render_template('index.html', data=website_data)


@app.route('/certificadoTDCOnline2021Innovationpdf')
def nada():
    return "static/certificados/certificadoTDCOnline2021Innovation.pdf"


if __name__ == '__main__':
    app.run(port=5000, debug=True)
