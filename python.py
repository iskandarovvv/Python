#       1
#javohir = {
#    "ismi" : "Javohir",
#    "yoshi" : "16",
#    "tuman" : "Bog'ot tumani"
#}
#print(f"Do'stimning ismi : {javohir['ismi']} , u {javohir['yoshi']} da u {javohir['tuman']} da yashaydi!")
#







#                         2
#lugat = {
#    "diyorbek" : "osh",
#    "javohir" : "sho'rva",
#    "isroil" : "somsa"
#}
#print(f"Diyorning yoqtirgan taomi {lugat['diyorbek']}")




#              3
python = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"
}
#print(f"Pythonda else {python['else']}")

#             4
#kalit = input("Kalit so'z kiriting:")
#print(python.get(kalit, "Bunday so'z mavjud emas"))







#          5
kalit = input("Kalit so'z kiriting : ")
qisqasi = python.get (kalit)
if qisqasi == None :
    print("Bunday so'z mavjud emas")
else :
    print(f"{kalit.title()} so'zi {qisqasi} deb tarjima qilinadi")