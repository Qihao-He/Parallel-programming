CC = mpicc
CFLAGS = -O2 -Wall -g
LFLAGS = -ljpeg -lm

all:   14digit_coarse 
	# 14digit_fine

14digit_coarse:	14digit_coarse.o
		$(CC) -o 14digit_coarse 14digit_coarse.o $(LFLAGS)

14digit_coarse.o:	14digit_coarse.c
		$(CC) $(CFLAGS) -c 14digit_coarse.c

14digit_fine:	14digit_fine.o
		$(CC) -o 14digit_fine 14digit_fine.o $(LFLAGS)

14digit_fine.o:	14digit_fine.c
		$(CC) $(CFLAGS) -c 14digit_fine.c

clean:
	rm -f *~ *.o 14digit_coarse 14digit_fine

submit:
	tar -czvf BBPF_project.tar.gz Makefile README *.c
