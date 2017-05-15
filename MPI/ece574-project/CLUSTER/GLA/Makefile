CC = mpicc
CFLAGS = -O2 -Wall -g
LFLAGS = -ljpeg -lm

all:   GLA_coarse GLA_fine

GLA_coarse:	GLA_coarse.o
		$(CC) -o GLA_coarse GLA_coarse.o $(LFLAGS)

GLA_coarse.o:	GLA_coarse.c
		$(CC) $(CFLAGS) -c GLA_coarse.c

GLA_fine:	GLA_fine.o
		$(CC) -o GLA_fine GLA_fine.o $(LFLAGS)

GLA_fine.o:	GLA_fine.c
		$(CC) $(CFLAGS) -c GLA_fine.c

clean:
	rm -f *~ *.o  GLA_coarse GLA_fine

submit:
	tar -czvf GLA_project.tar.gz Makefile README *.c
