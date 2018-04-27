MAIN_FILE = fruits-game.py

OUTPUTDIR = build
NUITKA_OPTS = \
	--output-dir=$(OUTPUTDIR) \
	--show-progress \
	--show-modules \
	--recurse-to=fruits \
	--recurse-dir=packages/fruits

NUITKA_BUILD_OPTS = \
	--lto \
	--warn-implicit-exceptions \
	--warn-unusual-code
NUITKA_DEBUG_OPTS = \
	--no-strip \
	--full-compat \
	--show-memory
NUITKA_FULL_BUILD_OPTS = \
	--python-flag="-O" \
	--recurse-on \
	--recurse-stdlib \
	--recurse-not-to=unittest \
	--recurse-not-to=pickle \
	--recurse-not-to=thread \
	--recurse-not-to=weakref \
	--recurse-not-to=queue \
	--recurse-not-to=pygame \
	--recurse-not-to=importlib \


mypy:
	mypy --strict --ignore-missing-imports $(shell find packages/fruits -type f | grep .py)
	mypy --strict --ignore-missing-imports $(shell find packages/fruitslib/ -type f | grep .py)


install:
	python3.6 setup.py install
	rm -rf dist

run:
	PYHTONPATH=packages python3.6 fruits-game.py

build:
	nuitka3 $(MAIN_FILE) $(NUITKA_OPTS) $(NUITKA_BUILD_OPTS)

debug:
	nuitka3 $(MAIN_FILE) $(NUITKA_OPTS) $(NUITKA_BUILD_OPTS) $(NUITKA_DEBUG_OPTS)

full-build:
	nuitka3 $(MAIN_FILE) $(NUITKA_OPTS) $(NUITKA_BUILD_OPTS) $(NUITKA_FULL_BUILD_OPTS)

clean:
	rm -rf $(OUTPUTDIR)
