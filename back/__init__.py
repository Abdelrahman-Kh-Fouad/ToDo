from app import app 
from app import dbUsers 
from models import User

if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0" , port=5000)
