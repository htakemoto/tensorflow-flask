# TensorFlow and Flask

TensorFlow and Flask

## ToDo

Create your image

``` bash
$ docker build -t $USER/tensorflow-flask .
```

Run the image

``` bash
$ docker run -v $(pwd)/server:/app --workdir /app -p 5000:5000 -it $USER/tensorflow-flask bash
```

Run server

``` bash
$ python hello.py
```