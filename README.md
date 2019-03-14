
# Dependencias

```
sudo apt install python3-pip python3-venv httpie jq -y
```

# Instalación de pyenv

https://github.com/pyenv/pyenv
https://github.com/pyenv/pyenv/wiki#suggested-build-environment

```
pyenv install 3.7.2
```

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
FLASK_APP=flaskr/kakebo.py flask run
```
```
http :5000 | jq
```

# Cómo lanzar tests

```
source venv/bin/activate
export PYTHONPATH=flaskr:tests
watchexec --exts py ./save_actions.sh
```

## Cobertura

```
coverage report
coverage html
```

# Docker

```
docker build -t kakebo-api .
docker run --rm -p 5000:5000 kakebo-api
```
