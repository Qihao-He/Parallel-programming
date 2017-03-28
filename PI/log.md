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
3/8/2016
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

14:33PMQ
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
Using Atom git-plus package failed at cannot pull okr push in the Atom.
Switch back to use vim.
22:16PM
Find how to use the Atom git-plus package.
22:45PM
Fully understand how to use the Atom git-plus package.
________________________________________________________________________________
3/13/2017
11:22AM
NUMPY
Reading the ESCI 386- Python Fourier Transforms
http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson17-Fourier-Transforms.pdf
DFT

16:07PM
The magnitude squared of the Fourier coefficients , |F(m)|2, is called the
power. Power Spectrum- A plot of the power vs. frequency is referred to as the
power spectrum.
Power spectra for Square signal and for Gaussian Signal.
Signal, Normalized Power.

numpy.fft Module
Function:
fft(s) forward DFT and returns the coefficient F,
ifft(F) the inverse DFT and returns the signal s,
fftfreq(n,d) computes the natural frequencies/wavenumbers. d is an optional
sample spacing.

NATURAL FREQUENCY: The frequency at which a system tends to oscillate in the
absence of any driving or damping force.
Wavenumbers: In the physical sciences, the wavenumbers is the spatial frequency
of a wave, either in cycles per unit distance or radians per unit distance.
fftshift(F) shifts the zero frequency to the center o f the array.
________________________________________________________________________________
3/14/2017
21:54PM
Comparing the parallel program hello_fft, that uses the transmitting the data
back and forward for the processing in different threads. I infer that parallel
is surely faster than the single processing thread.
22:14PM
Read the parallel programming book for inspiration.
________________________________________________________________________________
3/15/2017
11:30AM
The numpy.fft.fft() Function
The fft.fft() function accepts either a real or a complex array as an input
argument, and returns a complex array of the same size that contains the Fourier coefficients.
For the returned complex array:
– The real part contains the coefficients for the cosine terms.
– The imaginary part contains the negative of the coefficients for the sine
terms.
NOTE: This is exactly what forward Fourier transform is doing.

14:31PM
IMPORTANT NOTICE!!! There are different definitions for how a DFT should be
taken.
Fourier coefficients
F(m) forward transform, is the spectral coefficient for the mth wave component.
F(m) is always complex-valued.
f(n) inverse transform, is value of function f at grid point n. f(n) maybe real
or complex-valued.
NumPy actually uses these equations.
This means that NumPy’s Fourier coefficients will be N times larger than
expected!
QUESTION: Why are the equation deferent with the previous ones? And why is that
1/N change in F(m) and f(n) shows that Fourier coefficients are N times larger
than expected.

fft.fftfreq() function
The natural frequencies associated with the spectral coefficients are calculated
using the fft.fft() function.
The zeroth frequency is first, followed by the positive frequencies in ascending
 order, and then the negative frequencies in descending order.

Reading the program file: fft-example.py
FFT result has RE, IM, |Fk|^2 three graphs.
FFT leakage:
1. There is no limits on the number of data points when taking FFTs in NumPy.
2. The FFT algorithm is much more efficient if the number of data points is a
 power of 2 (128, 512, 1024, etc.).
3. The DFT assumes that the signal is periodic on the interval 0 to N, where N
 is the total number of data points in the signal.
4. Care needs to be taken to ensure that all waves in the signal are periodic
 within the interval 0 to N, or a phenomenon known as leakage will occur.
________________________________________________________________________________
3/16/2017
15:30PM
fft.rfft() Function
Since for real input the negative frequencies are redundant, there is an
fft.rfft() function that only computes the positive coefficients for a real
input.

QUESTION: What is real input? Does the real input means the real part or the
actual input? Why is the nagative frequencies are redundant?

The negative frequencies: The concept of negative and positive frequency can be
as simple as a wheel rotating one way or the other way: a signed value of
frequency can indicate both the rate and direction of rotation.

The helper routine fftfreq() only returns the frequencies for the complex FFT.
It is different for even and odd cases, the frequencies are different.
21:30PM
NOTE:
Reading the FFT examples in (numpy.fft) that is using python. While comparing
with the parallel programming using the hello-fft. There should be applied with
the same precision level.

