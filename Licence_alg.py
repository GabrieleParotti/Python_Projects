#functions:
# J=(Omega*tau*gamma**(2*(J/N)))/((gamma**(J/N)+1)*((pi+Theta*ct)*tau*gamma*gamma**(J/N)+Theta*(cd-ct*tau)))
# Omega=sum_n^{N}omega_n
# rho=J/N

class Licence:
    
    def __init__(self,omega=40,tau=0.047,J=None,N=None,gamma=1.85,pi=104,Theta=8,cd=0.136,ct=1.7, j=None):
        self.omega=omega
        self.tau=tau
        self.J=J
        self.N=N
        self.gamma=gamma
        self.pi=pi
        self.Theta=Theta
        self.cd=cd
        self.ct=ct
        self.j=j

    def opt_lin(self, N):
        omega = self.omega
        tau = self.tau
        gamma = self.gamma
        pi = self.pi
        Theta = self.Theta
        cd = self.cd
        ct = self.ct
        J=N #initial guess
        for t in range(100):
            j=((omega*N)*tau*gamma**(2*(J/N)))/((gamma**(J/N)+1)*((pi+Theta*ct)*tau*gamma**(J/N)+Theta*(cd-ct*tau)))
            J=j
        return(J)

licence=Licence()
print(licence.opt_lin(67000)) 