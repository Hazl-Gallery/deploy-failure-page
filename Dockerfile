FROM nginx:alpine

RUN apk add --no-cache python3

COPY index.html /tmp/index.html
COPY process_template.py /usr/local/bin/process_template.py

EXPOSE 80

CMD sh -c 'python3 /usr/local/bin/process_template.py && nginx -g "daemon off;"'
