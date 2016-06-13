SHELL := /bin/bash

export BASEDIR
BASEDIR := $(CURDIR)

all: help
.	: install uninstall test

#COLORS
GREEN  := $(shell tput -Txterm setaf 2)
WHITE  := $(shell tput -Txterm setaf 7)
YELLOW := $(shell tput -Txterm setaf 3)
RESET  := $(shell tput -Txterm sgr0)

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# A category can be added with @category
HELP_FUN = \
	%help; \
	while(<>) { push @{$$help{$$2 // 'options'}}, [$$1, $$3] if /^([a-zA-Z\-]+)\s*:.*\#\#(?:@([a-zA-Z\-]+))?\s(.*)$$/ }; \
	print "usage: make [target]\n\n"; \
	print "WP - Developer Tools\n\n"; \
	for (sort keys %help) { \
	print "${WHITE}$$_:${RESET}\n"; \
	for (@{$$help{$$_}}) { \
	$$sep = " " x (32 - length $$_->[0]); \
	print "  ${YELLOW}$$_->[0]${RESET}$$sep${GREEN}$$_->[1]${RESET}\n"; \
	}; \
	print "\n"; }

help: ##@other Lamento, não posso te ajudar mais que isso! =)
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

# cnab240
##
install: ##@cnab Instalar pacote CNAB240
	@echo 'Instalando pacote cnab240...'
	$(if $(shell pip freeze|grep cnab240), @echo 'O pacote já esta instalado!', @python setup.py install)
	@hash -r

uninstall: ##@cnab Desinstalar pacote CNAB240
	@echo 'Desinstalando pacote cnab240...'
	$(if $(shell pip freeze|grep cnab240), @pip uninstall -y cnab240==0.01, @echo 'O pacote já esta desinstalado!')
	@hash -r

clear: ##@cnab Remover as pastas; cnab240.egg-info, .tox, build e dist.
	@echo 'Wipeout...'
	@rm -rf cnab240.egg-info dist build .tox
	@hash -r

dev-requirements: ##@dev Instalar requirements_dev CNAB240
	@echo 'Instalando modelos dev...'
	$(if $(shell pip freeze|grep cnab240), @pip install -r requirements_dev.txt, @echo 'O pacotes já estão desinstalado!')
	@hash -r

tox-them-all: ##@dev tox - Rodar todos os testes para o pacote CNAB240
	@echo 'tox, testando...'
	$(if $(shell pip freeze|grep tox), @tox, @pip install tox)

unittest-them-all: ##@dev unittest - Rodar todos os testes para o pacote CNAB240
	@echo 'WOW, testando!!!'
	@python -m unittest discover || unit2 discover

check-root:
	@export USER=`whoami`
	@if [ "$(USER)" != "root" ] ; then \
		echo "Hey fellow user, try again using sudo!" ; \
		exit 1; \
	else \
		echo "Hey ho let's go..."; \
	fi

%:
	@:
