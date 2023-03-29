from flask import Flask, render_template, jsonify

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
    'Salary': 'USD 120,000'
  }
]

@app.route("/")
def hello_mayank():
    return render_template('home.html', 
                          jobs = JOBS,
                          company_name = "MJ Inc" )

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host = '0.0.0.0',debug = True)
  
  