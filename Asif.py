	from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('leave_form.html')

@app.route('/submit_leave_form', methods=['POST'])
def submit_leave_form():
    student_id = request.form['student_id']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    reason = request.form['reason']

    # Insert the leave application data into the database here

    return "Leave application submitted successfully!"

if __name__ == '__main__':
    app.run()