from flask import Flask
app = Flask("app")

@app.route("/")
def hello_world():
  return "Heya! I’m going to crush Flask! #SkillcrushingIt."

app.run(host='0.0.0.0', port=8080)