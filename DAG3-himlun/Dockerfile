# # FROM ubuntu:trusty

# # RUN apt-get update && apt-get install -y stress && rm -rf /var/lib/apt/lists/*

# # # ENTRYPOINT ["/usr/bin/stress", "--verbose"]
# # # STRESS
# # # CMD []
# # # Stress with ARGS
# # CMD "stress --cpu 4 --timeout 10s"
# # Use the official Debian as a base image for both architectures
# # Use the official Debian as a base image for both architectures
# FROM debian:bullseye-slim

# # Install stress package and timeout command
# RUN apt-get update && apt-get install -y stress && rm -rf /var/lib/apt/lists/*

# # Set the default command to run when the container starts
# CMD [pwd]



FROM ubuntu:trusty

RUN apt-get update && apt-get install -y stress && rm -rf /var/lib/apt/lists/*

# Stress with ARGS
CMD ["/usr/bin/stress", "--cpu", "4", "--timeout", "10s"]
