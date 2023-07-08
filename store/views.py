from asyncio.windows_events import NULL
from contextlib import nullcontext
from pickle import TRUE
from django.shortcuts import redirect, render

from .models import customer,product, seller, soldproduct


# Create your views here.
def index(request):
       x=product.objects.all()
       return render(request,'index.html',{'user':False,'product':x})


def login(request):
    val=0
    if request.method == 'POST':
      username=request.POST['username']
      password=request.POST['password']
      
      x=customer.objects.all()
      for i in x:
         if i.username==username and i.password1==password:
            x=product.objects.all()
            return render(request,'index.html',{'user':TRUE,'product':x,'userid':i.id})
         
      else:
        return render(request,'login.html',{'value':100})
    else:
     return render(request,'login.html',{'value':NULL})

   
def edit(request,userid):
   u=customer.objects.get(id=userid)
   return render(request,'edit.html',{'user':u})

def addedit(request,userid):
   fname=request.POST['fname']
   lname=request.POST['lname']
   mobile=request.POST['mobile']
   address=request.POST['address']
   pincode=request.POST['pincode']
   username=request.POST["username"]
   u=customer.objects.get(id=userid)
   u.fname=fname
   u.lname=lname
   u.mobile=mobile
   u.address=address
   u.pincode=pincode
   u.username=username
   u.save()
   x=customer.objects.get(id=userid)
   y=soldproduct.objects.filter(cid=userid)
   return render(request,'account.html',{'user':x,'product':y}) 
  


def register(request):
   if request.method == 'POST':
      fname=request.POST['fname']
      lname=request.POST['lname']
      address=request.POST['address']
      pincode=request.POST['pincode']
      mobile=request.POST['mobile']
      username=request.POST['username']
      email=request.POST['email']
      password1=request.POST['password1']
      password2=request.POST['password2']
      if password1==password2:
          user=customer(fname=fname,lname=lname,address=address,pincode=pincode,mobile=mobile,username=username,email=email,password1=password1)
          user.save()
          x=product.objects.all()
          return render(request,'index.html',{user:TRUE,'product':x,'userid':user.id})
      return render(request,'register.html',{'invalid':100})
   else:
      return render(request,'register.html')


def logout(request):
       return redirect('/')


def products(request,id):
   obj=[]
   x=product.objects.get(id=id)
   obj.append(x)
   return render(request,'products.html',{'products':obj})


def search(request):
   obj=[]
   x=request.POST['name']
   y=product.objects.all()
   try:
      for i in y:
        if ((x.lower() == i.name.lower()) | (x.lower() == i.type.lower())) :
          obj.append(i)    
      return render(request,'products.html',{'products':obj})
   except:
      return redirect('/')



def sellerlogin(request):
    user=0
    obj=[]
    if request.method == 'POST':
      username=request.POST['username']
      password=request.POST['password']
      x=seller.objects.all()
      for i in x:
         if i.username==username and i.password1==password:
            j=i
            user=user+1
      if user !=0 :
         y=product.objects.all()
         for k in y:
            if k.sellerid==j:
               obj.append(k)
         return render(request,'seller.html',{'product':obj,'user':j})
      else:
        return render(request,'sellerlogin.html',{'value':100})
    else:
     return render(request,'sellerlogin.html',{'value':NULL})



def sellerregister(request):
   obj=[]
   if request.method == 'POST':
      name=request.POST['name']
      address=request.POST['address']
      mobile=request.POST['mobile']
      username=request.POST['username']
      email=request.POST['email']
      password1=request.POST['password1']
      password2=request.POST['password2']
      if password1==password2:
          user=seller(name=name,address=address,mobile=mobile,username=username,email=email,password1=password1)
          user.save()
          y=product.objects.all()
          for k in y:
            if k.sellerid==user:
               obj.append(k)
          return render(request,'seller.html',{'product':obj,'user':user})
      return render(request,'sellerregister.html',{'invalid':100})
   else:
      return render(request,'sellerregister.html')


def sellerlogout(request):
   return redirect('/')


def buy(request,productid,customerid):
   u=[]
   quantity=1
   x=product.objects.all()
   y=customer.objects.all()
   for i in x:
      if i.id == productid:
         a=i
   for j in y:
      if j.id == customerid:
         b=j
   if a.quantity>=quantity:
      try:
        sell=soldproduct(pid=a,cid=b,quantitywished=quantity,cost=a.cost)
        sell.save()
        u.append(sell)

        a.quantity=a.quantity-quantity
        if a.quantity==0 :
            a.delete()
        else:
           a.save()
      except:
         p=soldproduct.objects.get(pid=productid,cid=customerid)
         p.quantitywished=p.quantitywished+quantity
         p.cost=p.cost+a.cost
         p.save()
         a.quantity=a.quantity-quantity
         if a.quantity==0 :
            a.delete()
         else:
           a.save()
         u.append(p)
      msg="Thank you for buying Keep on shopping"
   else:
      msg="product not available"    
   q=soldproduct.objects.all()
   for i in q:
         if i.id==(u[0]).id:
            r=u[0]
   return render(request,'buyproduct.html',{'msg':msg,'customer':b,'product':a})

def buy1(request,productid,customerid):
  u=[]
  quantity=1
  x=product.objects.all()
  y=customer.objects.all()
  for i in x:
    if i.id == productid:
         a=i
  for j in y:
      if j.id == customerid:
         b=j
  if request.method!='POST':
    return render(request,'buy.html',{'product':a,'customer':b})
  else:
   if a.quantity>=quantity:
      try:
        sell=soldproduct(pid=a,cid=b,quantitywished=quantity,cost=a.cost)
        sell.save()
        u.append(sell)

        a.quantity=a.quantity-quantity
        if a.quantity==0 :
            a.delete()
        else:
           a.save()
        
      except:
         p=soldproduct.objects.get(pid=productid,cid=customerid)
         p.quantitywished=p.quantitywished+quantity
         p.cost=p.cost+a.cost
         p.save()
         u.append(p)
 
   q=soldproduct.objects.all()
   for i in q:
         if i.id==(u[0]).id:
            r=u[0]
   return redirect('/')








def account(request,userid):
   y=[]
   x=customer.objects.get(id=userid)
   y=soldproduct.objects.filter(cid=userid)
   return render(request,'account.html',{'user':x,'product':y})

def selleraccount(request,userid):
   x=seller.objects.get(id=userid)
   return render(request,'selleraccount.html',{'user':x})

def addproduct(request):
   x=seller.objects.all()
   return render(request,'addproduct.html',{'user':x})


def add(request):
   if request.method == 'POST':
      name=request.POST['name']
      type=request.POST['type']
      desc=request.POST['description']
      quantity=request.POST['quantity']
      cost=request.POST['cost']
      sellerid=request.POST['sellerid']
      sell=seller.objects.get(id=sellerid)
      add=product(name=name,type=type,quantity=quantity,description=desc,cost=cost,sellerid=sell)
      add.save()
      obj=[]
      y=product.objects.all()
      for k in y:
         if k.sellerid==sell:
            obj.append(k)
      message="Product added succesfully"
      return render(request,'seller.html',{'product':obj,'user':sell,'msg':message})
   

def delete(request,pid,uid):
   x=product.objects.get(id=pid)
   y=seller.objects.get(id=uid)
   z=product.objects.all()
   x.delete()
   obj=[]
   for k in z:
         if k.sellerid==y:
            obj.append(k)
   message="product deleted successfully"
   return render(request,'seller.html',{'product':obj,'user':y,'msg':message})


def cart(request):
   return render(request,'cart.html')
















