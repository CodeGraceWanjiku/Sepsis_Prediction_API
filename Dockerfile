# set up base image
FROM python:3.10.9

# create a working directory
WORKDIR /app

# copy the contents of the requirements into a temp folder in a container
COPY requirements.txt /tmp/requirements.txt

# install packages in the requirements.txt
RUN python -m pip install --timeout 300000 -r /tmp/requirements.txt

# copy all apps and folders into the container's working directory
COPY . /app

# expose port 8077 outside the container
EXPOSE 8077


# run the fastapi
CMD ['uvicorn','main:app','--host','0.0.0.0','--port',8077]
