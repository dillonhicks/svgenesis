####################################################
# Makefile
#
#
# This Makefile provides a way of easily executing all tests within
# the svgenesis tests suite.
####################################################

SHELL=/bin/bash

TEST_MODULES =  primitivestest.py \
		compositestest.py \
		svgtests.py

REMOVE_PATTERNS = *~\
		  *pyc \
		  build \
		  test_out

SUBDIRS =

tests:
	@(for test in $(TEST_MODULES); \
	do\
		./$$test -v; \
	done;)

clean:
	@(for pat in $(REMOVE_PATTERNS); \
	do \
		rm -rfv $$pat ;\
	done;)
	@(for subdir in $(SUBDIRS); \
	do \
		make -C $$subdir clean; \
	done;)


