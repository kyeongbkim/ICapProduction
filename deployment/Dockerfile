FROM nvidia/cuda:11.7.0-runtime-ubuntu22.04

WORKDIR flask

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda2-4.5.11-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    /opt/conda/bin/conda create --name python-3.9.12 python=3.9.12 && \
    echo "conda activate python-3.9.12" >> ~/.bashrc

RUN apt-get install -y vim

COPY requirements.txt /tmp/requirements.txt
COPY docker-install.sh /tmp/docker-install.sh
RUN  chmod 755 /tmp/docker-install.sh && /tmp/docker-install.sh
RUN  rm -f /tmp/requirements.txt /tmp/docker-install.sh

CMD [ "/bin/sh", "docker-entry.sh" ]
