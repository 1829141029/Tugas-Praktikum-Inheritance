class Malware(object):
	def __init__ (self, t, g, a):
		self.trojan = t
		self.generic = g
		self.adware = a

	def jumlahMalware(self):
		return self.trojan + self.generic + self.adware

	def cetakData(self):
		print("Malware Trojan\t: ", self.trojan)
		print("Malware Generic\t: ", self.generic)
		print("Malware Adware\t: ", self.adware)

	def cetakJM(self):
		print("Total dari semua Malware yang berada di Perangkat Anda \t= ", self.jumlahMalware())

class KeadaanPerangkat(Malware):
	def __init__(self, t, g, a, p):
		self.trojan = t
		self.generic = g
		self.adware = a 
		self.perangkat = p
		
	def cetakData(self):
		print("Malware Trojan\t: ", self.trojan)
		print("Malware Generic\t: ", self.generic)
		print("Malware Adware\t: ", self.adware)
		print("Keadaan Perangkat Anda Saat ini\t: ", self.perangkat)

def main():
	wh1 = KeadaanPerangkat (12, 5, 9, "Terancam")
	wh1.cetakData()
	wh1.cetakJM()

if __name__ == "__main__":
	main()
