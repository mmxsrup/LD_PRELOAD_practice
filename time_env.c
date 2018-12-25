#include <stdlib.h>
#include <time.h>

time_t time(time_t *tloc) {
    return atoll(getenv("TIME"));
}
