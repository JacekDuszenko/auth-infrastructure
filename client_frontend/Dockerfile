FROM nginx:alpine

COPY nginx/default.conf /etc/nginx/conf.d

RUN rm -rf /usr/share/nginx/html/*

WORKDIR /usr/share/nginx/html

COPY dist/client/ .

CMD ["nginx", "-g", "daemon off;"]