from tkinter import *
import tkinter
from tkinter import messagebox
import pypyodbc as db

#کل کد ها باید بین خط های تکینتر باشد در غیر این صورت ارور خواهد داد
#this is for login login Window
loginwindow =  tkinter.Tk()
loginwindow.title("برنامه مدیریت فروشگاه")

try:
    con=db.connect(Trusted_Connectoin='yes',
                    Driver='{SQL Server};',
                    Server='localhost;',
                    Database='Store;')
    curs=con.cursor()
except:
    messagebox.showerror(title='!خطای اتصال',message='!نمی‌توان به پایگاه داده وصل شد')

myVar=[]



def back15func():
    error15.place(x=1000,y=1000)
    sell_custfactor.place(x=91,y=15)
    make_transaction.place(x=91,y=70)
    delete_transaction.place(x=91,y=125)
    shop_stuff.place(x=91,y=180)
    shop_transaction.place(x=91,y=235)

    l15.place(x=1000,y=1000)
    optionmenu1_widget.place(x=1000,y=1000)
    but15.place(x=1000,y=1000)
    back15.place(x=1000,y=1000)
    error15.place(x=1000,y=1000)




def but15func():
    #اسم شعبه در متغیر زیر ذخیره شد
    esme_shobe = control_variable1.get()
    print(esme_shobe)
    #حالا از پایگاه داده لیست تراکنش های ان شعبه به دست اید و در متغیر زیر ذخیره شود
    branch_factor = "تراکنش ها"
    error15.place(x=1000,y=1000)
    messagebox.showinfo("تراکنش های شعبه", branch_factor)



def shoptrans_func():
    sell_custfactor.place(x=1000,y=1000)
    make_transaction.place(x=1000,y=1000)
    delete_transaction.place(x=1000,y=1000)
    shop_stuff.place(x=1000,y=1000)
    shop_transaction.place(x=1000,y=1000)

    l15.place(x=150,y=15)
    optionmenu1_widget.place(x=220,y=55)
    but15.place(x=230,y=100)
    back15.place(x=20,y=270)



def back14func():
    sell_custfactor.place(x=91,y=15)
    make_transaction.place(x=91,y=70)
    delete_transaction.place(x=91,y=125)
    shop_stuff.place(x=91,y=180)
    shop_transaction.place(x=91,y=235)

    l14.place(x=1000,y=1000)
    optionmenu2_widget.place(x=1000,y=1000)
    but14.place(x=1000,y=1000)
    back14.place(x=1000,y=1000)
    error14.place(x=1000,y=1000)





def but14func():
    #کد فروشگاه در متغیر زیر ذخیره شد
    kode_forushgah = control_variable2.get()
    print(kode_forushgah)
    #حالا اقلام ان فروشگاه از پایگاه داده بررسی شود و در متغیر زیر ذخیره شود
    shop_stuff_list = "اقلام فروشگاه"
    error14.place(x=1000,y=1000)
    messagebox.showinfo("اقلام موجود در فروشگاه", shop_stuff_list)



def shopstuff_func():
    sell_custfactor.place(x=1000,y=1000)
    make_transaction.place(x=1000,y=1000)
    delete_transaction.place(x=1000,y=1000)
    shop_stuff.place(x=1000,y=1000)
    shop_transaction.place(x=1000,y=1000)

    l14.place(x=150,y=15)
    optionmenu2_widget.place(x=220,y=55)
    but14.place(x=230,y=100)
    back14.place(x=20,y=270)






def but13func():
    trans_code=entryDel.get()
    curs.execute("delete from purchases where trans#= "+trans_code)
    messagebox.showinfo('نمایش کل جدول',message=curs.fetchall())



def back13func():
    sell_custfactor.place(x=91,y=15)
    make_transaction.place(x=91,y=70)
    delete_transaction.place(x=91,y=125)
    shop_stuff.place(x=91,y=180)
    shop_transaction.place(x=91,y=235)

    but13.place(x=1000,y=1000)
    back13.place(x=1000,y=1000)
    l13.place(x=1000,y=1000)



def delfunc():
    sell_custfactor.place(x=1000,y=1000)
    make_transaction.place(x=1000,y=1000)
    delete_transaction.place(x=1000,y=1000)
    shop_stuff.place(x=1000,y=1000)
    shop_transaction.place(x=1000,y=1000)

    but13.place(x=230,y=100)
    back13.place(x=20,y=270)
    l13.place(x=100,y=15)





