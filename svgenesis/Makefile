SHELL=bash
REMOVE_PATTERNS = *~\
		  *pyc \
		  build

SUBDIRS = templates \
	  composites \
	  geometry3d \
	  primitives \
	  maps \



.PHONY: all clean 

all: clean 

clean:
	@(for pat in $(REMOVE_PATTERNS); \
	do \
		rm -rfv $$pat ;\
	done;)

	@(for subdir in $(SUBDIRS); \
	do \
		make -C $$subdir clean ; \
	done;)
