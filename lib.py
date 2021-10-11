import numpy as np


def qaoa_erdos_renyi_normalize_parameters(betas, gammas):
    new_betas = (betas + np.pi / 2) % (np.pi) - np.pi / 2
    new_gammas = (gammas + np.pi) % (2 * np.pi) - np.pi
    if new_betas[0] > 0:
        new_betas = -new_betas
        new_gammas = -new_gammas
    return new_betas, new_gammas