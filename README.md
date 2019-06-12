
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

# Formateo del fuente

```
yapf -pir flaskr
```

# Analizar el fuente

```
flake8 flaskr
```

# Docker

```
docker build -t kakebo_backend .
docker run --rm -p 5005:5005 \
	-v /home/kakebo/movimientos/:/flaskr/datos/ \
	--name kakebo-backend \
	kakebo_backend
```

```
docker-compose stop && docker system prune -f && docker-compose pull --ignore-pull-failures && docker-compose up --build -d && docker-compose logs -f
```

# URLs de interés

- https://flaticons.net/
- http://www.htaccesstools.com/htpasswd-generator/
