if [ -z "${GITLAB_USERNAME}" ]; then
    echo "set GITLAB_USERNAME environment variable"
    exit 1
fi

if [ -z "${GITLAB_PASSWORD}" ]; then
    echo "set GITLAB_PASSWORD environment variable"
    exit 1
fi

docker login registry.gitlab.com --username $GITLAB_USERNAME --password $GITLAB_PASSWORD
IMG=registry.gitlab.com/jacekduszenko/teamprogramming2k19/client_backend
if [ -z "$1" ]; then
    echo "Tag not specified, building 1.0.0 and latest"
    TAG1=1.0.0
    TAG2=latest
    docker build --no-cache -t $IMG:$TAG1 -t $IMG:$TAG2 .
    docker push $IMG:$TAG1
    docker push $IMG:$TAG2
else
    TAG=$1
    echo "Building tag $TAG"
    docker build -t $IMG:$TAG .
    docker push $IMG:$TAG
fi

