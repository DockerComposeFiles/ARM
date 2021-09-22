FROM arm32v7/debian
RUN apt update && apt install stress
ADD stress_bbb.sh /
CMD ./stress_bbb.sh
