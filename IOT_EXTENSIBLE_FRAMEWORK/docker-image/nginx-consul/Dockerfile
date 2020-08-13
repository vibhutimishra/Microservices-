FROM nginx:1.12

RUN apt-get update -q && apt-get -y install curl

EXPOSE 80

RUN curl -L https://releases.hashicorp.com/consul-template/0.18.2/consul-template_0.18.2_linux_amd64.tgz | tar -C /usr/local/bin -zxf -

RUN mkdir /etc/consul-templates

COPY nginx.consul.tmpl /etc/consul-templates/nginx.conf
COPY index.html /usr/share/nginx/html/

RUN rm /etc/nginx/conf.d/*

CMD /usr/sbin/nginx -c /etc/nginx/nginx.conf && consul-template \
-consul-addr=$DOCKER_HOST:8500 -consul-token=$CONSUL_TOKEN \
-template "/etc/consul-templates/nginx.conf:/etc/nginx/conf.d/default.conf:/usr/sbin/nginx -s reload"