def input_dic1():
    n = int(input("Nhap vao n = "))
    a = {}
    for i in range(n):
        print("Nhap san pham {}: ".format(i+1))
        id = input("Nhap ma hang: ")
        quantity = int(input("Nhap so luong: "))
        a[id] = quantity
    return a


def init_dic2():
    b = {
        1: "Nha cung cap A",
        2: "Nha cung cap B",
        3: "Nha cung cap C"
    }
    return b

def output_dic(a):
    for key, value in a.items():
        print("Ma hang: {}, So luong: {}".format(key, value))

def H001_dic1(a):
    if "H001" in a:
        a["H001"] = 200
    else:
        quantity = int(input("Nhap so luong cho H001: "))
        a["H001"] = quantity
        print("Da them H001 vao tu dien !")
    return a


def del_soluong_0(a):
    keys_to_remove = [key for key, value in a.items() if value == 0]

    for key in keys_to_remove:
        del a[key]

    return a


def output_list(a):
    id_list = list(a.keys())
    quant_list = list(a.values())

    print("3 phan tu dau cua id_list: ")
    print(id_list[0:3])

    print("3 phan tu cuoi cua quant_list: ")
    print(quant_list[-3:])


a = input_dic1()
output_dic(a)
output_list(a)


