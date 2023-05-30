import egtplot
from egtplot import plot_static


def get_payoff(b, c, k, p, alpha):
    return [[2 * b - c, b - c, 2 * b - c], 
            [2 * b, 0, b - p], 
            [2 * b - c, b - c - k + alpha * p, 2 * b - c]]

# benefit, cost, kostofp, p, benefitof p

parameter_values = [[3], [2], [.19], [2], [.1]]
labels = ['N', 'S', 'I']

simplex = plot_static(parameter_values, custom_func=get_payoff, 
vert_labels=labels,
                        background=True)
# grey is a saddle point, dotted line means every point is equilibrium, 
white circle means unstable equilibrium (I and N have it too but already 
has dotted line)
