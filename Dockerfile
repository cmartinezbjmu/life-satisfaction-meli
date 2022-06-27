FROM python:3.8-alpine

RUN pip install --upgrade pip

RUN apk --update add gcc build-base freetype-dev libpng-dev openblas-dev

RUN pip install --no-cache-dir matplotlib pandas

# Generate requirements.txt file
RUN pip install pipenv
COPY Pipfile* /
RUN pipenv run pip freeze > requirements.txt

# Copy project's files
COPY . /
# Change directory to roles_ms
COPY ./static/* /static
RUN chmod +x /static/*
RUN chmod -R 755 requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR /app

# Creates a new user (best practices)
RUN adduser -D appUser
RUN chown -R appUser:appUser /app
RUN chmod -R 755 /app

# Switch to created user
USER appUser