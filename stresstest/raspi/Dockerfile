FROM arm32v7/rc-buster
RUN apt update && apt install stress
ADD stress_raspi.sh /
CMD ./stress_raspi.sh
