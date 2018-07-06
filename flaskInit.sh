#!/usr/bin/env bash

APP_NAME=$1

echo "Building flask app $APP_NAME"
echo "____________________________"
python3 -m venv venv
source venv/bin/activate
pip install flask
mkdir $APP_NAME bin docs tests
# touch run.py

touch $APP_NAME/__init__.py
echo "from flask import Flask" > $APP_NAME/__init__.py
echo "" >> $APP_NAME/__init__.py
echo "app = Flask(__name__)" >> $APP_NAME/__init__.py
echo "app.config.from_pyfile('../application.cfg')" >> $APP_NAME/__init__.py
echo "" >> $APP_NAME/__init__.py
echo "@app.route('/')" >> $APP_NAME/__init__.py
echo "def index():" >> $APP_NAME/__init__.py
echo "    return 'Hello World!'" >> $APP_NAME/__init__.py

echo "from $APP_NAME import app" > run.py
echo "" >> run.py
echo "if __name__ == '__main__':" >> run.py
echo "    app.run()" >> run.py

echo "DEBUG=True" > application.cfg


exit 0
