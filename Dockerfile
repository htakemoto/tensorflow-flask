FROM tensorflow/tensorflow:1.1.0

# $ docker run -v $(pwd)/server:/app -it -p 5000:5000 tensorflow/tensorflow:1.1.0

# install flask
RUN pip install flask

# install packages used inside container (optional)
RUN apt-get update
RUN apt-get -y install zsh vim