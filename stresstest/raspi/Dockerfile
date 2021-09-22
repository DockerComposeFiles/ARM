FROM arm32v7/debian
RUN apt update && apt install stress
ADD stress_raspi.sh /
CMD ./stress_raspi.sh
