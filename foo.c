#include <stdio.h>
#include <unistd.h>

int main(void) {
	char buf[32];

	seteuid(getuid());

	gets(buf);

	return ( 0 );
}
