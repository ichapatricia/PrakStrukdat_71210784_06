from re import X


class NodeTabungan:
    no_rekening = None
    nama = None
    saldo =  None
    next = None

def __init__(self,no_rekening,nama,saldo=0):
    self.no_rekening = no_rekening
    self.nama = nama
    self.saldo = saldo
    self.next = None

class SLNC:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def hapus(self, indeks):
        x = self.head
        if indeks == 0:
            self.head = x.next
            del x
            self._size -=1
        elif indeks == self._size-1:
            while x.next != self.tail:
                x = x.next
            del self.tail
            self.tail = x
            self.tail.next = None
            self.size -=1
        else:
            for i in range(indeks-1):
                x= x.next

                x.next = x.next.next
                del x.next
            self.size -=1
        
    def print(self):
        x = self.head

        while x:
            print("Norek :",x.no_rekening)
            print("Saldo :",x.nama)
            print("Norek :",x.saldo)
            x = x.next

    def insert_head(self,no_rekening,nama,saldo):
        rek_baru = NodeTabungan(no_rekening,nama,saldo)
        if self.size == 0:
            self.head = rek_baru
            self.tail = rek_baru
        else:
            rek_baru.next = self.head
            self.head = rek_baru

        self.size += 1

slnc=SLNC()
slnc.insert_head(201,"Hanif",250000)
slnc.insert_head(201,"YUdha",150000)
slnc.print()
slnc.filter(100)
slnc.print()
slnc.update(200)
slnc.update(50)
slnc.print()



    