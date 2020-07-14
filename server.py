from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/components.html')
def components():
    return render_template('components.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/download.html')
def download():
    return render_template('download.html')

@app.route('/pricing.html')
def pricing():
    return render_template('pricing.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode ='a') as database:
		name = data["name"]
		email = data['email']
		subject = data['subject']
		message = data['message']
		file=database.write(f'\n{name},{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', mode ='a', newline='') as database2:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer= csv.writer(database2, delimiter =',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,subject,message])

@app.route('/enviar_formulario', methods=['POST', 'GET'])
def enviar_formulario():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_to_csv(data)
    	return redirect('thanks.html')
    else:
    	return 'deu ruim!'
