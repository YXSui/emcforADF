# Emc for ADF
----
Effective Mass Calculator(**emc**) for Amsterdam Density Functional(ADF) software is an auxiliary python tool that can calculate effective mass and plot band structure automatically.
## Background
----
### 1. effective mass
[effective mass](https://en.wikipedia.org/wiki/Effective_mass_(solid-state_physics)) is defined as:

![](picture/01.svg)

in which *x, y, z* are the directions in the reciprocal Cartesian space (2π/A), *En(k)* is the dispersion relation for the *n*-th electronic band.For electrons or electron holes in a solid, the effective mass is usually stated in units of the rest mass of an electron, *me* (*9.11×1E−31* kg). In these units it is usually in the range *0.01* to *10*, but can also be lower or higher—for example, reaching *1,000* in exotic heavy fermion materials, or anywhere from zero to infinity (depending on definition) in graphene. In some degree, effective mass can represent the mobility of electronics or holes along the transport direction.
### 2. ADF
Amsterdam Density Functional[(ADF](https://www.scm.com/)/[BAND)](https://www.scm.com/product/band_periodicdft/) is a periodic DFT code BAND shares many of the benefits with molecular DFT code ADF. Using atomic orbitals for periodic DFT calculations has a number of advantages over plane waves. But there are still some deficiencies in ADF/BAND such as rough plot of ***band structure*** or inaccurate ***effective mass*** calculation. So the **emc** tools come.

## Installation
----
`emcforADF.py` and `bandforADF.py` are two python scripts that were tested with Python 2.7.

To install:

 - check that if the two scripts are excutable, using `ls -la` to see if there are `x` flag in linux. If doesn't, use command `chmod +x emcforADF.py` and `chmod +x bandforADF.py`.
 - check if the two scripts are in your path `$PATH`
 - use the codes and generate band structure/ effctive mass!
 
 ## Highlight
 ----
 ### BandforADF
  1. user defined band numbers, both valence band (**VB**) and conductence band (**CB**) numbers
  2. can generate dat format file, the band numbers is up to your setting
  3. can give a preview of band structure plot by python, so you can adjust band numbers to generate high quality figures
 
 ## Usage
 ----
 ### BandforADF
 
  1. Run ADF, set kpath in ADF input file.
  2. generate output.file
  3. generate Kpoints in csv format(using GUI bandstructure)
  4. put output.file and emass.csv(whatever you name it) and python scripts in the same directory
  5. use command `python bandforADF.py` to generate bandstructure and dat format file


