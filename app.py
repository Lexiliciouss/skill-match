from flask import Flask, request
import csv

app = Flask(__name__)

# define the endpoint
@app.route('/survey_questions', methods=['POST'])
def survey_questions():
    # get user answers from the request
    name = request.form.get('name')
    skills_used = request.form.get('skills_used')
    skills_to_learn = request.form.get('skills_to_learn')
    time_available = request.form.get('time_available')
    
    # save user answers to a csv file
    with open('user_responses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, skills_used, skills_to_learn, time_available])
    
    # return a success message 
    return 'Thanks for completing the survey!'

if __name__ == '__main__':
    app.run(debug=True)
