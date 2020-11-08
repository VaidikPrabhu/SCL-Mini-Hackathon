from flask import Flask, request,render_template
from covid import Covid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('covid.html')

def get_country(country):

    covid=Covid()
    country=covid.get_status_by_country_name(country)
    confirmed=country['confirmed']
    active=country['active']
    recovered=country['recovered']
    deaths=country['deaths']
    """a=f'In {country} confirmed cases are {confirmed}, active cases are {active}, recovered cases are {recovered} and deaths {deaths}'"""
    return  confirmed,active,recovered,deaths


@app.route('/process',methods=['POST'])

def process():
    country1=request.form["country"]
    print(country1)
    confirmed,active,recovered,deaths=get_country(country1)
    return render_template('covid_result.html', confirmed=confirmed,active=active,recovered=recovered,deaths=deaths,country=country1)





if __name__ == '__main__':
	# Remove "debug = True" when deployed in production 
    app.run(debug = True)
