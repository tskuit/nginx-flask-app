from app import app
import os

if __name__ == "__main__":
    app.run(host='127.0.0.1', port="8082", debug=False)

##    app.run(host='127.0.0.1', port="8082", debug=True)
##    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT"), debug=True)
