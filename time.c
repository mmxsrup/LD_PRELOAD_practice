// My time function

#include <stdio.h>
#include <time.h>
#include <sys/time.h>


#define ADD_SEC 3

time_t time(time_t *t) {
	struct timeval tv;
	time_t result;

	if (gettimeofday(&tv, (struct timezone*)NULL))
		result = (time_t)-1;
	else
		result = (time_t)(tv.tv_sec + ADD_SEC);

	if (t != NULL)
		*t = result;
	printf("now_time + 3	: %ld\n", result);
	return result;
}
