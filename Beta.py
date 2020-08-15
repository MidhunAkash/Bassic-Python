class l:
    id1=""
    pasw=""
    nam=""
class c:
    it1=""
    it2=""
    it3=""
    it4=""
    q1=0
    q2=0
    q3=0
    q4=0
    c1=0
    c2=0
    c3=0
    c4=0
    tot=0
def intro():   
 print("""        ********************************
                             welcome
                                to
                           Super Market
               ********************************
                                               -By Midhun""")
def pay():
 inp1=input("""you have to pay Rs.%d
 choose the payment method:
  1.internet banking
  2.credit card
  3.cash on delivery(COD)
  4.cancel the payment\n"""%c.tot)
 if inp1=='1':
     print(""""THANK YOU FOR SHOPING" See you again\n""")
     con()
 elif inp1=='2':
     print(""""THANK YOU FOR SHOPING" See you again\n""")
     con()
 elif inp1=='3':
     inp2=input("please enter you adress:")
     print("""your oder will be deliver to this adress:"%s".

            "THANK YOU FOR SHOPING" See you again\n"""%inp2)
     con()
 elif inp1=='4':
     print("'YOUR PAYMENT IS CANCELLED SUCESSFULLY'")
     cart()
 else:
     print("invalid option please try again")
     pay()
def con():     
 inp1=input("""press:
 1.To continue shoping
 2.Go to exit\n""")
 if inp1=='1':
     sh()
 elif inp1=='2':
     exit()
 else:
     print("invalid option please try again")
     con()
     
def cart():
 c.tot=c.c1+c.c2+c.c3+c.c4
 print("""your products in the cart are:
       Product Name      quantity        Amount
        %s      %d            Rs.%d
        %s                 %d            Rs.%d
        %s       %d            Rs.%d
        %s     %d            Rs.%d
              
                total amount=Rs.%d\n"""%(c.it1,c.q1,c.c1,c.it2,c.q2,c.c2,c.it3,c.q3,c.c3,c.it4,c.q4,c.c4,c.tot))
 inp1=input("press:\n1.continue shoping\n2.Go for the payment\n3.delete product\n")
 if inp1=='1':
     sh()
 elif inp1=='2':
     pay()
 elif inp1=='3':
     inp2=input("""press to delete the product:
 sl.no  Product Name       quantitiy     Amount
  1.    %s      %d              Rs.%d
  2.    %s                 %d              Rs.%d
  3.    %s       %d              Rs.%d
  4.    %s     %d              Rs.%d\n"""%(c.it1,c.q1,c.c1,c.it2,c.q2,c.c2,c.it3,c.q3,c.c3,c.it4,c.q4,c.c4))
     if inp2=='1':
         if c.q1>0:
             c.q1-=1
             c.c1-=30
             cart()
         else:
           c.it1=""
           c.c1=0
           c.q1=0
           cart()
     elif inp2=='2':
         if c.q2>0:
             c.q2-=1
             c.c2-=45
             cart()
         else:
          c.it2=""
          c.c2=0
          c.q2=0
          cart()
     elif inp2=='3':
         if c.q3>0:
             c.q3-=1
             c.c3-=70
             cart()
         else:
          c.it3=""
          c.c3=0
          c.q3=0
          cart()
     elif inp2=='4':
         if c.q4>0:
             c.q4-=1
             c.c4-=50
             cart()
         else:
          c.it4=""
          c.c4=0
          c.q4=0
          cart()
     else:
         print("invalid option please try again")
         cart()
 else:
     print("invalid option please try again")
     cart()
def sh():
 inp4=input("select your catogory:\n1.soaps\n2.tooth pastes\n3.open cart\n4.exit the proggramme\n")
 if inp4=='1':
     inp5=input("select your brand:\n1.santhoor(100g)--30/-\n2.lux(100g)--45/-\n")
     if inp5=='1':
         inp6=input("press:\n1.add to cart\n2.change the product\n")
         if inp6=='1':
             c.q1=float(input("how many qantity:"))
             c.it1="santhoor(100g)"
             c.c1=30*c.q1
             print("\nproduct is 'ADDED TO CART' Sucessfully\n")
             sh()
         else:
             sh()
     elif inp5=='2':
         inp7=input("press:\n1.add to cart\n2.change the product\n")
         if inp7=='1':
             c.q2=float(input("how many qantity:"))
             c.it2="lux"
             c.c2=45*c.q2
             print("\nproduct is 'ADDED TO CART' Sucessfully\n")
             sh()
         else:
             sh()
     else:
         print("invalid option please try again")
         sh()
 elif inp4=='2':
     inp8=input("select your brand:\n1.colgate(500g)--70/-\n2.pepsident(500g)--50/-\n")
     if inp8=='1':
         inp9=input("press:\n1.add to cart\n2.change the product\n")
         if inp9=='1':
             c.q3=float(input("how many qantity:"))
             c.it3="colgate(500g)"
             c.c3=70*c.q3
             print("\nproduct is 'ADDED TO CART' Sucessfully\n")
             sh()
         else:
             sh()
     elif inp8=='2':
         inp10=input("press:\n1.add to cart\n2.change the product\n")
         if inp10=='1':
             c.q4=float(input("how many qantity:"))
             c.it4="pepsident(500g)"
             c.c4=50*c.q4
             print("\nproduct is 'ADDED TO CART' Sucessfully\n")
             sh()
         else:
             sh()
     else:
         print("invalid option please try again")
         sh()
 elif inp4=='3':
     cart()
 elif inp4=='4':
     exit()
 else:
     print("invalid option please try again")
     sh()
def log():
 
     in2=input("enter your user id:")
     in3=input("enter your password:")
     if in2==l.id1:
         if in3==l.pasw:
             print("\n' welcome",l.nam,"'\n")
             intro()
             sh()
         else:
             print("incorrect password")
             log()
     else:
         print("incorrect user id")
         inp1=input("press:\n1.To Register\n2.to renter you user id\n")
         if inp1=='1':
             up()
         else:
             log()
def up():
  l.nam=input("enter your Name:")
  l.id1=input("create your own user id:")
  pas()
def pas():
   l.pasw=input("create you pasword(*must cotain atleat 4 or more characters):")    
   if len(l.pasw)>=4:
       pho()
   else:
        print("you have to enter atleast 4 numbers")
        pas()
def pho():
   ph=(input("enter your Phone number:"))
   if len(ph)==10:
     print("""you have completed your "sing up" process SUCESSFULLY.
Now you can go for the "login".
LOGIN""")
     log()
   else:
     print("invalid phone number")
     pho()
intro()
print("""\nNote:if you visting here for the first time then
please go for the "Register" option.\n""")
def sing():
 in1=input("press\n1.login\n2.Register\n3.exit\n")
 if in1=='1':
    log()
 elif in1=='2':
    up()
 elif in1=='3':
    exit()
 else:
    print("invalid option please try again")
    sing()
sing()         
