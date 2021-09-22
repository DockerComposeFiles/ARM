FROM arm32v7/debian:buster
RUN apt update && apt install stress
ADD stress_bbb.sh /
CMD ./stress_bbb.sh
