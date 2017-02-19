docker-build:
	docker build . -t newmamka/server:latest
docker-run:
	-docker rm -f nmamka_run
	docker run --name nmamka_run -p 1337:8080 -v $(realpath ./):/usr/src/newmamka -d kmp_mamka/server
