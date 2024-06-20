docker buildx create --use
docker buildx build --platform linux/amd64 --load -t architecture-app .
docker tag architecture-app foncheto/test-arqui  
docker push foncheto/test-arqui
