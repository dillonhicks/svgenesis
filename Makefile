##################################################
# Makefile
##################################################
REMOVE_PATTERNS = *~\
		  *pyc \
		  build

SUBDIRS = svgenesis \
	  tests \
	  scripts \
	  docs

.PHONY: clean tests install all docs view-test

all:
	@echo 'Pick one of the following targets: ' 
	@echo '* tests'
	@echo '* install' 
	@echo '* install-local' 
	@echo '* clean'
	@echo '* docs'

tests:
	@make -C tests

install:
	python setup.py -v install

install-local:
	python setup.py -v install --prefix=$(HOME)

clean:
	@(for pat in $(REMOVE_PATTERNS); \
	do \
		rm -rfv $$pat ;\
	done;)
	@(for subdir in $(SUBDIRS); \
	do \
		make -C $$subdir clean; \
	done;)

view-tests: tests
	@firefox tests/test_out/*svg &

docs:
	make -C docs html
