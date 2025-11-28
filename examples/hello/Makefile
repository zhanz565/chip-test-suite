# Simple Makefile for Example Project

CC = gcc
CFLAGS = -Wall -Wextra

SRC = src/main.c
OUT = build/demo.out

all: $(OUT)

$(OUT):
	mkdir -p build
	$(CC) $(CFLAGS) $(SRC) -o $(OUT)

clean:
	rm -rf build