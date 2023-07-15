# re-implementation of rand() and srand() as provided by glibc

# shortened excerpt from glibc: stdlib/random_r.c
# int __random_r (struct random_data *buf, int32_t *result){
#  int32_t *state;
#
#  state = buf->state;
#
#  if (buf->rand_type == TYPE_0){
#      int32_t val = ((state[0] * 1103515245U) + 12345U) & 0x7fffffff;
#      state[0] = val;
#      *result = val;
#  }
#  ...
# }
#
#
# To get the same behavior in c, you have to run the following initialization
#   int seed = 1;
#   char state[8];
#   initstate(seed, state, 8); //switches to TYPE_0 rng and seets the seed
#   rand()

RAND_MAX = 2147483647

_next = 1


def rand():
    global _next
    _next = ((_next * 1103515245) + 12345) & 0x7fffffff
    return _next


def srand(seed):
    global _next
    _next = seed & 0x7fffffff
