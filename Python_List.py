spisok=[] #пустой список
numbers=[1,2,3,4,5]
abc=['A','B,','C']
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
  print("1-добавить букву в список")
  print("2-соединить два списка/n3-добавить букву на i позицию")
  print("4-удалить элемент/n5-удалить элемент, указав его порядковый номер")
  print("6-узнать индекс/n7-перевернуть список")
  valik=int(input())
  if valik==1:
   a=input("Введи букву ")
   slovo_list.append(a)
   print(f"Добавили {a} новый список", slovo_list)
  elif valik==2:
   slovo_list.extend(abc)
   print(slovo_list)
  elif valik==3:
   a=input("Введи букву, которую хочешь добавить ")
   i=input("Введи номер позиции, куда хочешь добавить букву ")
   slovo_list.insert(i-1,a) #0,1,2...
   print(slovo_list)
  elif valik==4:
   a=input("Введи букву, которую хочешь удалить ")
   n=slovo_list.count(a)
   if n>0:
       for i in range(n):
        slovo_list.remove(a)
   else:
    print("Искомой буквы нет ")
   print(slovo_list)
  elif valik==5:
   i=int(input("Введи номер позиции элемента для удаления "))
   n=len(slovo_list)
   if i<=n:
    slovo_list.pop(i)
    print(slovo.list)
   else:
      print("Букв меньше, чем указаная позиция ")
  elif valik==6:
    a=input("Введи букву, позицию которой ты хочешь узнать ")
    i=slovo_list.index(a) #проверка, если буквы нет
    print(f"Элемент {a} стоит на {i+1}-ом месте")
  elif valik==7:
    slovo_list.reverse()
    print(slovo_list)