22:00PM
Need to know about NumPy more. And also need to dig into the NumPy and the .fft
module.
NumPy is an extension to the Python programming language, adding support for
large, multi-dimensional arrays and matrices, along with a large library of
high-level mathematical functions to operate on these arrays.--reference from
wiki

numpy.fft.fft
https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html

Compute the one-dimensional discrete FOURIER Transform.
This function computes the one-dimensional n-point discrete Fourier
Transform(DFT) with the efficient Fast Fourier Transform(FFT) algorithm[CT].
________________________________________________________________________________
3/17/2017
Review the DFT and FFT algorithms. n^2 to nlogn.
The parallel algorithm can shorten the FFT algorithm.
________________________________________________________________________________
3/19/2017
Understand the Recursive_FFT(a,n) pseudocode that illustrate the recursively
breaking the array of coefficients a[0 ... (n-1)] to half in recursive.
The time of the Recursive_FFT is T(n)=2*T(n/2)+O(n)=O(nlogn)
Have a pretty good understanding of the Recursive_FFT data float.
Understand the primitive dth root of unity.
Comparing with the iterative algorithm. Iterative_FFT(a,n)
________________________________________________________________________________
3/20/2017
Set up git repository for local and Remote access on Haswell machine, both
repository are synchronized with the Github for version control.
Reading the Iterative_FFT(a,n)
________________________________________________________________________________
3/21/2017
Reference from the book Parallel Program DESIGN
Understand the butterfly patterns of the data.
The iterative algorithm can be derive directly from Figure 15.4. After an
initial permutation step, the algorithm will iterate logn times. Each iteration
corresponds to a horizontal layer in Figure 15.4c. Within an iteration the
algorithm updates values for  each of the n indices. The time complexity is the
same as the recursive algorithm O(nlogn). The use of temporary variable t cuts
the number of complex number multiplications nearly in half.
________________________________________________________________________________
3/25/2017
read the hello_fft
I wonder if I am using the program correctly. Check the usage.
/* if this is true: $hello_fft.bin log2_N [jobs[loops]] */
$hello_fft.bin 8 [4[2]]
/* if this would be right $hello_fft.bin log2_N jobs loops */
$hello_fft.bin 8 4 2
This is the correct input method, see 3/27/2017 notes.

Find that lost connection of raspberrypi. Can not compile and run code
temporarily.

BS NOTE:
Should allow more time for the experiment to run for measuring the energy. The
time increases from 1 second to the log2_N=22 last about 60 seconds, so the main
focus should be on one or a few calculation that would show visible difference.
Also as the calculation increases size, the memory is used up for the matrix
size increases in exponential way.

Dig in the program.
Dig in the header file gpu_fft.h
mailbox.c mailbox.h

Have question where does the API function it is calling from: gpu_fft_prepare()
Also find that the results listing in the blog reference from:
https://www.raspberrypi.org/blog/accelerating-fourier-transforms-using-the-gpu/
is giving the Speedup.

Along with the results showing in the reference:

   Points	   batch=1	   batch=10	   batch=50	   FFTW	   Speedup
   256	112	22	16	92	5.8x
   512	125	37	26	217	8.3x
   1024	136	54	45	482	10.7x
   2048	180	107	93	952	10.2x
   4096	298	256	240	3002	12.5x
   8192	689	624	608	5082	8.4x
   16384	1274	1167	1131	12005	10.6x
   32768	3397	3225	3196	31211	9.8x
   65536	6978	6703	6674	82769	12.4x
   131072	16734	16110	16171	183731	11.4x

These are the time measure for the time-old and time-new that gives out the
speedup. As the points of calculation increases, the speedup of changing the
batch size from 1 to 10 to 50 is not making the typical per-transform runtimes
in microseconds changes a lot.

QUESTION: What does the column difference in batch=1,10,50 means. With the FFTW
 Fastest Fourier Transform in the West (FFTW). From the results shows:
 the Speedup increases to 12.5x peak at 4096 points.

Also read in the results of the gpu_fft.txt:

 log2(N) |   8   |   9   |  10   |  11   |  12  |  13  |  14  |  15
      1 | 0.033 | 0.049 | 0.070 | 0.12  | 0.25 | 0.61 |  1.2 |  3.5
     10 | 0.017 | 0.029 | 0.049 | 0.11  | 0.27 | 0.66 |  1.2 |  3.3
   FFTW | 0.092 | 0.22  | 0.48  | 0.95  | 3.0  | 5.1  | 12   | 31

