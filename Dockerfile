FROM scratch
ADD rootfs.tar.xz /
CMD ["bash"]

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

COPY src/sample.py  /app

CMD [ "python", "sample.py" ]