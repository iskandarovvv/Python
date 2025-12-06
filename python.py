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
#python = {
#    'integer':"Butun son",
#    'float':"O'nlik son",
#    'string':"Matn",
#    'list':"Ro'yxat",
#    'tuple':"O'zgarmas ro'yxat"
#}
#print(f"Pythonda else {python['else']}")

#             4
#kalit = input("Kalit so'z kiriting:")
#print(python.get(kalit, "Bunday so'z mavjud emas"))







#          5
#kalit = input("Kalit so'z kiriting : ")
#qisqasi = python.get (kalit)
#if qisqasi == None :
#    print("Bunday so'z mavjud emas")
#else :
#    print(f"{kalit.title()} so'zi {qisqasi} deb tarjima qilinadi")








#
#python = {
#    'boolean':'Mantiqiy qiymat',
#    'float': "O'nlik son",
#    'for':"Biror amalni qayta-qayta bajarish tsikli",
#    'if':'Shartlarni tekshirish operatori',
#    'integer':'Butun son'
#}
#for kalit , qiymat in (python.items()):
#    print(f"{kalit.title()} - {qiymat}")







#
#1_mashxur_shaxs = {
#    'ism' : 'Abu Abdulloh Muhammad ibn Ismoil',
#    't_yili' : '810',
#    'vafot_yili' : '870',
#    't_joyi' : 'Buxoro'
#}
#2_mashxur_shaxs = {
#    'ism' : 'Abdulla Qodiriy',
#    't_yili' : '1894',
#    'vafot_yili' : '1938',
#    't_joyi' : 'Toshkent'
#}
#3_mashxur_shaxs = {
#    'ism' : 'Erkin Vohidov',
#    't_yili' : '1936',
#    'vafot_yili' : '2016',
#    't_joyi' : 'Fargona'
#}
#4_mashxur_shaxs = {
#    'ism' : 'Alisher Navoiy',
#    't_yili' : '1441',
#    'vafot_yili' : '1501',
#    't_joyi' : 'Xirot'
#}
#
#shaxslar = [1_mashxur_shaxs , 2_mashxur_shaxs , 3_mashxur_shaxs , 4_mashxur_shaxs]
#
#for shaxs in shaxslar:
#    ism = shaxs['ism']
#    t_yili = shaxs['t_yili']
#    vafot_yili = shaxs['vafot_yili']
#    t_joyi = shaxs['t_joyi']
#    print(f"{ism} {t_yili}-yilda {t_joyi}da tavvallud topgan." f"{vafot_yili-t_yili} umr ko'rgan.")












#
#
#
#
#
#
#
#1_mashxur_shaxs = {
#    'ism' : 'Abu Abdulloh Muhammad ibn Ismoil',
#    't_yili' : '810',
#    'vafot_yili' : '870',
#    't_joyi' : 'Buxoro'
#    'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#}
#2_mashxur_shaxs = {
#    'ism' : 'Abdulla Qodiriy',
#    't_yili' : '1894',
#    'vafot_yili' : '1938',
#    't_joyi' : 'Toshkent'
#    'asarlar': ["O'tkan kunlar","Mehrobdan chayon", "Obid ketmon"]
#}
#3_mashxur_shaxs = {
#    'ism' : 'Erkin Vohidov',
#    't_yili' : '1936',
#    'vafot_yili' : '2016',
#    't_joyi' : 'Fargona'
#    'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#}
#4_mashxur_shaxs = {
#    'ism' : 'Alisher Navoiy',
#    't_yili' : '1441',
#    'vafot_yili' : '1501',
#    't_joyi' : 'Xirot'
#    'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#}
#
#shaxslar = [1_mashxur_shaxs , 2_mashxur_shaxs , 3_mashxur_shaxs , 4_mashxur_shaxs]
#
#for shaxs in shaxslar:
#    ism = shaxs['ism']
#    t_yili = shaxs['t_yili']
#    vafot_yili = shaxs['vafot_yili']
#    t_joyi = shaxs['t_joyi']
#    asarlar = shaxs['asarlar']
#    print(f"{ism} {t_yili}-yilda {t_joyi}da tavvallud topgan." f"{vafot_yili-t_yili} umr ko'rgan.")
#    print(f"\n{ism} ning mashxur asarlari: ")
#    for asar in asarlar:
#        print(asar)




























#kinolar = {
#    'diyorbek':['Interesting','Iqror','Titanic'],
#    'shabnam':['Qasoskorlar','Spiderman','Temir odam'],
#    'javohir':['Tom and jerry','Uyda yolgiz','Shaytanat'],
#    }
#
#for ism, kinolar in kinolar.items():
#    print(f"\n{ism.title()}ning sevimli kinolari:")
#    for kino in kinolar:
#        print(kino)

















#
#
#davlatlar = {
#    "o'zbekiston":{
#                   'poytaxt':"toshkent",
#                   'maydon':448978,
#                   'aholi':33_000_000,
#                   'pul birligi':"so'm"
#                   },
#    "rossiya":{
#                   'poytaxt':"moskva",
#                   'maydon':17_098_246,
#                   'aholi':144_000_000,
#                   'pul birligi':"rubl"
#                   },
#    "aqsh":{
#                   'poytaxt':"vashington",
#                   'maydon':9_631_418,
#                   'aholi':327_000_000,
#                   'pul birligi':"dollar"
#                   },
#    "malayziya":{
#                   'poytaxt':"kuala-lumpur",
#                   'maydon':329750,
#                   'aholi':25_000_000,
#                   'pul birligi':"rinngit"
#                   }
#    }
#
#for davlat, malumot in davlatlar.items():
#    if davlat.lower()=='aqsh':
#        davlat = davlat.upper()
#    else:
#        davlat = davlat.capitalize()
#    print(f"{davlat}ning poytaxti {malumot['poytaxt'].title()}"
#          f"Hududi: {malumot['maydon']} kv.km"
#          f"Aholisi: {malumot['aholi']}"
#          f"Pul birligi: {malumot['pul birligi']}")























#
#

#for1
#k = int(input("k = "))
#n = int(input("n = "))

#for i in range(n):
#    print(k)



#for2
#a = int(input("a = "))
#b = int(input("b = "))
#
#count = 0
#for i in range(a, b + 1):
#    print(i)
#    count = count + 1
#
#print("Sikl", count, "marta takrorlandi")











#for3
#a = int(input("a = "))
#b = int(input("b = "))
#
#count = 0
#for i in range(b -1 , a ,  -1 ):
#    print(i)
#
#count += 1
#print("soni ", count)




















#for4

#narx = float(input("1 kg konfet narxini kiriting: "))
#
#for i in range(1, 10 + 1):
#    print(i, "kg konfet narxi =", narx * i)








#while True :
#    yosh = int(input("Yoshingizni kiriting : "))
#    if yosh <= 7 :
#        narx = 2000
#    elif yosh <= 18 :
#        narx = 3000
#    elif yosh <= 65 :
#        narx = 10000
#    else :
#        narx = 0
#    print(f"Sizga chipta {narx} so'm")
#    javob = input("Yana davom etasizmi? Dasturni tugatish uchun 'exit' yoki 'quite' deb yozing : ")
#    if (javob.lower() == 'quite' or javob.lower() == 'exit') :
#        break








A = "Sevgan kitobingizni kiriting : "

while True :
    kitob = input(A)
    javob = input("Dasturni tugatish uchun 'exit' yoki 'quite' deb yozing :  ")
    if (javob.lower() == 'quite' or javob.lower() == 'exit') :
        break