def maketrans_func():
    sell_custfactor.place(x=1000,y=1000)
    make_transaction.place(x=1000,y=1000)
    delete_transaction.place(x=1000,y=1000)
    shop_stuff.place(x=1000,y=1000)
    shop_transaction.place(x=1000,y=1000)


    l121.place(x=415,y=80)
    entry121.place(x=275,y=80)
    l122.place(x=415,y=120)
    entry122.place(x=275,y=120)
    l123.place(x=415,y=160)
    entry123.place(x=275,y=160)

    l124.place(x=180,y=80)
    entry124.place(x=50,y=80)
    l125.place(x=180,y=120)
    entry125.place(x=50,y=120)
    l126.place(x=180,y=160)
    entry126.place(x=50,y=160)



    but12.place(x=230,y=245)
    back12.place(x=20,y=270)
    l12.place(x=100,y=15)



def but12func():
      kode_tarakonesh = entry121.get()
      print(kode_tarakonesh)
      kode_moshtari = entry122.get()
      print(kode_moshtari)
      kode_shobe = entry123.get()
      print(kode_shobe)
      tarikh = entry124.get()
      print(tarikh)
      zaman = entry125.get()
      print(zaman)
      geymat = entry126.get()
      print(geymat)
      #مقادیر درخواستی اضافه کردن تراکنش در متغیر های بالا ذخیره شد.حالا از پایگاه داده کار انجام شود


def back12func():
    sell_custfactor.place(x=91,y=15)
    make_transaction.place(x=91,y=70)
    delete_transaction.place(x=91,y=125)
    shop_stuff.place(x=91,y=180)
    shop_transaction.place(x=91,y=235)

    but12.place(x=1000,y=1000)
    back12.place(x=1000,y=1000)
    l12.place(x=1000,y=1000)
    l121.place(x=1000,y=1000)
    entry121.place(x=1000,y=1000)
    l122.place(x=1000,y=1000)
    entry122.place(x=1000,y=1000)
    l123.place(x=1000,y=1000)
    entry123.place(x=1000,y=1000)
    l124.place(x=1000,y=1000)
    entry124.place(x=1000,y=1000)
    l125.place(x=1000,y=1000)
    entry125.place(x=1000,y=1000)
    l126.place(x=1000,y=1000)
    entry126.place(x=1000,y=1000)

    entry121.delete(0, END)
    entry122.delete(0, END)
    entry123.delete(0, END)
    entry124.delete(0, END)
    entry125.delete(0, END)
    entry126.delete(0, END)


#back 11
def back11func():
    l11.place(x=1000,y=1000)
    entry11.place(x=1000,y=1000)
    but11.place(x=1000,y=1000)
    optionmenu_widget.place(x=1000,y=1000)
    error11.place(x=1000,y=1000)

    sell_custfactor.place(x=91,y=15)
    make_transaction.place(x=91,y=70)
    delete_transaction.place(x=91,y=125)
    shop_stuff.place(x=91,y=180)
    shop_transaction.place(x=91,y=235)


#button ok 11
def but11func():
    #اسم مشتری در متغیر زیر ذخیره شد.حالا از پایگاه داده نراکنش های ان را بدست بیاور و سپس در متغیر زیر ذخیره ک
    xxxx =  control_variable.get()
    #اسم مشتری در متغیر بالا ذخیره شد.حالا از پایگاه داده نراکنش های ان را بدست بیاور و سپس در متغیر زیر ذخیره کن
    customer_shops = "لیست خرید های مشتری"
    error11.place(x=1000,y=1000)
    messagebox.showinfo("فاکتور خرید های مشتری", customer_shops)



#11
def sell_custfactorfunc():
    sell_custfactor.place(x=1000,y=1000)
    make_transaction.place(x=1000,y=1000)
    delete_transaction.place(x=1000,y=1000)
    shop_stuff.place(x=1000,y=1000)
    shop_transaction.place(x=1000,y=1000)

    l11.place(x=150,y=15)
    optionmenu_widget.place(x=225,y=55)
    but11.place(x=230,y=100)
    back11.place(x=20,y=270)

def cust_factor():
    #اسم مشتری در متغیر زیر است
    moshtari = l01.cget("text")
    print(moshtari)
    #در اینجا باید از پایگاه داده خرید های مشتری در متغیر
    #factor_variable
    #ذخیره شود تا در مسیج باکس نشان داده شود
    factor_variable = "اخرین خرید های شما"
    messagebox.showinfo("فاکتور خرید های شما", factor_variable)


def ok_login_cust():
    #اسم مشتری از لیست انتخاب شده در متغیر زیر ذخیره شد
    xxxx =  control_variable.get()
    l01.config(text=xxxx)
    optionmenu_widget.place(x=1000,y=1000)
    l1custerror.place(x=1000,y=1000)
    print("cust")
    l1.place(x=1000,y=1000)
    butokcust.place(x=1000,y=1000)
    pass_entry.place(x=1000,y=1000)
    l01.place(x=220,y=15)
    butcustfactor.place(x=117,y=50)



