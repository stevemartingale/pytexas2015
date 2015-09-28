FROM ubuntu:14.04
RUN apt-get -qq update
RUN apt-get upgrade -y
RUN apt-get install -y openjdk-7-jre-headless python-pip python-dev build-essential wget supervisor
RUN pip install streamparse pymongo kafka-python
RUN /usr/bin/wget -q https://github.com/technomancy/leiningen/raw/stable/bin/lein -O /usr/bin/lein
RUN /bin/chmod 755 /usr/bin/lein 
ADD toycount /srv/toycount-topology
ADD supervisor.conf /etc/supervisor/conf.d/
CMD ["supervisord", "-n"]
