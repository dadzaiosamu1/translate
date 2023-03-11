from flask import Flask, request
import requests
from urllib.parse import quote

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

def otvet(vopros):
	if vopros:
		server = "https://degtev-api.vercel.app"
		response = requests.get(server+"/d?i="+quote(vopros))
		if response.status_code == 200:
			return response.json().get("result", {})
	return {}

@app.route('/', methods=['GET'])
def home():
	if request.args.get("vopros"):
		return otvet(request.args.get("vopros"))
	return """
<form method='GET'>
<input name="vopros" required style="width: 100%">
<input type="submit" value="Спросить">
</form>
"""

if __name__ == '__main__':
	app.run(debug=True)

