CC = mpicc
CFLAGS = -O2 -Wall -g
LFLAGS = -ljpeg -lm

all:   BBPF_pi_coarse BBPF_pi_fine

BBPF_pi_coarse:	BBPF_pi_coarse.o
		$(CC) -o BBPF_pi_coarse BBPF_pi_coarse.o $(LFLAGS)

BBPF_pi_coarse.o:	BBPF_pi_coarse.c
		$(CC) $(CFLAGS) -c BBPF_pi_coarse.c

BBPF_pi_fine:	BBPF_pi_fine.o
		$(CC) -o BBPF_pi_fine BBPF_pi_fine.o $(LFLAGS)

BBPF_pi_fine.o:	BBPF_pi_fine.c
		$(CC) $(CFLAGS) -c BBPF_pi_fine.c

clean:
	rm -f *~ *.o BBPF_pi_coarse BBPF_pi_fine

submit:
	tar -czvf BBPF_pi_project.tar.gz Makefile README *.c
