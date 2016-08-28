CC = arm-linux-gnueabi-gcc

hello : hello.c
	$(CC) -o hello hello.c -static
