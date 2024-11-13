from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

budget=Flask(__name__)
budget.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tracker.db'
budget.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(budget)


class BTracker(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    date=db.Column(db.Date,nullable=False)
    category=db.Column(db.String(100),nullable=False)
    description=db.Column(db.String(200))
    amount=db.Column(db.Float,nullable=False)

@budget.route('/')
def index():
    expenses=BTracker.query.all()
    total_amount=sum(exp.amount for exp in expenses)
    return render_template('bdtracker/index.html',expenses=expenses,total_amount=total_amount)

@budget.route('/add',methods=['GET','POST'])
def add_expense():
    if request.method == "POST":
        category=request.form['category']
        description=request.form['description']
        amount=float(request.form['amount'])
        date=datetime.strptime(request.form['date'],'%Y-%m-%d')
        new_expense=BTracker(category=category,description=description,amount=amount,date=date)
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('bdtracker/add_expense.html')


@budget.route('/delete/<int:id>')

def delete_expense(id):
    expense=BTracker.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('index'))


@budget.route('/update/<int:id>',methods=['GET','POST'])

def update_expense(id):
    update_expense=BTracker.query.get_or_404(id)
    if request.method=="POST":
        update_expense.category=request.form["cat"]
        update_expense.description=request.form["desc"]
        update_expense.amount=request.form["amt"]
        update_expense.date=datetime.strptime(request.form['dat'],'%Y-%m-%d')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("bdtracker/update_expense.html",expense=update_expense)





if __name__=="__main__":
    budget.run(debug=True)




# datetime.strptime(): This is a method from Python's datetime module. It is used to convert a string representation of a date into a datetime object, based on a specified format.