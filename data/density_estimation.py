
import numpy as np


def distance(coords1, coords2):
    '''
    Distance between two latitude-longitude coordinates
    Good enough approsimation when the compared points are close-by
    '''
    return np.sqrt((coords1[0]-coords2[0])**2 + (coords1[1]-coords2[1])**2)

def gaussian_kernel(x, bw=1.):
    return np.exp(-(x/bw)**2)

def quartic_kernel(x, bw=1.):
    y = (x/bw)**2
    return 15/16. * (1-y)**2 * (y<1)

def weighted_distances(point, ref_coords, kernel='quartic', bw=1.):
    '''
    returns ker(d(point, ref_coords))
    '''
    ker = {'quartic': quartic_kernel, 'gaussian': gaussian_kernel}[kernel]
    distances = distance(point, ref_coords)
    return ker(distances, bw=bw)
    
def point_density(point, ref_coords, kernel='quartic', bw=1.):
    '''
    density of points, defined by `ref_coords`, around `point`
    '''
    w = weighted_distances(point, ref_coords, kernel=kernel, bw=bw)
    return np.sum(w)

def average_score(point, ref_coords, scores, kernel='quartic', bw=1.):
    '''
    Weighted average of `scores`, weighted by distance to `point`
    `ref_coords` are the latitudes and longitudes associated to `scores`
    '''
    w = weighted_distances(point, ref_coords, kernel=kernel, bw=bw)
    if w.sum()==0 and kernel=='quartic':
        return average_score(point, ref_coords, scores, kernel='gaussian', bw=bw)
    return np.sum(w*scores) / w.sum()