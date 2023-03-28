from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'Title':'Data Scientist',
    'Location': 'Delhi, India',
    'Salary': 'Rs 10,000,000'
  },
{
    'id':2,
    'Title':'Front End Engineer',
    'Location': 'Bangalore, India'
  },
{
    'id':3,
    'Title':'Data Analyst',
    'Location': 'New York, USA',
    'Salary': 'USD 100,000'
  }
]

@app.route("/")
def hello_mayank():
    return render_template('home.html', 
                          jobs = JOBS,
                          company_name = "Chukandar" )

if __name__ == "__main__":
  app.run(host = '0.0.0.0',debug = True)
  
  