MAIN_FILE = fruits-game.py

OUTPUTDIR = build
NUITKA_OPTS = \
	--standalone \
	--output-dir=$(OUTPUTDIR) \
	--show-progress \
	--show-modules

NUITKA_BUILD_OPTS = \
	--lto \
	--warn-implicit-exceptions \
	--warn-unusual-code
NUITKA_DEBUG_OPTS = \
	--no-strip \
	--full-compat \
	--show-memory
NUITKA_FULL_BUILD_OPTS = \
	--nofreeze-stdlib \
	--python-flag="-O" \
	--recurse-on \
	--recurse-stdlib \
	--recurse-not-to=unittest

mypy:
	mypy --strict --ignore-missing-imports $(shell find packages/fruits -type f | grep .py)
	mypy --strict --ignore-missing-imports $(shell find packages/fruitslib/ -type f | grep .py)

test:
	pytest

install:
	python3.6 setup.py install
	rm -rf dist

build:
	nuitka $(MAIN_FILE) $(NUITKA_OPTS) $(NUITKA_BUILD_OPTS)

debug:
	nuitka $(MAIN_FILE) $(NUITKA_OPTS) $(NUITKA_BUILD_OPTS) $(NUITKA_DEBUG_OPTS)

full-build:
	nuitka $(MAIN_FILE) $(NUITKA_OPTS) $(NUITKA_BUILD_OPTS) $(NUITKA_FULL_BUILD_OPTS)

clean:
	rm -rf $(OUTPUTDIR)
