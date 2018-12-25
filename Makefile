CXX = gcc
CFLAGS = -std=c99 -Wall
CFLAGS_SHARED = -fPIC -shared

all: challenge libtime.so libtime_env.so
	# LD_PRELOAD=./libtime.so ./challenge

challenge: challenge.o
	$(CXX) $(CFLAGS) -o challenge challenge.o

libtime.so: time.c
	$(CXX) $(CFLAGS) $(CFLAGS_SHARED) -o libtime.so time.c

libtime_env.so: time_env.c
	$(CXX) $(CFLAGS) $(CFLAGS_SHARED) -o libtime_env.so time_env.c

clean: 
	rm -f *.o challenge libtime.so
