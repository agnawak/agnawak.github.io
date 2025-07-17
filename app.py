
from flask import Flask, render_template, request, redirect, url_for
from models import db, TestCase

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testcases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    testcases = TestCase.query.all()
    return render_template('index.html', testcases=testcases)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        selected_os = request.form.getlist('os')
        hardware = request.form.getlist('hardware')
        new_case = TestCase(
            title=request.form['title'],
            os = request.form['os'],
            hardware_required=request.form['hardware_required'],
            hardware=", ".join(hardware),
            # steps=request.form['steps'],
            # expected_result=request.form['expected_result'],
            protocol=", ".join(request.form.getlist('protocol')),
            priority=", ".join(request.form.getlist('priority')),
            state=request.form['state']
        )
        db.session.add(new_case)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    case = TestCase.query.get_or_404(id)
    if request.method == 'POST':
        case.title = request.form['title']
        case.os = request.form['os']
        case.hardware_required =", ".join(request.form.getlist('hardware_required'))
        case.hardware = ", ".join(request.form.getlist('hardware'))
        # case.steps = request.form['steps']
        # case.expected_result = request.form['expected_result']
        case.protocol = ", ".join(request.form.getlist('protocol'))
        case.priority = ", ".join(request.form.getlist('priority'))
        case.state = request.form['state']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', case=case)

@app.route('/delete/<int:id>')
def delete(id):
    case = TestCase.query.get_or_404(id)
    db.session.delete(case)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
