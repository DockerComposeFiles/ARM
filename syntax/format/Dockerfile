FROM alpine:latest AS new_base
# TODO with --no-cache
FROM new_base
# Do next


# ENTRYPOINT [“executable”, “param1”, “param2”, ..]
# run Container endless
ENTRYPOINT ["tail", "-f", "/dev/null"]
# default Entrypoint
ENTRYPOINT ["/bin/sh", "-c"]


# run one bash script
ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

# run one python script
CMD ["python" ,"./script.py" ]
# run one python 3 script
CMD ["python3" ,"./script.py" ]

# run one java script
