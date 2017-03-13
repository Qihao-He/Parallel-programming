Author:Qihao He
Diary of process of raspberry pi study in GPU:
________________________________________________________________________________
2/20/2017
run hello-fft

follow blog:
ACCELERATING FOURIER TRANSFORMS USING THE GPU
https://www.raspberrypi.org/blog/accelerating-fourier-transforms-using-the-gpu/

To get GPU_FFT enter the following at the command prompt:
sudo rpi-update && sudo reboot
To build and run the example program:
cd /opt/vc/src/hello_pi/hello_fft
make
sudo mknod char_dev c 100 0
sudo ./hello_fft.bin
API documentation can be found in the hello_fft folder.
________________________________________________________________________________
3/4/2017
8:24pm
ESCI 386 – Scientific Programming, Analysis and Visualization with Python
Lesson 17 - Fourier Transforms
numpy:
http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson17-Fourier-Transforms.pdf

8:50pm
GPGPU HACKING ON THE PI
https://www.raspberrypi.org/blog/gpgpu-hacking-on-the-pi/

9:21pm
A BIRTHDAY PRESENT FROM BROADCOM
https://www.raspberrypi.org/blog/a-birthday-present-from-broadcom/

9:23pm
Need to install Ubuntu on Surface for dual boot.
________________________________________________________________________________
3/5/1017
2:50pm
Install Ubuntu on Surface failed at shrinking size of the disk.
Rerun:
cd /opt/vc/src/hello_pi/hello_fft
make
sudo mknod char_dev c 100 0
sudo ./hello_fft.bin
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8
rel_rms_err = 3.3e-07, usecs = 45, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 22
rel_rms_err = 1.5e-06, usecs = 782379, k = 0

3:30pm
Figuring out how to use the ./hello_fft.bin
Usage: hello_fft.bin log2_N [jobs [loops]]
log2_N = log2(FFT_length),       log2_N = 8...22
jobs   = transforms per batch,   jobs>0,        default 1
loops  = number of test repeats, loops>0,       default 1

Running the hello_fft.bin for the GPU limit processing data, which exploits the
BCM2835 SoC 3D hardware.

pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 1 1
rel_rms_err = 3.3e-07, usecs = 44, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 2 1
rel_rms_err = 3.1e-07, usecs = 30, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 4 1
rel_rms_err = 2.8e-07, usecs = 22, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 8 1
rel_rms_err = 2.7e-07, usecs = 19, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 16 1
rel_rms_err = 2.6e-07, usecs = 28, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 32 1
rel_rms_err = 2.6e-07, usecs = 17, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 64 1
rel_rms_err = 2.5e-07, usecs = 16, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 16 1
rel_rms_err = 2.6e-07, usecs = 17, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 128 1
rel_rms_err = 0.062, usecs = 17, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 256 1
rel_rms_err = 0.062, usecs = 16, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 512 1
rel_rms_err = 0.71, usecs = 15, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 1024 1
rel_rms_err = 0.94, usecs = 15, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 2048 1
rel_rms_err = 1, usecs = 15, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 4096 1
rel_rms_err = 1.1, usecs = 15, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 8192 1
rel_rms_err = 1.1, usecs = 15, k = 0

pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 1 4
rel_rms_err = 3.3e-07, usecs = 44, k = 0
rel_rms_err = 3.3e-07, usecs = 31, k = 1
rel_rms_err = 3.3e-07, usecs = 31, k = 2
rel_rms_err = 3.3e-07, usecs = 31, k = 3
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 1 8
rel_rms_err = 3.3e-07, usecs = 51, k = 0
rel_rms_err = 3.3e-07, usecs = 31, k = 1
rel_rms_err = 3.3e-07, usecs = 32, k = 2
rel_rms_err = 3.3e-07, usecs = 32, k = 3
rel_rms_err = 3.3e-07, usecs = 32, k = 4
rel_rms_err = 3.3e-07, usecs = 33, k = 5
rel_rms_err = 3.3e-07, usecs = 31, k = 6
rel_rms_err = 3.3e-07, usecs = 31, k = 7
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 1 16
rel_rms_err = 3.3e-07, usecs = 43, k = 0
rel_rms_err = 3.3e-07, usecs = 31, k = 1
rel_rms_err = 3.3e-07, usecs = 32, k = 2
rel_rms_err = 3.3e-07, usecs = 31, k = 3
rel_rms_err = 3.3e-07, usecs = 32, k = 4
rel_rms_err = 3.3e-07, usecs = 33, k = 5
rel_rms_err = 3.3e-07, usecs = 32, k = 6
rel_rms_err = 3.3e-07, usecs = 31, k = 7
rel_rms_err = 3.3e-07, usecs = 30, k = 8
rel_rms_err = 3.3e-07, usecs = 30, k = 9
rel_rms_err = 3.3e-07, usecs = 30, k = 10
rel_rms_err = 3.3e-07, usecs = 30, k = 11
rel_rms_err = 3.3e-07, usecs = 29, k = 12
rel_rms_err = 3.3e-07, usecs = 31, k = 13
rel_rms_err = 3.3e-07, usecs = 30, k = 14
rel_rms_err = 3.3e-07, usecs = 31, k = 15
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 8 1 32
rel_rms_err = 3.3e-07, usecs = 46, k = 0
rel_rms_err = 3.3e-07, usecs = 31, k = 1
rel_rms_err = 3.3e-07, usecs = 32, k = 2
rel_rms_err = 3.3e-07, usecs = 31, k = 3
rel_rms_err = 3.3e-07, usecs = 32, k = 4
rel_rms_err = 3.3e-07, usecs = 31, k = 5
rel_rms_err = 3.3e-07, usecs = 32, k = 6
rel_rms_err = 3.3e-07, usecs = 30, k = 7
rel_rms_err = 3.3e-07, usecs = 31, k = 8
rel_rms_err = 3.3e-07, usecs = 29, k = 9
rel_rms_err = 3.3e-07, usecs = 29, k = 10
rel_rms_err = 3.3e-07, usecs = 29, k = 11
rel_rms_err = 3.3e-07, usecs = 29, k = 12
rel_rms_err = 3.3e-07, usecs = 30, k = 13
rel_rms_err = 3.3e-07, usecs = 32, k = 14
rel_rms_err = 3.3e-07, usecs = 31, k = 15
rel_rms_err = 3.3e-07, usecs = 30, k = 16
rel_rms_err = 3.3e-07, usecs = 30, k = 17
rel_rms_err = 3.3e-07, usecs = 30, k = 18
rel_rms_err = 3.3e-07, usecs = 29, k = 19
rel_rms_err = 3.3e-07, usecs = 30, k = 20
rel_rms_err = 3.3e-07, usecs = 30, k = 21
rel_rms_err = 3.3e-07, usecs = 29, k = 22
rel_rms_err = 3.3e-07, usecs = 29, k = 23
rel_rms_err = 3.3e-07, usecs = 29, k = 24
rel_rms_err = 3.3e-07, usecs = 29, k = 25
rel_rms_err = 3.3e-07, usecs = 30, k = 26
rel_rms_err = 3.3e-07, usecs = 29, k = 27
rel_rms_err = 3.3e-07, usecs = 29, k = 28
rel_rms_err = 3.3e-07, usecs = 29, k = 29
rel_rms_err = 3.3e-07, usecs = 29, k = 30
rel_rms_err = 3.3e-07, usecs = 31, k = 31

pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 22 1 1
rel_rms_err = 1.5e-06, usecs = 781473, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 22 2 1
rel_rms_err = 1.5e-06, usecs = 783190, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 22 4 1
Out of memory.  Try a smaller batch or increase GPU memory.
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 22 8 1
Out of memory.  Try a smaller batch or increase GPU memory.
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 22 2 2
rel_rms_err = 1.5e-06, usecs = 785348, k = 0
rel_rms_err = 1.5e-06, usecs = 781543, k = 1
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 22 2 4
rel_rms_err = 1.5e-06, usecs = 781577, k = 0
rel_rms_err = 1.5e-06, usecs = 778754, k = 1
rel_rms_err = 1.5e-06, usecs = 778890, k = 2
rel_rms_err = 1.5e-06, usecs = 778164, k = 3

Compare with the performance of the CPU ARM processor.

9:13pm
Read about FFT and DFT wiki for refreshing FFT workload.

________________________________________________________________________________
3/6/2017
9:54AM
Reading FFT tutorials YOUTUBE VIDEOS

