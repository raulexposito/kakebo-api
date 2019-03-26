
# Dependencias

```
sudo apt install python3-pip python3-venv httpie -y
```

# Instalación de pyenv

https://github.com/pyenv/pyenv
https://github.com/pyenv/pyenv/wiki#suggested-build-environment

```
pyenv install 3.7.2
```

# Instalación de watchexec

https://github.com/watchexec/watchexec

# Primera vez que usamos el repo

```
pyenv local 3.7.2
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Cómo ejecutar

```
source venv/bin/activate
export FLASK_DEBUG=1
FLASK_APP=flaskr/kakebo.py flask run --host=0.0.0.0 --port=5005
```
```
http :5005
```

# Cómo lanzar tests

```
source venv/bin/activate
export PYTHONPATH=flaskr:tests
watchexec --exts py ./save_actions.sh
```

# Cobertura

```
coverage report
coverage html
```

# Formateo del fuente

```
yapf -pir flaskr tests
```

# Docker

```
docker build -t kakebo-api .
docker run --rm -p 5005:5005 \
	-v /home/kakebo/kakebo-api/datos/:/flaskr/datos/ \
	--name kakebo-api \
	kakebo-api
```
