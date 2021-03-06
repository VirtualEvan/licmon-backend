PYTHON ?= python3.8
FLASK_HOST ?= 127.0.0.1
FLASK_PORT ?= 5000
VENV ?= .venv

SHELL := /bin/bash
PIP := ${VENV}/bin/pip
FLASK := ${VENV}/bin/flask
CONFIG := licmon/licmon.cfg

.PHONY: all
all: ${VENV} ${NODE_MODULES_GLOBAL} ${NODE_MODULES_CLIENT} config
	@printf "\033[38;5;154mSETUP\033[0m  \033[38;5;105mInstalling licmon python package\033[0m\n"
	@${PIP} install -q -e '.[dev]'

${VENV}:
	@printf "\033[38;5;154mSETUP\033[0m  \033[38;5;105mCreating virtualenv\033[0m\n"
ifeq (, $(shell which ${PYTHON} 2> /dev/null))
	@printf "\033[38;5;220mFATAL\033[0m  \033[38;5;196mPython not found (${PYTHON})\033[0m\n"
	@exit 1
endif
ifneq (True, $(shell ${PYTHON} -c 'import sys; print(sys.version_info[:2] >= (3, 7))'))
	@printf "\033[38;5;220mFATAL\033[0m  \033[38;5;196mYou need at least Python 3.7\033[0m\n"
	@exit 1
endif
	@${PYTHON} -m venv --prompt licmon .venv
	@${PIP} install -q -U pip setuptools


${CONFIG}: | ${CONFIG}.example
	@printf "\033[38;5;154mSETUP\033[0m  \033[38;5;105mCreating config [\033[38;5;147m${CONFIG}\033[38;5;105m]\033[0m\n"
	@cp ${CONFIG}.example ${CONFIG}
	@sed -i.bak "s/^SECRET_KEY = None/SECRET_KEY = '$$(LC_ALL=C tr -dc A-Za-z0-9 < /dev/urandom | head -c 32)'/" ${CONFIG}
	@sed -i.bak "s/^SKIP_LOGIN = False/SKIP_LOGIN = True/" ${CONFIG}
	@sed -i.bak "s/^EMAIL_BACKEND = '[^']\+'/EMAIL_BACKEND = 'licmon.vendor.django_mail.backends.console.EmailBackend'/" ${CONFIG}
	@rm -f ${CONFIG}.bak
	@printf "       \033[38;5;82mDon't forget to update the config file if needed!\033[0m\n"


.PHONY: flask-server
flask-server:
	@printf "  \033[38;5;154mRUN\033[0m  \033[38;5;75mRunning Flask dev server [\033[38;5;81m${FLASK_HOST}\033[38;5;75m:\033[38;5;81m${FLASK_PORT}\033[38;5;75m]\033[0m\n"
	@${FLASK} run -h ${FLASK_HOST} -p ${FLASK_PORT} --extra-files $(abspath licmon/licmon.cfg):$(abspath licmon/servers.cfg)


.PHONY: build
build:
	@printf "  \033[38;5;154mBUILD\033[0m  \033[38;5;176mBuilding production package\033[0m\n"
	# @rm -rf newdle/client/build build
	# @source ${VENV}/bin/activate && cd newdle/client && npm run build
	@source ${VENV}/bin/activate
	@${PIP} list
	@python setup.py bdist_wheel -q


.PHONY: config
config: ${CONFIG}