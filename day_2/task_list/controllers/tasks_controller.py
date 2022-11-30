from flask import Flask, render_template, Blueprint, request, redirect
from repos import task_repo, user_repo
from models.task import Task

tasks_blueprint = Blueprint("tasks", __name__)

# INDEX 
# GET '/tasks'
@tasks_blueprint.route('/tasks')
def tasks():
    all_tasks = task_repo.select_all()
    return render_template('tasks/index.html', all_tasks=all_tasks)


# NEW (display form)
# GET '/tasks/new'

@tasks_blueprint.route('/tasks/new')
def new_task():
    users = user_repo.select_all()
    return render_template('tasks/new.html', users=users)

# CREATE (save)
# POST '/tasks'
@tasks_blueprint.route('/tasks', methods=['POST'])
def create_task():
    description = request.form['description']
    duration = request.form['duration']
    completed = request.form['completed']
    user_id = request.form['user_id']
    user = user_repo.select(user_id) 
    task = Task(description, user, duration, completed)
    task_repo.save(task)
    return redirect('/tasks')


# SHOW
# GET '/tasks/<id>'
@tasks_blueprint.route('/tasks/<task_id>')
def show_one_task(task_id):
    task = task_repo.select(task_id)
    return render_template('tasks/show.html', task=task)

# EDIT (display form) 
# GET '/tasks/<id>/edit'
@tasks_blueprint.route('/tasks/<task_id>/edit')
def edit_task(task_id):
    task = task_repo.select(task_id)
    users = user_repo.select_all()
    return render_template('tasks/edit.html', users=users, task=task)


# UPDATE
# PUT '/tasks/<id>'
# PUT indicates updating an existing resource
@tasks_blueprint.route('/tasks/<task_id>', methods=['POST'])
def update(task_id):
    description = request.form['description']
    duration = request.form['duration']
    completed = request.form['completed']
    user_id = request.form['user_id']
    user = user_repo.select(user_id) 
    task = Task(description, user, duration, completed, task_id)
    task_repo.update(task)
    return redirect ('/tasks')



# DELETE
# DELETE '/tasks/<id>/delete'
@tasks_blueprint.route('/tasks/<task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task_repo.delete(task_id)
    return redirect('/tasks')

