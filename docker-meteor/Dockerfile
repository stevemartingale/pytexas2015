FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y supervisor curl language-pack-en
RUN curl https://install.meteor.com/ | sh
RUN /bin/sh -c "echo -e 'LANG=en_US.UTF-8\nLC_ALL=en_US.UTF-8' > /etc/default/locale" #https://github.com/meteor/meteor/issues/4019
ADD ./dashboard /srv/dashboard
CMD ["supervisord", "-n"]