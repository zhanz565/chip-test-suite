#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int blink_stub(int times) {
    return times > 0 ? 1 : 0;
}

int max_int(int a, int b) {
    return (a > b) ? a : b;
}

int main(void) {
    printf("Hello from ES-TDK Demo!\n");
    return 0;
}
