# barvin (beetle darvin) [work in progress]

The aim is to create phylogenesis simulation and ultimately compare cladograms
inferred with different algorithms to ground truth.

## Outline

Beetles are instances of Species class characterized by:

1. faux binomial name generated from a list of polish words
2. DNA sequence for phylogenetic analysis (can be viewed as 18S rDNA)
3. phylogenetic relationships (immediate descendants and ancestor)
4. extinction status (bool)

After instantiating Species() you can can perform cladogenesis which will:
1. create 2 new Species()
2. set appropriate phylogenetic relations
3. set each descendats genome to a mutated version of the original
4. mark the ancestor as extinct

```
beetle = Species()
beetle.cladgen()
```

## worder.py 

This module defines Worder() class used to generate faux binomial names and pool
*reasonably* sounding traits.

Worder instance stores binomial name components and traits as numpy string
arrays. The pool() method pools random k lines (default is k=100) and can be
used to reload the selection if names become repetitive. The christen() method
returns a faux binomial name as a string.

```
wd = Worder()
wd.pool()
name = wd.christen()
```

## genome.py

[wrk in prgrs]
