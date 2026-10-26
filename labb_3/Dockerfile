FROM apache/spark:python3

USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends netcat-openbsd \
 && rm -rf /var/lib/apt/lists/* 
USER spark

WORKDIR /opt/spark/work-dir

