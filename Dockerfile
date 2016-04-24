FROM debian
# Step 2 done
RUN apt-get update && apt-get install -y git lsb-release vim bsdmainutils man-db manpages && git config --global user.email "you@example.com" && git config --global user.name "Your Name" && mkdir -p myproject
# Step 3 done
WORKDIR /myproject
# Step 4 done
ADD build_history.sh /myproject/build_history.sh
# Step 5 done
RUN git init
# Step 6 done
RUN touch projectfile
# Step 7 done
RUN git add projectfile
# Step 8 done
RUN ./build_history.sh
# Step 9 done
CMD /bin/bash
# Step 10 done
