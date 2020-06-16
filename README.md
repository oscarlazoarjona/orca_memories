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
    Rabi frequency: 1.643 GHz
    Signal & Control bandwidth: 1.471 GHz, 2.953 GHz
    Signal & Control duration: 0.300 ns, 0.300 ns
    Signal & Control waists: 131.000 um, 131.000 um
    Signal & Control double Rayleigh range: 13.819 cm, 13.895 cm
    Control pulse energy :      1.885 nJ
    Critical pulse energy:      1.885 nJ
    t0s: 1.180 ns, t0w: 1.180 ns, t0r: 4.680 ns
    L: 13.705 cm
    Temperature: 115.00 °C
    n: 1.52e+19 m^-3
    kappa: 2.34e+06 sqrt((m s)^-1)

    Critical energy: 1.88 nJ
    Analytic-theory efficiency:  0.7953
    Numerical efficiency: 0.7862

    Beam-splitter picture transmissivities and reflectivities:
    TB: 0.0921, RS: 0.8819
    RB: 0.9079, TS: 0.1181

Checking this solution against the differential equations:

    orca_memories/examples$ python _01_high_efficiency.py
    For the write process
    the log_10 of relative and global errors (for B and S):
    Left and right hand sides comparison:
            Bmin   Bave   Bmax   Smin   Save   Smax
    rerr: -15.95 -11.58  -8.55 -15.95 -12.51 -10.31
    gerr: -19.23 -12.03  -9.54 -17.90 -12.89 -11.20

    For the read process
    the log_10 of relative and global errors (for B and S):
    Left and right hand sides comparison:
            Bmin   Bave   Bmax   Smin   Save   Smax
    rerr: -15.95 -11.80  -9.10 -15.95 -12.45 -10.17
    gerr: -17.80 -12.15  -9.92 -17.72 -12.89 -11.39
