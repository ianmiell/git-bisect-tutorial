FROM debian
# Step 2 done
RUN apt-get update && apt-get install -y git lsb-release vim bsdmainutils man-db manpages && git config --global user.email "you@example.com" && git config --global user.name "Your Name" && mkdir -p myproject && touch ~/.bash_history
# Step 3 done
WORKDIR /myproject
# Step 4 done
ADD build_history.sh /myproject/build_history.sh
# Step 5 done
RUN git init && echo 'git init' >> ~/.bash_history
# Step 6 done
RUN touch projectfile && echo 'touch projectfile' >> ~/.bash_history
# Step 7 done
RUN git add projectfile && echo 'git add projectfile' >> ~/.bash_history
# Step 8 done
RUN ./build_history.sh && echo './build_history.sh' >> ~/.bash_history
# Step 9 done
ADD test.sh /myproject/test.sh
# Step 10 done
RUN git bisect start && echo 'git bisect start' >> ~/.bash_history
# Step 11 done
RUN git bisect bad && echo 'git bisect bad' >> ~/.bash_history
# Step 12 done
RUN git checkout HEAD~1023 && echo 'git checkout HEAD~1023' >> ~/.bash_history
# Step 13 done
RUN git bisect good && echo 'git bisect good' >> ~/.bash_history
# Step 14 done
RUN git bisect good && echo 'git bisect good' >> ~/.bash_history
# Step 15 done
RUN git bisect bad && echo 'git bisect bad' >> ~/.bash_history
# Step 16 done
RUN git bisect bad && echo 'git bisect bad' >> ~/.bash_history
# Step 17 done
RUN git bisect bad && echo 'git bisect bad' >> ~/.bash_history
# Step 18 done
RUN git bisect bad && echo 'git bisect bad' >> ~/.bash_history
# Step 19 done
RUN git bisect bad && echo 'git bisect bad' >> ~/.bash_history
# Step 20 done
RUN git bisect bad && echo 'git bisect bad' >> ~/.bash_history
# Step 21 done
RUN git bisect bad && echo 'git bisect bad' >> ~/.bash_history
# Step 22 done
RUN git bisect bad && echo 'git bisect bad' >> ~/.bash_history
# Step 23 done
RUN git bisect good && echo 'git bisect good' >> ~/.bash_history
# Step 24 done
CMD /bin/bash
# Step 25 done
