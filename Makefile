lock:
	pipenv lock

install:
	pipenv install

build:
	docker build -t csirl-api .

run: build
	docker run -p 5000:5000 csirl-api
