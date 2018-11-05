from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.models import Task
from app import db

DATABASE = 'app.db'

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Task: {},Task description: {},Start of task: {},remember_me={},'.format(
            form.task.data,form.description.data,form.start.data,form.remember_me.data))



        return redirect(url_for('messages'))

    return render_template('login.html',  title='Task Form', form=form)


@app.route('/messages',methods=['GET', 'POST'])
def messages():
    tasks = Task.query.all()
    tasks = Task.query.order_by(Task.task).all()

    if len(tasks) == 1:
        tasks[0].active = True
        active = tasks[0].task_id
        db.session.commit()


    if tasks:
        return render_template('index.html', tasks=tasks,)
