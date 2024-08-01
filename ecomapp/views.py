from django.shortcuts import render,redirect
from .models import  CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User,auth
from ecomapp.models import category
from ecomapp.models import product,usermember,cart
from django.contrib import messages



# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def admin_home(request):
    return render(request,'admin_home.html')

@login_required(login_url='login')
def checkout(request):
    return render(request,'checkout.html')

@login_required(login_url='login')
def category1(request):
    return render(request,'category.html')

@login_required(login_url='login')
def products(request):
    ct=category.objects.all()
    return render(request,'product.html',{'ct':ct})


def user_login(request):
    
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['passwd']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.user_type == '1':
                login(request,user)
                return redirect('admin_home')
            
            else:
                login(request,user)
                messages.info(request,f'welcome {username}')
                return redirect('user_home')
        else:
            return redirect('/')
    return render(request,'home.html')
    
@login_required(login_url='login')
def add_category(request):
    if request.method=='POST':
        cat=request.POST['cat']
        c=category(category=cat)
        c.save()
        return redirect('admin_home')

@login_required(login_url='login')
def add_product(request):
    if request.method=='POST':
        pname=request.POST['pname']
        pdesc=request.POST['pdesc']
        price=request.POST['price']
        pimg=request.FILES['file']
        sel=request.POST['sel']
        cs=category.objects.get(id=sel)
        p=product(pname=pname,desc=pdesc,price=price,pimage=pimg,category1=cs)
        p.save()
    return redirect('admin_home')

@login_required(login_url='login')
def show_product(request):
    pdts=product.objects.all()
    return render(request,'show_product.html',{'pdts':pdts})

@login_required(login_url='login')
def deletepage(request,pk):
    pts=product.objects.get(id=pk)
    pts.delete()
    return redirect('show_product')

def reg(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['uname']
        password=request.POST['passwd']
        cpassword=request.POST['cpasswd']
        utype=request.POST['utype']
        
        dob=request.POST['dob']
        email=request.POST['email']
        city=request.POST['city']
        
        contact=request.POST['phno']
        
        
        if password==cpassword:
            if CustomUser.objects.filter(username=username).exists():
                
                return redirect('home')
            else:
                user=CustomUser.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    username=username,
                    email=email,
                    password=password,
                    user_type=utype
                )
                user.save()
                uid=CustomUser.objects.get(id=user.id)
                tr=usermember(user=uid,dob=dob,number=contact,city=city)
                tr.save()
        return redirect('home')

@login_required(login_url='login')
def user_home(request):
    current_user=request.user.id
    user1=usermember.objects.get(user_id=current_user)
    cat=category.objects.all()
    return render(request,'user_home.html',{'users':user1,'cat':cat})

@login_required(login_url='login')

def view_user(request):
    ur=usermember.objects.all()
    return render(request,'view_user.html',{'ur':ur})

@login_required(login_url='login')
def delete_user(request,pk):
    
    u=usermember.objects.get(id=pk)
    c=CustomUser.objects.get(id=u.user_id)
    
    u.delete()
    c.delete()
    return redirect('view_user')

@login_required(login_url='login')
def show(request,id):
    pro=product.objects.filter(category1=id)
    cat=category.objects.get(id=id)
    cat1=category.objects.all()
    return render(request,'show.html',{'pro':pro,'c':cat,'cat':cat1})

@login_required(login_url='login')
def add_cart(request,id):
    pr=product.objects.get(id=id)
    
    user=request.user
    # item=cart(prod=pr,user=user)
    item,created=cart.objects.get_or_create(user=user,prod=pr)
    if not created:
        item.quantity+=1
        item.save()
    item1=cart.objects.filter(user=user)
    return redirect('view_cart')


@login_required(login_url='login')
def remove(request,id):
    c=cart.objects.get(id=id)
    c.delete()
    return redirect('view_cart')

@login_required(login_url='login')
def view_cart(request):
    user=request.user
    item1=cart.objects.filter(user=user)
    total_pr=sum(item.total_price() for item in item1)
    ct=cart.objects.filter(user_id=user).count()
    return render(request,'cart.html',{'items':item1,'tot':total_pr,'cou':ct})
    
@login_required(login_url='login')
def logout(request):
    
    auth.logout(request)
    return redirect('home')


@login_required(login_url='login')
def cartincrement(request,id):
    cart_item=cart.objects.get(prod_id=id,user=request.user)
    cart_item.quantity +=1
    cart_item.save()
    return redirect('view_cart')

@login_required(login_url='login')
def cartdecrement(request,id):
    cart_item=cart.objects.get(prod_id=id,user=request.user)
    cart_item.quantity -=1
    cart_item.save()
    return redirect('view_cart')



# @login_required(login_url='login')
# def pay(request):
#     messages.info(request,"Payment Successful, \n Your order is placed")
#     return redirect('checkout')
            
    
        
