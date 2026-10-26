# Dockerfile.streaming
FROM apache/spark:python3

# Install netcat (nc) as root, then switch back to the normal spark user
USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends netcat-openbsd \
 && rm -rf /var/lib/apt/lists/* 
# && mkdir -p /opt/csv_output_directory && mkdir -p /opt/checkpoint_directory \
# && sudo chown -R spark /opt/csv_output_directory && sudo chown -R spark /opt/checkpoint_directory
USER spark

WORKDIR /opt/spark/work-dir

