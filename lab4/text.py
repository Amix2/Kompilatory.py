class klasa:
    def klasa(self):
        self.val = 1


dic = {
    klasa.__name__ : 1
}

q = klasa()
print(q)
print(dic[q.__class__.__name__])
print(klasa.__name__)
