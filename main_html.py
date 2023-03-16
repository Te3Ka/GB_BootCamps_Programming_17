from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
	name = "Ivan"
	return render_template("base.html", name=name)

if __name__ == '__main__':
	app.run()