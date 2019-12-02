import flask
import os

app = flask.Flask(__name__)

@app.route('/get',methods =['GET'])
def fetech_data():
    return "Hello Sultan Mirza This container 2 flask !!!!!!!!!!!!1"

@app.route('/get/make_ssh',methods =['GET'])
def make_ssh_con():
    os.system("mkdir flask_dir")
    # os.system("sshpass -p gslab@123 ssh gslab@192.168.1.106")
    os.system("python3 ssh_w_python.py")
    return "Your python code for ssh is running...... "



if __name__ == "__main__":
    app.run(debug=True,port=5005,host='0.0.0.0')