log2(N) |  16  |  17 |  18 |  19 |   20 |   21 |   22        All times in
      1 |  7.0 |  17 |  43 |  97 |  194 |  388 |  786        milliseconds
   FFTW | 83   | 180 | 560 | 670 | 1600 | 3400 | 8800        2 sig. figs
________________________________________________________________________________
3/26/2017
In the gpu_fft.txt, the accuracy part is describing the RMS root mean square in
PPM parts-per-million, which is pretty accurate.
In the throughput section:
All times in milliseconds 2 significant figures:
That shows the time cost of running the program comparing with the FFTW, which
is significantly shorter than the FFTW.
QUESTION: Why is the Batch size only differ in 1 and 10 form? Why is any number
that is between these two number is not measured?
________________________________________________________________________________
3/27/2016
In the gpu_fft.txt, it mentioned that:It accepts three optional command-line
arguments: <log2_N> <batch> <loops>. So the input method would be
$hello_fft.bin 8 4 2

Command measuing the performance of the FFT job size, batch, loop.
$ cd /opt/vc/src/hello_pi/hello_fft
$ sudo perf_3.16 stat -d ./hello_fft.bin 21 4
rel_rms_err = 1.5e-06, usecs = 384048, k = 0

 Performance counter stats for './hello_fft.bin 21 4':

      16611.682000      task-clock (msec)         #    0.884 CPUs utilized
               331      context-switches          #    0.020 K/sec
                 0      cpu-migrations            #    0.000 K/sec
            16,477      page-faults               #    0.992 K/sec
    11,577,399,763      cycles                    #    0.697 GHz                     [37.56%]
     1,285,911,727      stalled-cycles-frontend   #   11.11% frontend cycles idle    [37.54%]
        11,624,766      stalled-cycles-backend    #    0.10% backend  cycles idle    [37.36%]
     3,590,951,918      instructions              #    0.31  insns per cycle
                                                  #    0.36  stalled cycles per insn [24.99%]
       491,596,173      branches                  #   29.593 M/sec                   [25.14%]
        12,319,210      branch-misses             #    2.51% of all branches         [25.08%]
        27,138,104      L1-dcache-loads           #    1.634 M/sec                   [25.06%]
           697,059      L1-dcache-load-misses     #    2.57% of all L1-dcache hits   [25.08%]
   <not supported>      LLC-loads
   <not supported>      LLC-load-misses

      18.790153624 seconds time elapsed

$ cd ~/QH_directory/userland/host_applications/linux/apps/hello_pi/hello_fft
$ sudo perf_3.16 stat -d ./hello_fft.bin  20 10
rel_rms_err = 1.4e-06, usecs = 192471, k = 0

 Performance counter stats for './hello_fft.bin 20 10':

      20842.337000      task-clock (msec)         #    0.812 CPUs utilized
               599      context-switches          #    0.029 K/sec
                 0      cpu-migrations            #    0.000 K/sec
            20,571      page-faults               #    0.987 K/sec
    14,530,940,586      cycles                    #    0.697 GHz                     [37.67%]
     1,611,996,079      stalled-cycles-frontend   #   11.09% frontend cycles idle    [37.42%]
        14,560,086      stalled-cycles-backend    #    0.10% backend  cycles idle    [37.28%]
     4,522,659,463      instructions              #    0.31  insns per cycle
                                                  #    0.36  stalled cycles per insn [24.94%]
       615,849,834      branches                  #   29.548 M/sec                   [25.04%]
        14,833,907      branch-misses             #    2.41% of all branches         [25.11%]
        32,706,289      L1-dcache-loads           #    1.569 M/sec                   [25.19%]
         1,152,936      L1-dcache-load-misses     #    3.53% of all L1-dcache hits   [25.16%]
   <not supported>      LLC-loads
   <not supported>      LLC-load-misses

      25.663854775 seconds time elapsed

