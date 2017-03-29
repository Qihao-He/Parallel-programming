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

 $ sudo perf_3.16 stat -d ./hello_fft.bin  8 10 2
 rel_rms_err = 2.7e-07, usecs = 20, k = 0
 rel_rms_err = 2.7e-07, usecs = 18, k = 1

  Performance counter stats for './hello_fft.bin 8 10 2':

          35.376000      task-clock (msec)         #    0.814 CPUs utilized
                 11      context-switches          #    0.311 K/sec
                  0      cpu-migrations            #    0.000 K/sec
                 97      page-faults               #    0.003 M/sec
          1,315,035      cycles                    #    0.037 GHz
          4,507,197      stalled-cycles-frontend   #  342.74% frontend cycles idle
            441,497      stalled-cycles-backend    #   33.57% backend  cycles idle
          4,967,122      instructions              #    3.78  insns per cycle
                                                   #    0.91  stalled cycles per insn [59.55%]
            942,058      branches                  #   26.630 M/sec                   [39.51%]
             40,161      branch-misses             #    4.26% of all branches         [16.84%]
      <not counted>      L1-dcache-loads
      <not counted>      L1-dcache-load-misses
    <not supported>      LLC-loads
    <not supported>      LLC-load-misses

        0.043437430 seconds time elapsed

 $ sudo perf_3.16 stat -d ./hello_fft.bin  8 1 2
 rel_rms_err = 3.3e-07, usecs = 53, k = 0
 rel_rms_err = 3.3e-07, usecs = 34, k = 1

  Performance counter stats for './hello_fft.bin 8 1 2':

          25.234000      task-clock (msec)         #    0.741 CPUs utilized
                 17      context-switches          #    0.674 K/sec
                  0      cpu-migrations            #    0.000 K/sec
                 91      page-faults               #    0.004 M/sec
          3,416,788      cycles                    #    0.135 GHz
          5,496,335      stalled-cycles-frontend   #  160.86% frontend cycles idle
            459,694      stalled-cycles-backend    #   13.45% backend  cycles idle
          4,608,842      instructions              #    1.35  insns per cycle
                                                   #    1.19  stalled cycles per insn [42.36%]
            787,847      branches                  #   31.222 M/sec                   [18.20%]
      <not counted>      branch-misses
      <not counted>      L1-dcache-loads
      <not counted>      L1-dcache-load-misses
    <not supported>      LLC-loads
    <not supported>      LLC-load-misses

        0.034069553 seconds time elapsed

$ sudo perf_3.16 stat -d ./hello_fft.bin  8 50 2
rel_rms_err = 2.5e-07, usecs = 18, k = 0
rel_rms_err = 2.5e-07, usecs = 18, k = 1

 Performance counter stats for './hello_fft.bin 8 50 2':

         85.593000      task-clock (msec)         #    0.905 CPUs utilized
                13      context-switches          #    0.152 K/sec
                 0      cpu-migrations            #    0.000 K/sec
               141      page-faults               #    0.002 M/sec
        59,446,895      cycles                    #    0.695 GHz                     [33.73%]
        18,211,275      stalled-cycles-frontend   #   30.63% frontend cycles idle    [44.18%]
           447,559      stalled-cycles-backend    #    0.75% backend  cycles idle
         9,224,249      instructions              #    0.16  insns per cycle
                                                  #    1.97  stalled cycles per insn [43.85%]
         1,173,759      branches                  #   13.713 M/sec                   [33.63%]
            72,115      branch-misses             #    6.14% of all branches         [28.20%]
            82,373      L1-dcache-loads           #    0.962 M/sec                   [27.02%]
            58,372      L1-dcache-load-misses     #   70.86% of all L1-dcache hits   [26.00%]
   <not supported>      LLC-loads
   <not supported>      LLC-load-misses

       0.094569758 seconds time elapsed
