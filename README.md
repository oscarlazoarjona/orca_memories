Solvers and accessories for Off-Resonant cascaded absorption quantum memories.

This package is currently written for Python 2.7, and all Python commands should use this version (until a new release happens). The following commands assume a UNIX-like OS.

Installation
============
Clone and install using pip:

    $ git clone https://github.com/oscarlazoarjona/orca_memories
    $ pip install orca_memories/

To upgrade to a newer version:

    $ cd orca_memories
    orca_memories$ git pull
    orca_memories$ pip install . --upgrade


To uninstall:

    $ pip uninstall orca_memories

Using orca_memories
===================

To run any of the examples go to the `orca_memories/examples/` directory and run Python on them. The examples will output plots and other files to the corresponding folders in the examples folder.

Running a high efficiency memory with feasible parameters:

    $ cd orca_memories/examples/
    orca_memories/examples$ python _01_high_efficiency.py
    Atom: Rb87
    delta1: 9.000 GHz
    delta2: -9.000 GHz
    Rabi frequency: 5.880 GHz
    Signal & Control bandwidth: 0.735 GHz, 2.953 GHz
    Signal & Control duration: 0.600 ns, 0.300 ns
    Signal & Control waists: 131.000 um, 131.000 um
    Signal & Control double Rayleigh range: 13.819 cm, 13.895 cm
    Control pulse energy :      6.031 nJ
    Critical pulse energy:      6.031 nJ
    Average control power:      0.482 W
    Critical average control power:      0.482 W
    t0s: 1.180 ns, t0w: 1.180 ns, t0r: 4.680 ns
    L: 27.410 cm
    Temperature: 115.00 °C
    n: 1.52e+19 m^-3
    kappa: 3.21e+10 sqrt((m s)^-1)
    Pumping: 0.0

    Critical energy: 6.03 nJ
    Analytic-theory efficiency: 0.9358
    Numerical efficiency      : 0.9346
    Theorical efficiency      : 0.9346

    Beam-splitter picture transmissivities and reflectivities:
    TB: 0.0313, RS: 0.9625
    RB: 0.9710, TS: 0.0339

![](https://raw.githubusercontent.com/oscarlazoarjona/orca_memories/master/pictures/high_efficiency.png)

Checking this solution against the differential equations:

    orca_memories/examples$ python _02_check_solution.py
    For the write process:
    the log_10 of relative and global errors (for B and S):
    Left and right hand sides comparison:
            Bmin   Bave   Bmax   Smin   Save   Smax
    rerr: -15.95 -14.99 -13.41 -15.95 -14.21 -12.10
    gerr: -18.58 -15.03 -13.63 -17.24 -14.35 -12.95

    For the read process:
    the log_10 of relative and global errors (for B and S):
    Left and right hand sides comparison:
            Bmin   Bave   Bmax   Smin   Save   Smax
    rerr: -15.95 -14.94 -13.70 -15.95 -14.14 -11.58
    gerr: -17.97 -15.03 -13.81 -17.66 -14.23 -12.79
