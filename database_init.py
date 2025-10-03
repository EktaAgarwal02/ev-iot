def init_db():
    with app.app_context():
        try:
            db.create_all()
            print("Database initialized successfully!")
        except Exception as e:
            print(f"Error initializing database: {e}")

# Initialize database when application starts
with app.app_context():
    init_db()