List=["italy","rome","usa","india"]
print(List)
print("List : \n1.Add new  \n2.delete \n3.delete selected item")
selection=input("make your selection:")
a=input ()
print()
if selection=="1":
    List.insert(4,a)
    print(List)
elif selection=="2":
   List.remove( List.index(a))
   print(List)
elif selection=="3":
    pass
else:
    print("not a valid selection")
