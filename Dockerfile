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
ADD test.sh /myproject/test.sh
# Step 10 done
RUN git bisect start
# Step 11 done
RUN git bisect bad
# Step 12 done
RUN git checkout HEAD~1023
# Step 13 done
RUN git bisect good
# Step 14 done
RUN git bisect good
# Step 15 done
RUN git bisect bad
# Step 16 done
RUN git bisect bad
# Step 17 done
RUN git bisect bad
# Step 18 done
RUN git bisect bad
# Step 19 done
RUN git bisect bad
# Step 20 done
RUN git bisect bad
# Step 21 done
RUN git bisect bad
# Step 22 done
RUN git bisect bad
# Step 23 done
RUN git bisect good
# Step 24 done
CMD /bin/bash
# Step 25 done
