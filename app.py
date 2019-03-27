from flask import Flask, request, jsonify
import html2text

app = Flask(__name__)

@app.route('/html2md',  methods = ['POST'])
def html2md():
  string = request.get_data().decode('utf8')
  h = html2text.HTML2Text()
  md = h.handle(string)
  return md

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