def ok_login_sell():

    if pass_entry.get() == "1234" :
        l1sellerror.place(x=1000,y=1000)
        print("sell")
        l1.place(x=1000,y=1000)
        butoksell.place(x=1000,y=1000)
        pass_entry.place(x=1000,y=1000)
        sell_custfactor.place(x=91,y=15)
        make_transaction.place(x=91,y=70)
        delete_transaction.place(x=91,y=125)
        shop_stuff.place(x=91,y=180)
        shop_transaction.place(x=91,y=235)

    else :
        l1sellerror.place(x=190,y=170)


def custfunc():
    l1.config(text="لطفا اسم کاربری خود را انتخاب کنید")
    optionmenu_widget.place(x=228,y=70)
    butokcust.place(x=233,y=135)
    loginCustomer.place(x=1000,y=1000)
    loginSeller.place(x=1000,y=1000)

def sellfunc():
    l1.config(text="لطفا رمز عبور امنیتی را وارد کنید")

    butoksell.place(x=233,y=100)
    loginCustomer.place(x=1000,y=1000)
    loginSeller.place(x=1000,y=1000)
    pass_entry.place(x=180,y=65)



loginwindow.geometry("500x310")
loginwindow.resizable(0,0)
l1=tkinter.Label(loginwindow, text="لطفا نوع کاربری را مشخص کنید",font=("",14))
l1.place(x=147,y=10)
l1custerror=tkinter.Label(loginwindow,text="مشتری با این کد وجود ندارد",bg="red",font=("",13))
l1custerror.place(x=1000,y=1000)
l1sellerror=tkinter.Label(loginwindow,text="رمز عبور اشتباه میباشد",bg="red",font=("",13))
l1sellerror.place(x=1000,y=1000)

butokcust = Button(loginwindow,text="ok",bg="green",command=ok_login_cust,font=("",13))
butokcust.place(x=1000,y=1000)
butoksell = Button(loginwindow,text="ok",bg="green",command=ok_login_sell,font=("",13))
butoksell.place(x=1000,y=1000)
butcustfactor = Button(loginwindow,text="فاکتور گیری از خرید های اخیر شما",command=cust_factor,bg="pink",height = 3,font=("", '15'))
butcustfactor.place(x=1000,y=1000)



sell_custfactor =Button(loginwindow,text="تراکنش های مربوط به مشتری",bg="red",height=2,width=35,font=("",13),command=sell_custfactorfunc)
sell_custfactor.place(x=1000,y=1000)

make_transaction =Button(loginwindow,text="افزودن تراکنش",bg="purple",height=2,width=35,font=("",13),command=maketrans_func)
make_transaction.place(x=1000,y=1000)

delete_transaction =Button(loginwindow,text="حذف تراکنش",bg="orange",height=2,width=35,font=("",13),command=delfunc)
delete_transaction.place(x=1000,y=1000)

shop_stuff =Button(loginwindow,text="اقلام موجود در فروشگاه",bg="green",height=2,width=35,font=("",13),command=shopstuff_func)
shop_stuff.place(x=1000,y=1000)

shop_transaction =Button(loginwindow,text="تراکنش های یک شعبه خاص",bg="blue",height=2,width=35,font=("",13),command = shoptrans_func)
shop_transaction.place(x=1000,y=1000)


#sell_custfactorfunc widgets  11
l11=tkinter.Label(loginwindow, text="لطفا مشتری را انتخاب کنید",font=(",15"))
l11.place(x=1000,y=1000)
entry11 =  Entry(loginwindow)
entry11.place(x=1000,y=1000)
but11 = Button(loginwindow,text="ok",bg="green",font=("",13),command=but11func)
but11.place(x=1000,y=1000)
back11 = Button(loginwindow,text="back",bg="red",font=("",10),command=back11func)
back11.place(x=1000,y=1000)
error11=tkinter.Label(loginwindow, text="مشتری با این کد موجود نیست",font=(",13"),bg="red")
error11.place(x=1000,y=1000)


#make transaction widgwts 12
l12=tkinter.Label(loginwindow, text="لطفا اطلاعات درخواستی را به درستی وارد کنید",font=(",15"))
l12.place(x=1000,y=1000)
but12 = Button(loginwindow,text="ok",bg="green",font=("",13),command=but12func)
but12.place(x=1000,y=1000)
back12 = Button(loginwindow,text="back",bg="red",font=("",10),command=back12func)
back12.place(x=1000,y=1000)

l121=tkinter.Label(loginwindow, text="کد تراکنش ",font=(",13"))
l121.place(x=1000,y=1000)
entry121 =  Entry(loginwindow)
entry121.place(x=1000,y=1000)

l122=tkinter.Label(loginwindow, text="کد مشتری",font=(",13"))
l122.place(x=1000,y=1000)
entry122 =  Entry(loginwindow)
entry122.place(x=1000,y=1000)