11:03AM
FFT Wikipedia

11:45AM
Fully understand how FFT is fast in N*log(N).

2:41PM
Reading M*N matrix multiplication.

3:46PM
Reading Cooley-Tukey FFT algorithm.

10:43PM
Reading Cooley-Tukey FFT algorithm.
________________________________________________________________________________
3/7/2017
10:57AM
Reading Cooley-Tukey FFT algorithm

2:34PM
Reading the Hello-FFT readme context.

4:00PM
Reading the book: PARALLEL PROGRAMMING
in C with MPI and OpenMP
Chapter 15 The Fast Fourier Transform Page:353-367
Page 354 FOURIER ANALYSIS:
Where frequency means the number of complete cycles the wave completes between
time 0 and time 2PI. Nonzero real components correspond to cosine functions;
nonzero imaginary components correspond to sine functions.
Page 355 FOURIER ANALYSIS:
We divide the amplitude shown in the left half of Figure 15.1b by 8 (half of 16,
the number of sample points) to determine the coefficients of various sinusoidal
components.
5:17PM
Mention about the primitive square root of 1 is -1.
10:20PM
Reading the DFT

________________________________________________________________________________
2/8/2016
1:35PM
Page360 FFT
Algorithm with complexity O(n*log(n)) exits and it is amenable to
parallelization.
To evaluate f(x), a polynomial of degree n where n is a power of 2, the
algorithm defines two new polynomials of degree n/2. Function f[0](x) contains
the elements of f(x) associated with the even power of x, while function f[1](x)
contains the elements associated with the odd powers of x.
Note that f(x)=f[0](x^2)+x*f[1](x^2)
So the problem of evaluating f(x) at the points omega n 0,...omega n (n-1)
reduces to evaluating f[0] and f[1] at (omega n 0)^2, (omega n 1)^2...
(omega n n/2-1)^2, then computing f(x)=f[0](x^2)+x*f[1](x^2).

 Halving Lemma
 If n is an even positive number, then the squares of the n complex nth roots of
 units are identical to the n/2 complex (n/2)th roots of unity.

3:06PM
Page 361 Recursive FFT setup and algorithm illustrates in the Figure 15.4.
Page 362
y[k]     <- y[0][k]+omega*y[1][k]
y[k+n/2] <- y[0][k]-omega*y[1][k]
Page 363 Pseudocode statement for Iterative_FFT.

9:15PM
Page 363 Figure 15.5
The use of temporary variable t cuts the number of complex number multiplication
nearly in half.
15.5 PARALLEL PROGRAM DESIGN
Page 364 Figure 15.6
Page 365 Agglomeration and Mapping
Each agglomerated task(process) is represented by a gray rectangle. Every
process controls two arrays of complex values. The first array, a, contains a
contiguous group of input coefficients. The second array, y, holds intermediate
values. At the end of the computation, array y contains a contiguous group of
transformed values.
3 phases in the parallel algorithm
1.processes permute the a's. all-to-all communication.
2.processes perform the first log(n)-log(p) iterations of the FFT by performing
the required *+-
3.the processes perform the final log(p) iterations of the FFT by swapping y's
and performing the requisite *+-.

________________________________________________________________________________
3/9/2017
13:20PM
Page 365 Agglomeration and Mapping
Think of the processes as being organized as a logical hypercube.
During each of the final log(p) iterations, pairs of processes swap values
across a different dimension of the hypercube.

Isoefficiency Analysis
Each process perform an equal share of the computations. Since the computational
complexity of the sequential algorithm is O(nlog(n)), the computational
complexity of the parallel algorithm is O(nlog(n/p)).
Each process controls at most [n/p] elements of a.

