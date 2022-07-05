class Tabungan:
    #constructor
    def __init__(self, saldo):
        self.saldo=saldo

    #method
    def ambilUang(self, nominal):
        self.saldo -= nominal
    
    def nabung(self, nominal):
        self.saldo += nominal

    def getSaldo(self):
        return self.saldo

tab1 = Tabungan(3000000)
print("Saldo sekarang: ",tab1.getSaldo())
tab1.ambilUang(500000)
print("Saldo sekarang: ",tab1.getSaldo())
tab1.nabung(200000)
print("Saldo sekarang: ",tab1.getSaldo())