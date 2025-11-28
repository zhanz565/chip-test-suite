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

      tests:
        test_spec.et: |
          test "test_addition" {
              expect add(2, 3) == 5;
          }

          test "test_blink_stub" {
              expect blink_stub(3) == 1;
              expect blink_stub(0) == 0;
          }

          test "test_max_int" {
              expect max_int(3, 7) == 7;
              expect max_int(10, -5) == 10;
              expect max_int(0, 0) == 0;
          }