$ sudo perf_3.16 stat -d ./hello_fft.bin  20 1
rel_rms_err = 1.5e-06, usecs = 191712, k = 0

 Performance counter stats for './hello_fft.bin 20 1':

       2073.859000      task-clock (msec)         #    0.895 CPUs utilized
                45      context-switches          #    0.022 K/sec
                 0      cpu-migrations            #    0.000 K/sec
             2,138      page-faults               #    0.001 M/sec
     1,445,726,218      cycles                    #    0.697 GHz                     [37.45%]
       168,054,051      stalled-cycles-frontend   #   11.62% frontend cycles idle    [37.85%]
         2,340,102      stalled-cycles-backend    #    0.16% backend  cycles idle    [38.15%]
       439,204,097      instructions              #    0.30  insns per cycle
                                                  #    0.38  stalled cycles per insn [25.45%]
        60,354,270      branches                  #   29.102 M/sec                   [25.31%]
         1,630,240      branch-misses             #    2.70% of all branches         [25.16%]
         4,900,540      L1-dcache-loads           #    2.363 M/sec                   [25.60%]
           155,059      L1-dcache-load-misses     #    3.16% of all L1-dcache hits   [25.15%]
   <not supported>      LLC-loads
   <not supported>      LLC-load-misses

       2.316615205 seconds time elapsed

$ sudo perf_3.16 stat -d ./hello_fft.bin  20 10 1
rel_rms_err = 1.4e-06, usecs = 192392, k = 0

Performance counter stats for './hello_fft.bin 20 10 1':

     20795.216000      task-clock (msec)         #    0.820 CPUs utilized
              622      context-switches          #    0.030 K/sec
                0      cpu-migrations            #    0.000 K/sec
           20,571      page-faults               #    0.989 K/sec
   14,462,479,493      cycles                    #    0.695 GHz                     [37.65%]
    1,591,452,238      stalled-cycles-frontend   #   11.00% frontend cycles idle    [37.42%]
       14,030,599      stalled-cycles-backend    #    0.10% backend  cycles idle    [37.63%]
    4,527,389,098      instructions              #    0.31  insns per cycle
                                                 #    0.35  stalled cycles per insn [25.28%]
      618,832,550      branches                  #   29.758 M/sec                   [25.06%]
       14,727,795      branch-misses             #    2.38% of all branches         [24.83%]
       36,632,522      L1-dcache-loads           #    1.762 M/sec                   [24.99%]
          997,478      L1-dcache-load-misses     #    2.72% of all L1-dcache hits   [25.00%]
  <not supported>      LLC-loads
  <not supported>      LLC-load-misses

     25.369885801 seconds time elapsed

$ sudo perf_3.16 stat -d ./hello_fft.bin  20 10 2
rel_rms_err = 1.4e-06, usecs = 193745, k = 0
rel_rms_err = 1.4e-06, usecs = 194533, k = 1

Performance counter stats for './hello_fft.bin 20 10 2':

     41489.336000      task-clock (msec)         #    0.813 CPUs utilized
            1,241      context-switches          #    0.030 K/sec
                0      cpu-migrations            #    0.000 K/sec
           20,567      page-faults               #    0.496 K/sec
   28,924,373,678      cycles                    #    0.697 GHz                     [37.64%]
    3,146,747,530      stalled-cycles-frontend   #   10.88% frontend cycles idle    [37.61%]
       27,314,821      stalled-cycles-backend    #    0.09% backend  cycles idle    [37.43%]
    9,032,409,981      instructions              #    0.31  insns per cycle
                                                 #    0.35  stalled cycles per insn [24.85%]
    1,234,499,221      branches                  #   29.755 M/sec                   [24.84%]
       29,373,667      branch-misses             #    2.38% of all branches         [25.05%]
       59,944,125      L1-dcache-loads           #    1.445 M/sec                   [25.11%]
        2,015,937      L1-dcache-load-misses     #    3.36% of all L1-dcache hits   [25.19%]
  <not supported>      LLC-loads
  <not supported>      LLC-load-misses

     51.033239728 seconds time elapsed


QUESTION: Why is the using more batch is taking more time?
NOTE: "usecs", (microseconds), "rel_rms_err",(relative root mean square error) k
should be the times at which the loop times.
QUESTION: So the usecs time is less than 1 second, when I set the batch size
differ in 1 and 10, how does the usecs actually shows? Is it showing the time
that uses

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
