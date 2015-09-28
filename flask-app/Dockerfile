FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y build-essential python python-dev python-setuptools supervisor
RUN easy_install pip
RUN pip install flask uwsgi kafka-python
ADD ./endpoint/app/*.py /srv/api/
ADD ./endpoint/config/supervisor.conf /etc/supervisor/conf.d/
EXPOSE 5000
CMD ["supervisord", "-n"]
#CMD /bin/bash
#CMD /usr/local/bin/uwsgi --http :5000 --wsgi-file /srv/api/endpoint.py