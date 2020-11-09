# define the name of the virtual environment directory
app_name = todo_flask
VENV := .venv

# default target, when make executed without arguments
init: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

run: venv
	./$(VENV)/bin/python3 app.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

build:
    @docker build -t $(app_name) .

run:
    docker run --detach -p 5000:5000 $(app_name)

kill:
    @echo 'Killing container...'
    @docker ps | grep $(app_name) | awk '{print $$1}' | xargs docker

.PHONY: init venv run clean