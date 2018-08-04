# binding energy calculator

from scipy.constants import m_p, m_n, m_e, m_u, c, eV
MeV = 1.0e6*eV
mp = m_p*c**2/MeV
mn = m_n*c**2/MeV
me = m_e*c**2/MeV
mu = m_u*c**2/MeV

def BE(Z,N,Delta):
    A = Z+N
    return Z*(mp+me)+N*mn - A*mu - Delta