l123=tkinter.Label(loginwindow, text="کد شعبه",font=(",13"))
l123.place(x=1000,y=1000)
entry123 =  Entry(loginwindow)
entry123.place(x=1000,y=1000)

l124=tkinter.Label(loginwindow, text="تاریخ",font=(",13"))
l124.place(x=1000,y=1000)
entry124 =  Entry(loginwindow)
entry124.place(x=1000,y=1000)

l125=tkinter.Label(loginwindow, text="زمان",font=(",13"))
l125.place(x=1000,y=1000)
entry125 =  Entry(loginwindow)
entry125.place(x=1000,y=1000)

l126=tkinter.Label(loginwindow, text="قیمت",font=(",13"))
l126.place(x=1000,y=1000)
entry126 =  Entry(loginwindow)
entry126.place(x=1000,y=1000)



#delet trensaction widgets 13
l13=tkinter.Label(loginwindow, text="لطفاکد تراکنش را وارد کنید",font=(",15"))
l13.place(x=1000,y=1000)
entryDel =  Entry(loginwindow)
entryDel.place(x=1000,y=1000)
but13 = Button(loginwindow,text="ok",bg="green",font=("",13),command=but13func)
but13.place(x=1000,y=1000)
back13 = Button(loginwindow,text="back",bg="red",font=("",10),command=back13func)
back13.place(x=1000,y=1000)



#shop stuff widgets 14
l14=tkinter.Label(loginwindow, text="لطفاکد فروشگاه را انتخاب کنید",font=(",15"))
l14.place(x=1000,y=1000)
entry14 =  Entry(loginwindow)
entry14.place(x=1000,y=1000)
but14 = Button(loginwindow,text="ok",bg="green",font=("",13),command=but14func)
but14.place(x=1000,y=1000)
back14 = Button(loginwindow,text="back",bg="red",font=("",10),command=back14func)
back14.place(x=1000,y=1000)
error14=tkinter.Label(loginwindow, text="فروشگاهی با این کد موجود نیست",font=(",13"),bg="red")
error14.place(x=1000,y=1000)


#shop transaction factor widgets 15
l15=tkinter.Label(loginwindow, text="لطفا اسم شعبه را انتخاب کنید",font=(",15"))
l15.place(x=1000,y=1000)
entry15 =  Entry(loginwindow)
entry15.place(x=1000,y=1000)
but15 = Button(loginwindow,text="ok",bg="green",font=("",13),command=but15func)
but15.place(x=1000,y=1000)
back15 = Button(loginwindow,text="back",bg="red",font=("",10),command=back15func)
back15.place(x=1000,y=1000)
error15=tkinter.Label(loginwindow, text="شعبه ای با این کد موجود نیست",font=(",13"),bg="red")
error15.place(x=1000,y=1000)



pass_value =StringVar()
pass_entry = Entry(loginwindow)
pass_entry.place(x=1000,y=1000)

control_variable = tkinter.StringVar(loginwindow)
#باید اسم مشتری ها از پایگاه داده در بیاید و در این تاپل ذخیره شود
OPTION_TUPLE = ("مشتری 1", "مشتری 2", "مشتری 3")
optionmenu_widget = tkinter.OptionMenu(loginwindow,
                     control_variable, *OPTION_TUPLE)
optionmenu_widget.pack()
optionmenu_widget.place(x=1000,y=1000)
l01=tkinter.Label(loginwindow, text="اسم مشتری",font=(",15"))
l01.place(x=1000,y=1000)

control_variable1 = tkinter.StringVar(loginwindow)
#باید اسم شعبه ها از پایگاه داده بدست اید  و در تاپل زیر ذخیره شود
branch_TUPLE =("شعبه تبریز","شعبه همدان","شعبه جلفا")
optionmenu1_widget = tkinter.OptionMenu(loginwindow,
                     control_variable1, *branch_TUPLE)
optionmenu1_widget.pack()
optionmenu1_widget.place(x=1000,y=1000)


control_variable2 = tkinter.StringVar(loginwindow)
#باید کد فروشگاه ها از پایگاه داده بدست اید و در تاپل زیر ذخیره شود
shop_TUPLE =(123,174,203)
optionmenu2_widget = tkinter.OptionMenu(loginwindow,
                     control_variable2, *shop_TUPLE)
optionmenu2_widget.pack()
optionmenu2_widget.place(x=1000,y=1000)


loginCustomer = Button(loginwindow,text="مشتری",bg="yellow",command=custfunc,font=("",14))
loginSeller = Button(loginwindow,text="فروشنده",bg="yellow",command=sellfunc,font=("",14))
loginCustomer.place(x=173,y=65)
loginSeller.place(x=273,y=65)

loginwindow.mainloop()
