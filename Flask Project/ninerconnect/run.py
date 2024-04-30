from app import create_app

app = create_app() # App to run flask app

if __name__ == "__main__":
    app.run(debug=True)
