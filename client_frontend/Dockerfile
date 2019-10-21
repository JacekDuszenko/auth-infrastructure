FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf
RUN rm -rf /usr/share/nginx/html/*

WORKDIR /usr/share/nginx/html
COPY dist/ .

RUN chown -R nginx:nginx /usr/share/nginx/html/*
RUN chmod -R 0755 /usr/share/nginx/html/*


CMD ["nginx", "-g", "daemon off;"]