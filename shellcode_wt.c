#include <stdio.h>
char *SC =  "\x01\x60\x8f\xe2"
            "\x16\xff\x2f\xe1"
            "\x10\x22"
            "\x79\x46"
            "\x0e\x31"
            "\x01\x20"
            "\x04\x27"
            "\x01\xdf"
            "\x24\x1b"
            "\x20\x1c"
            "\x01\x27"
            "\x01\xdf"
            "\x73\x68\x65\x6c"
            "\x6c\x2d\x73\x74"
            "\x6f\x72\x6d\x2e"
            "\x6f\x72\x67\x0a";

int main(void)
        {
                fprintf(stdout,"Length: %d\n",strlen(SC));
                (*(void(*)()) SC)();
        return 0;
        }