14:50PM
Communication complexity
The all-to-all communication step is implemented as a series of swaps across
each hypercube dimension; it has time complexity O[(n/p)log(p)]. There are
log(p) iterations in which each process swaps about n/p values with a partner
process along one of the hypercube dimensions. The total time complexity of
these swaps is O[(n/p)log(p)]. With these assumption, the overall communication
complexity of the algorithm is O[(n/p)log(p)].
Isoefficiency of the parallel program.
The sequenrtial algorithm has time complexity O[nlog(n)]. The parallel overhead
is p times the communication complexity.
The isoefficiency function is: Page 365
The scalability of the FFT algorithm is similar to the scalability of the
hyper-quicksort and PSRS algorithms.
Page 366 Figure 15.7 The implement of n-element FFT on a p-process multicomputer
so that at the beginning of the computation every process contains a contiguous
set of input element, and at the end of the computation every process contains a
contiguous set of output elements.
Again: 3 phases in the parallel algorithm are shown.
1. Permutation of the input elements, all to all communication.
2. The first logn-logp iterations of the FFT require no communication
3. The last logp iterations require that every process swap copies of its values
with a process adjacent across some dimension of a hypercube.

15.6 SUMMARY
1. DFT is important.
2. FFT is interesting for 2 reasons:
  (a)it is a O(nlog(n)) implementation of the DFT comparing with the naive
  O(n^2).
  (b) FFT is amenable to parallelization.

16:13PM
Reading gpu_fft.txt
https://github.com/raspberrypi/userland/blob/master/host_applications/linux/apps/hello_pi/hello_fft/gpu_fft.txt
INTRODUCTION
GPU_FFT is an FFT library for the pi which exploits the BCM2835 SoC 3D hardware
to deliver 10 times more data throughput than is possible on the pi 1. Kernels
are provided for all power-of-2 FFT lengths between 2^8(256B) to 2^22(4KB). A
transpose function, which also uses the 3D hardware, is provided to support 2D
transforms.

QUESTION: If the RAM run out easily at the 2^22, I think the PI has 4G of RAM?
FACT: PI2 B has 1GB RAM. PI 3Like the Pi 2, it also has: 1GB RAM.
Answer: So running the job of 2^22 is taking 2^8(256B) to 2^22(4KB)?

ACCURACY
GPU_FFT uses single-precision floats for data and twiddle factors.
The relative root-mean-square (rms) error in parts-per-million (ppm) for
different transform lengths (N) is typically:
Accuracy has improved significantly over previous releases at the expense of a
small (2%) performance hit; however, FFTW is still one order of magnitude more
accurate than GPU_FFT.
Fastest Fourier Transform in the West (FFTW) is a software library for computing
discrete Fourier transforms.

8:00PM
THROUGHPUT
Use of "mailbox". It uses the mailbox for longer jobs to avoid busy waiting at
100% CPU for too long; GPU_FFT now avoids this 100us overhead by poking GPU
registers directly from the ARM if total batch runtime will be short.

Typical per-transform runtimes for batch size of 1 and 10;

QUESTIONS: What are the FFTW(FFTW_MEASURE mode) on a Pi 1 with L2 cache enabled
runtime comparing to? Is it batch size 1 or 10?

API FUNCTIONS
gpu_fft_prepare()
gpu_fft_execute()
gpu_fft_release()

PARAMETERS
int mb  MAILBOX file descriptor
int log2_N  log2(FFT length)=8-22
int direction FFT direction: forward FFT and inverse FFT
int jobs  Number of transform in batch=1 or more
GPU_FFT **  Output parameter from prepare: control structure
GPU_FFT * Input parameter to execute and release

DATA FORMAT
Data structure created for
Complex data array storage, REAL AND IMAGINARY, pointers to the input and
output arrays, executing a batch of transforms, buffer pointers are obtained.

DIFFICULT TO UNDERSTAND:
When executing a batch of transforms, buffer pointers are obtained as follows:

