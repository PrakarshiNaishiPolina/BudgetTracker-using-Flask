from budget import budget,db

with budget.app_context():
    db.create_all()
    print("database tables created successfully")
    