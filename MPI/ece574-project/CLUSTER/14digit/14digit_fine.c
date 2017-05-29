/* Auther: Qihao He <qi.he@maine.edu> */
/* This program uses Bailey–Borwein–Plouffe formula(BBPF) to compute PI, it fits
 very well with the hexadecimal. It has the time-complexity of O(n^2). It would
be a big problem set that exceeded the Gauss–Legendre algorithm's
time-complexity. If it use hexadecimal and implement with Gauss–Legendre
algorithm and then transform back to decimal, it would be a waste of time, for
that the transform speed is way slower than the computation speed. Luckily, it
is easy to implement BBPF in a parallel computation, it is easy to fully utilize
 4 cores of CPU. */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <errno.h>
#include <math.h>
#include <mpi.h>

// #define epsilon 1e-15//epsilon

/* True value of Pi from Wolframalpha www.wolframalpha.com */
// Digits after decimal are 1000.
#define truepivalue 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230825334468503526193118817101000313783875288658753320838142061717766914730359825349042875546873115956286388235378759375195778185778053217122680661300192787661119590921642019893
double concolve(int rank,int start,int end){
	double x,y;
	double temp1,temp2;
	double area=0;
	int i;

	for(i=start;i<=end;i++){
		x=(double)(2*i-1)/(double)n;
		temp1= 4.0/(1.0+x*x);
		y=(double)(2*i)/(double)n;
		temp2= 4.0/(1.0+y*y);
		area+= 4.0*temp1+2*temp2;
	}
	printf("Rank%d range from %d to %d,area:%f\n",rank,start,end,area);
	return area;
}

int main(int argc, char *argv[]) {

	double sum=0;
	double total_sum=0;
	double Rerror;//Relative error
	double error;
	int result;
	double temp1,temp2;

	/* measure time */
	double start_time,convolve_start,convolve_end,reduce_start,reduce_end;
	int numtasks,rank;//# of tasks, rank index

	/* Initialize MPI */
	result = MPI_Init(&argc,&argv);
	if (result != MPI_SUCCESS) {
		printf ("Error starting MPI program!.\n");
		MPI_Abort(MPI_COMM_WORLD, result);
	}

	/* Calls MPI_wtime() to get the wallclock times for Load, Convolve, Combine,
	and Store like we did with PAPI in the OpenMP code. You only need to record
	and print these from rank 0. */
	start_time=MPI_Wtime();

	/* Get number of tasks and our process number (rank) */
	MPI_Comm_size(MPI_COMM_WORLD,&numtasks);//number os tasks
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);

	convolve_start=MPI_Wtime();
	/* Only on rank 0 */
	if(rank==0){
		temp1=(double)0/(double)n;
		temp2=(double)n/(double)n;
		total_sum=4.0/(1+temp1*temp1)-4.0/(1+temp2*temp2);
		printf("Rank%d,total_sum:%f\n",rank,total_sum);
	}

	sum=convolve(rank,rank*n/2/numtasks+1,(rank+1)*n/2/numtasks);
	convolve_end=MPI_Wtime();

	MPI_Barrier(MPI_COMM_WORLD);

	reduce_start=MPI_Wtime();
	/* MPI_reduce */
	MPI_Reduce(&sum,	/* send data */
		&total_sum,	/* receive data */
		1,		/* count */
		MPI_DOUBLE,	/* type */
		MPI_SUM,	/* reduce type */
		0,		/* root */
		MPI_COMM_WORLD);

	if(rank==0){
		total_sum/=(3.0*n);
	}
	reduce_end=MPI_Wtime();

	/* print result on rank 0 */
	if(rank==0){
		printf("Rank%d:\nAppr pi: %13.15f\n",rank,total_sum);
		printf("True pi: %13.15f\n",truepivalue);//true value of pi
		printf("Epsilon: %1.15f\n",epsilon);//epsilon

		/* Relative error in epsilon */
		// printf("epsilon is: %f\n",(double)epsilon);
		// Rerror=abs(total_sum-(double)truepivalue)/(double)epsilon;
		// error=abs(total_sum-(double)truepivalue);
		// printf("Relative error in epsilon is: %f\n",Rerror);
		// printf("error is: %f\n",error);

		printf("Load time: %lf\n",convolve_start-start_time);
		printf("Convolve time: %lf\n",convolve_end-convolve_start);
		printf("Reduce time: %lf\n",reduce_end-reduce_start);
		printf("Total time = %lf\n",reduce_end-start_time);
	}

	/* MPI_Finalize at the end */
	MPI_Finalize();
	return 0;
}
