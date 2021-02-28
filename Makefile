PYTHON ?= python3.8
FLASK_HOST ?= 127.0.0.1
FLASK_PORT ?= 5000
VENV ?= .venv

FLASK := ${VENV}/bin/flask

.PHONY: flask-server
flask-server:
	@printf "  \033[38;5;154mRUN\033[0m  \033[38;5;75mRunning Flask dev server [\033[38;5;81m${FLASK_HOST}\033[38;5;75m:\033[38;5;81m${FLASK_PORT}\033[38;5;75m]\033[0m\n"
	@${FLASK} run -h ${FLASK_HOST} -p ${FLASK_PORT} --extra-files $(abspath licmon.cfg):$(abspath servers.cfg)