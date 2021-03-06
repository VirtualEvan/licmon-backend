# Builder image
FROM centos/python-38-centos7 AS backend-builder
USER root
COPY . .

RUN PYTHON=python3.8 make
RUN make build


# Production image
FROM centos/python-38-centos7
USER root

# Install lmutil dependencies
RUN set -ex && \
		yum install -y redhat-lsb && \
		yum clean all && rm -rf /var/cache/yum/

RUN pip install uwsgi ipython flask-shell-ipython httpie

# Copy the application
COPY --from=backend-builder /opt/app-root/src/dist/licmon*.whl /tmp/
RUN curl -SL https://www.plexim.com/sites/default/files/dstlm/flexnet_11_16_2_linux64.tar.gz | tar xvz -C /usr/local/bin
RUN pip install $(echo /tmp/licmon*.whl)
COPY uwsgi.ini .

USER default

ENV FLASK_ENV=production FLASK_APP=licmon.wsgi
CMD ["uwsgi", "--ini", "uwsgi.ini"]
EXPOSE 8080
