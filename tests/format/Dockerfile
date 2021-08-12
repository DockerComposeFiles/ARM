# ENTRYPOINT [“executable”, “param1”, “param2”, ..]

# run Container endless
ENTRYPOINT ["tail", "-f", "/dev/null"]

# default Entrypoint
ENTRYPOINT ["/bin/sh", "-c"]

# run one bash script
ADD entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

# run one python 3 script
CMD ["python3" ,"./script.py" ]

# run one java script
