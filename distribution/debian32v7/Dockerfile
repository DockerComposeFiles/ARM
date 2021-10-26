FROM arm32v7/debian

RUN apt update \
    && apt upgrade -y \
    && apt install nano -y \
    && apt clean

# Standard Entrypoint in Debian
ENTRYPOINT ["/bin/sh", "-c"]