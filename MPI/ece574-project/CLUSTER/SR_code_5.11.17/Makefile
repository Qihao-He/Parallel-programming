CC = mpicc
CFLAGS = -O2 -Wall -g
LFLAGS = -ljpeg -lm

all:   SR_serial SR_serial_fine	SR_mpi_before SR_mpi_coarse SR_mpi_fine

SR_serial:	SR_serial.o
		$(CC) -o SR_serial SR_serial.o $(LFLAGS)

SR_serial.o:	SR_serial.c
		$(CC) $(CFLAGS) -c SR_serial.c

SR_serial_fine:	SR_serial_fine.o
		$(CC) -o SR_serial_fine SR_serial_fine.o $(LFLAGS)

SR_serial_fine.o:	SR_serial_fine.c
		$(CC) $(CFLAGS) -c SR_serial_fine.c

SR_mpi_before:	SR_mpi_before.o
		$(CC) -o SR_mpi_before SR_mpi_before.o $(LFLAGS)

SR_mpi_before.o:	SR_mpi_before.c
		$(CC) $(CFLAGS) -c SR_mpi_before.c

SR_mpi_coarse:	SR_mpi_coarse.o
		$(CC) -o SR_mpi_coarse SR_mpi_coarse.o $(LFLAGS)

SR_mpi_coarse.o:	SR_mpi_coarse.c
		$(CC) $(CFLAGS) -c SR_mpi_coarse.c

SR_mpi_fine:	SR_mpi_fine.o
		$(CC) -o SR_mpi_fine SR_mpi_fine.o $(LFLAGS)

SR_mpi_fine.o:	SR_mpi_fine.c
		$(CC) $(CFLAGS) -c SR_mpi_fine.c

clean:
	rm -f *~ *.o SR_serial  SR_serial_fine SR_mpi_before SR_mpi_coarse SR_mpi_fine

submit:
	tar -czvf SR_project.tar.gz Makefile README *.c