struct GPU_FFT *fft = gpu_fft_prepare( ... , jobs);
 for (int j=0; j<jobs; j++) {
    struct GPU_FFT_COMPLEX *in  = fft->in  + j*fft->step;
    struct GPU_FFT_COMPLEX *out = fft->out + j*fft->step;

GPU_FFT.step is greater than FFT length because a guard space is left between
buffers for caching and alignment reasons.

ping-pong buffers
GPU_FFT performs multiple passes between ping-pong buffers.

________________________________________________________________________________
3/10/2017
10:00AM
data buffer: a region of a physical memory storage used to temporarily store
data while it is being moved from one place to another.
buffer pointers are void pointer
As the ping-pong buffer means, the final output lands in the same buffer as
input after an even number of passes. Transforms where log2_=12...16 use an odd
number of passes and  the final result is left out-of-place. The input data is
never preserved.

EXAMPLE PROGRAM
It accepts 3 optional command-line arguments:<log2_N> <batch> <loops>.

The special character device is required for the ioctl mailbox through which the
 ARM communicates with the Videocore GPU.

QUESTIONS: What is ioctl mailbox?
The intersection of the ARM communicates with the Videocore GPU. In computing,
ioctl (an abbreviation of input/output control) is a system call for
device-specific input/output operations and other operations which cannot be
expressed by regular system calls.

What is this special character device?

WITH OPEN GL on Pi 1
GPU_FFT and Open GL will run concurrently on Pi 1 if GPU_FFT is configured not
to use VC4 L2 cache by zeroing a define in file gpu_fft_base.c.

#define GPU_FFT_USE_VC4_L2_CACHE 0 // Pi 1 only: cached=1; direct=0

QUESTION: CACHED=1;DIRECT=0; What is the difference between the cached and
direct?

Overall performance will probably be higher if GPU_FFT and Open GL take turns at
using the 3D hardware. Since eglSwapBuffers() returns immediately without
waiting for rendering, call glFlush() and glFinish() afterwards as follows:
glFinish() //wait until v3D hardware is idle
...
gpu_fft_execute(...);//blocking call

13:00PM
QUESTION: What is the 3D hardware that is being used?
What is non-blocking call and blocking call?
What is V3D hardware, and why there has to be wait until it is idle?
It should be 3D hardware.

2D FFT
hello_fft_2d demo source,
hello_fft_2d.bin
generate a windows BMP file:"hello_fft_2d.bmp"

QUESTION: What should Mac Linux do aside from Windows file?

Demo uses a 512^2 array; rectangular arrays are allowed.
gpu_fft_trans.c
ptr.arm.uptr[6] = src->x < dst->y? src->x : dst->y;
ptr.arm.uptr[7] = src->y < dst->x? src->y : dst->x;

One may transpose the output from the second FFT pass back into the first pass
input buffer, by preparing and executing a second transposition; however, this
is probably unnecessary.  It depends on how the final output will be accessed.

14:13PM
Using the terminal, split the screens.
MACOS terminal cannot split screen.

14:33PM
Running the hello_fft.bin using:
more jobs = more transforms per batch, default=1

pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 12 2
rel_rms_err = 7.4e-07, usecs = 252, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 12 4
rel_rms_err = 7.1e-07, usecs = 258, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 12 8
rel_rms_err = 6.9e-07, usecs = 284, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 12 16
rel_rms_err = 6.4e-07, usecs = 267, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 12 32
rel_rms_err = 6.2e-07, usecs = 262, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 12 64
rel_rms_err = 6.1e-07, usecs = 263, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 12 128
rel_rms_err = 6e-07, usecs = 256, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 12 256
rel_rms_err = 5.9e-07, usecs = 256, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 12 1024
rel_rms_err = 5.9e-07, usecs = 255, k = 0
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 12 4096
Out of memory.  Try a smaller batch or increase GPU memory.
pi@raspberrypi:/opt/vc/src/hello_pi/hello_fft $ sudo ./hello_fft.bin 12 2048
rel_rms_err = 0.016, usecs = 254, k = 0

CONCLUSION OF THE INCREASING TRANSFORMS PER BATCH
We can see that the rel_rms_err has improved as the number of transforms per
batch increased. However, as the number of the transform per batch reaching to
the limit that would cause the OUT OF MEMORY, the rate of the accuracy
improvement of the rel_rms_err is decreasing. It has a twist when the number of
transforms per batch reach 2048, the error increased dramatically.
Also each time the number increase to double than the previous one, the time has
been doubled too.
1. Number of transform per batch *2, total time * 2.
2. Number of transform per batch increases, accuracy increases, until MAX GPU
MEM, inverse.

QUESTION:
What kind of transform is it doing?


________________________________________________________________________________

3/11/2017

13:00PM

Finish setup the github repository for the README.txt

14:33PM

Setting up the vimrc (vim configuration)for the easier use of vim.

Trying to figure out how to split window in vim for efficiency.

11:00PM
Atom git-plus package using git for version control.

________________________________________________________________________________
3/12/2017
17:55PM
Using Atom git-plus package failed at cannot pull or push in the Atom.
Switch back to use vim.

________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
________________________________________________________________________________
