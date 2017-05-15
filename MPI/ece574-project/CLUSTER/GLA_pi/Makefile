CC = mpicc
CFLAGS = -O2 -Wall -g
LFLAGS = -ljpeg -lm

all:   BBPF_pi GLA_pi_coarse GLA_pi_fine

BBPF_pi:	BBPF_pi.o
		$(CC) -o BBPF_pi BBPF_pi.o $(LFLAGS)

BBPF_pi.o:	BBPF_pi.c
		$(CC) $(CFLAGS) -c BBPF_pi.c

GLA_pi_coarse:	GLA_pi_coarse.o
		$(CC) -o GLA_pi_coarse GLA_pi_coarse.o $(LFLAGS)

GLA_pi_coarse.o:	GLA_pi_coarse.c
		$(CC) $(CFLAGS) -c GLA_pi_coarse.c

GLA_pi_fine:	GLA_pi_fine.o
		$(CC) -o GLA_pi_fine GLA_pi_fine.o $(LFLAGS)

GLA_pi_fine.o:	GLA_pi_fine.c
		$(CC) $(CFLAGS) -c GLA_pi_fine.c

clean:
	rm -f *~ *.o BBPF_pi GLA_pi_coarse GLA_pi_fine

submit:
	tar -czvf GLA_pi_project.tar.gz Makefile README *.c
