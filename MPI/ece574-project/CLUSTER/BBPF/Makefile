CC = mpicc
CFLAGS = -O2 -Wall -g
LFLAGS = -ljpeg -lm

all:   BBPF_coarse BBPF_fine

BBPF_coarse:	BBPF_coarse.o
		$(CC) -o BBPF_coarse BBPF_coarse.o $(LFLAGS)

BBPF_coarse.o:	BBPF_coarse.c
		$(CC) $(CFLAGS) -c BBPF_coarse.c

BBPF_fine:	BBPF_fine.o
		$(CC) -o BBPF_fine BBPF_fine.o $(LFLAGS)

BBPF_fine.o:	BBPF_fine.c
		$(CC) $(CFLAGS) -c BBPF_fine.c

clean:
	rm -f *~ *.o BBPF_coarse BBPF_fine

submit:
	tar -czvf BBPF_project.tar.gz Makefile README *.c
