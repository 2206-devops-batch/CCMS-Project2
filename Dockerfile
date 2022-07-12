
# Pull an official base image
FROM python:3.10.5-slim-bullseye

# Setting work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy src files
COPY . .

# Run Server
RUN export FLASK_APP=app.py
RUN export FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]