.DEFAULT_GOAL := help

CC = gcc
F90 = gfortran
PYTHON = python

FPP = gfortran -E
FPP_F90FLAGS = -x f95-cpp-input -fPIC
F90FLAGS = -fPIC
FCOMP = gfortran

CFLAGS = -fPIC

ifeq (${UNAME}, Darwin)
  LIBTOOL = libtool -static -o
else
  LIBTOOL = ar src
endif

PYTHON_MODULE_NAME = test_scm
# mapping between Fortran and C types
KIND_MAP = kind_map

# names (without suffix), f90 sources
LIBSRC_SOURCES = parameters datatypes library

# file names
LIBSRC_FILES = $(addsuffix .f90, ${LIBSRC_SOURCES})

# object files
LIBSRC_OBJECTS = $(addsuffix .o, ${LIBSRC_SOURCES})

# only used when cleaning up
LIBSRC_FPP_FILES = $(addsuffix .fpp, ${LIBSRC_SOURCES})

# source files that require a Python interface

# names (without suffix), f90 sources
LIBSRC_WRAP_SOURCES = datatypes library

# file names
LIBSRC_WRAP_FILES = $(addsuffix .f90, ${LIBSRC_WRAP_SOURCES})

# object files
LIBSRC_WRAP_OBJECTS = $(addsuffix .o, ${LIBSRC_WRAP_SOURCES})

# fpp files
LIBSRC_WRAP_FPP_FILES = $(addsuffix .fpp, ${LIBSRC_WRAP_SOURCES})

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

.PHONY: help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: all
all: _${PYTHON_MODULE_NAME}.cpython-37m-darwin.so _${PYTHON_MODULE_NAME}_pkg.cpython-37m-darwin.so

.PHONY: clean
clean:
	-rm \
		${LIBSRC_OBJECTS} \
		${LIBSRC_FPP_FILES} \
		libsrc.a \
		_${PYTHON_MODULE_NAME}.so \
		_${PYTHON_MODULE_NAME}_pkg.so \
		*.mod \
		*.fpp \
		f90wrap*.f90 \
		f90wrap*.o \
		*.o

%.o: %.f90
	${F90} ${F90FLAGS} -c $< -o $@

%.o: %.c
	${CC} ${CFLAGS} -c $< -o $@

%.fpp: %.f90
	${FPP} ${FPP_F90FLAGS} $< -o $@

libsrc.a: ${LIBSRC_OBJECTS}
	${LIBTOOL} $@ $?

_${PYTHON_MODULE_NAME}.cpython-37m-darwin.so: libsrc.a ${LIBSRC_FPP_FILES}
	f90wrap \
		-m ${PYTHON_MODULE_NAME} \
		${LIBSRC_WRAP_FPP_FILES} \
		-k ${KIND_MAP} \
		-v
	f2py-f90wrap \
		--fcompiler=$(FCOMP) \
		--build-dir . \
		-c \
		-m _${PYTHON_MODULE_NAME} \
		-L. -lsrc \
		f90wrap*.f90


_${PYTHON_MODULE_NAME}_pkg.cpython-37m-darwin.so: libsrc.a ${LIBSRC_FPP_FILES}
	f90wrap \
		-m ${PYTHON_MODULE_NAME}_pkg \
		${LIBSRC_WRAP_FPP_FILES} \
		-k ${KIND_MAP} \
		-v \
		-P
	f2py-f90wrap \
		--fcompiler=$(FCOMP) \
		--build-dir . \
		-c \
		-m _${PYTHON_MODULE_NAME}_pkg \
		-L. -lsrc \
		f90wrap*.f90

test: all
	pytest test.py -v
