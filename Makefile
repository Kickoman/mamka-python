docker-build:
	docker build . -t newmamka/server:latest
docker-run:
	-docker rm -f nmamka_run
	docker run --name nmamka_run -p 8080:1337 -v $(realpath ./www):/usr/src/newmamka -d newmamka/server
