all:
	gcc -m32 -fno-stack-protector -o foo foo.c
clean:
	rm -f foo
