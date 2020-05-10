FROM python:3.7.7-alpine3.10

WORKDIR /usr/src/myapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copies all files from curr directory (source) to destination
COPY . .

# our service will listen on port 5000 - specified in app.py
EXPOSE 5000

# execute app.py using python3 (command, argument)
CMD ["python3","app.py"]