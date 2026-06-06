
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = '''
<h1>Removal of MTI</h1>
<form method="post" enctype="multipart/form-data">
<input type="file" name="audio">
<button type="submit">Analyze</button>
</form>
{% if result %}
<p>{{result}}</p>
{% endif %}
'''

@app.route('/', methods=['GET','POST'])
def home():
    result = None
    if request.method == 'POST':
        result = "Audio received. MTI analysis module can be integrated here."
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True)
