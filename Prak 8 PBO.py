class Masyarakat_kampus:
    def __init__(self, nama):
        self.nama = nama

    def Gaji(self):
        pass

class Dosen(Masyarakat_kampus):
    def __init__(self):
        super().__init__("Dosen")

    def Gaji(self):
        return "Golongan DOSEN mendapatkan gaji: 45000"

class Karyawan(Masyarakat_kampus):
    def __init__(self):
        super().__init__("STAFF")

    def Gaji(self):
        return "Golongan STAFF mendapatkan gaji: 30000"

class Lain(Masyarakat_kampus):
    def __init__(self):
        super().__init__("Lain")

    def Gaji(self):
        return "Golongan LAINNYA mendapatkan gaji: 150000"

def main():
    dosen = Dosen()
    karyawan = Karyawan()
    lain = Lain()

    print("Nama: Ranngga Aditya Pradana")
    print("Nim: 064002300026")
    print(dosen.Gaji())
    print(karyawan.Gaji())
    print(lain.Gaji())

if __name__ == "__main__":
    main()