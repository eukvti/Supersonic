import numpy as np
M=float(input("Mach Sayısını Giriniz:"))
WedgeAcisi = float(input("Wedge Açısını Giriniz:"))
gamma = 1.4
def Hesaplayici(i, M):
    Denklem1 = 1 / (np.tan(np.deg2rad(WedgeAcisi)))
    Denklem2 = np.tan(i) * (((gamma + 1) * M ** 2.0) / (2 * (M ** 2 * (np.sin(i)) ** 2 - 1)) - 1)
    error1 = np.abs(Denklem2 - Denklem1)
    return error1
def MachCalculator(i,M):
    M2_UP = (gamma - 1) * M ** 2 * np.sin(i) ** 2 + 2
    M2_DO = 2 * gamma * M ** 2 * np.sin(i) ** 2 - (gamma - 1)
    M2_NE = np.sin((i - np.deg2rad(WedgeAcisi))) ** 2
    M2 = np.sqrt(M2_UP / (M2_DO * M2_NE))
    return M2
for i in np.linspace(np.deg2rad(WedgeAcisi),np.deg2rad(60),num=9000000):
    Errorcheck1 = Hesaplayici(i,M)

    if np.abs(Errorcheck1) < 0.0001:
        M2 = MachCalculator(i,M)
        print("Hesaplanıyor....")
        Bheta = i
        break
Bhetaacisi = np.rad2deg(Bheta)
print("Şok Açınız:", Bhetaacisi , "Şokun Arkasındaki Mach sayısı :", M2  )

