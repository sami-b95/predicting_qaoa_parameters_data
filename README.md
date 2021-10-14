# Predicting parameters for the Quantum Approximate Optimization Algorithm for MAX-CUT from the infinite-size limit

This repository contains code to re-generate the figures in the paper ***.

The data is not included in the repository. It must be downloaded from [this link](https://zenodo.org/record/5569075/files/data.tar.xz) and unpacked at the root of this repository.

The code in the following 3 Jupyter notebooks at the root of the repository:
- [infinite_size_parameters.ipnyb](./infinite_size_parameters.ipynb): Generate the plots of optimal angles for MAX-CUT QAOA on Erdos-Renyi/Chung-Lu graphs.
- [finite_size_instances.ipnyb](./finite_size_instances.ipynb): Generates the result histograms of optimizing QAOA MAX-CUT on Erdos-Renyi or Chung-Lu instances.
- [sk_finite_size.ipnyb](./sk_finite_size.ipynb): Generates the plots of the QAOA energy on the finite-size SK model, evaluated by the Monte-Carlo algorithm from the paper.