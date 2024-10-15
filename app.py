from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Secret key for CSRF protection
app.config['SECRET_KEY'] = 'supersecretkey'

# In-memory "database" for tasks
tasks = []

# FlaskForm class for the task form
class TaskForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')

# Home route to view all tasks
@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()  # Initialize the form
    if form.validate_on_submit():  # If the form is submitted and valid
        tasks.append({'content': form.task.data})  # Add the task to our list
        return redirect(url_for('index'))
    
    return render_template('index.html', tasks=tasks, form=form)

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):  # Ensure the task ID is within bounds
        tasks.pop(task_id)  # Remove the task
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
