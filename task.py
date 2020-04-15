import os


def find_path(file_name):
    for x,y,z in os.walk("//Users//vijayanand"):
        if file_name in z:
            return os.path.join(x,file_name)
    return None

def get_ext(path):
    ext_list = []
    for x,y,z in os.walk(path):
        if z:
            for items in z:
                ext = os.path.splitext(items)[-1]
                if ext and ext not in ext_list:
                    ext_list.append(ext)

    return ext_list

class Summa:
    def fun1(self):
        return "fun11"
    def fun2(self):
        return "fun22"
    def fun3(self):
        return "fun33"

#k = find_path('desktoppicture.db')
#print(k)
#k = get_ext("//Users//vijayanand")
k = dir(Summa)
k = [x for x in k if x[0] !='_']
print(k)
obj = Summa()

l = [getattr(Summa, x)(Summa()) for x in k]
print(l)

print(dict(list(zip(k,l))))