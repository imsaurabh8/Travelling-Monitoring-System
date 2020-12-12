from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register,History,Hospital,Feedback,Test
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/TMS/login")
def register(request):
    if request.method=="POST":
        adhaar_number=request.POST.get('adhaar_number')
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone_no = request.POST.get('phone_no')
        age = request.POST.get('age')

        register=Register(adhaar_number=adhaar_number,name=name,email=email,gender=gender,phone_no=phone_no,age=age)

        register.person = request.user
        register.save()


        print(adhaar_number,name,email,gender,phone_no)

    return render(request,'TMS/register.html')

@login_required(login_url="/TMS/login")
def history(request):
    if request.method=="POST":

        source = request.POST.get('source')
        dest = request.POST.get('dest')
        tv_date=request.POST.get('tv_date')
        transportation = request.POST.get('transportation')
        co_pass = request.POST.get('co_pass')

        history = History(source=source,dest=dest,tv_date=tv_date,transportation=transportation,co_pass=co_pass)
        history.person = request.user
        history.save()

        print(source,dest,transportation,co_pass)

    return render(request, 'TMS/history.html')

@login_required(login_url="/TMS/login")
def hospital(request):
    if request.method=="POST":

        name = request.POST.get('name')
        room_no = request.POST.get('room_no')
        room_type=request.POST.get('room_type')
        bill = request.POST.get('bill')

        h1=Hospital(name=name,room_no=room_no,room_type=room_type,bill=bill)
        h1.person=request.user
        h1.save()


        print(name,room_no,room_type,bill)

    return render(request, 'TMS/hospital.html')





@login_required(login_url="/TMS/login")
def feedback(request):
    if request.method=="POST":

        rev1 = request.POST.get('rev1')
        rev2 = request.POST.get('rev2')
        rev3 =request.POST.get('rev3')
        rev4 = request.POST.get('rev4')
        rev5 = request.POST.get('rev5')

        f1=Feedback(covid_days=rev1,hosp_clean=rev2,food_quality=rev3,travel_exp=rev4,improvement=rev5)


        f1.person=request.user
        f1.save()


        print(rev1,rev2,rev3,rev4,rev5)

    return render(request, 'TMS/feedback.html')


@login_required(login_url="/TMS/login")
def test(request):
    if request.method=="POST":

        test_done = request.POST.get('result')
        test_result = request.POST.get('result2')
        quarentined =request.POST.get('result3')

        t1=Test(test_done=test_done,test_result=test_result,quarentined=quarentined)

        t1.person=request.user
        t1.save()


        

    return render(request, 'TMS/test.html')

def signup(request):
    if request.method=="POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)

            return redirect('TMS:UserRegistration')
    else:
        form=UserCreationForm()

    return render(request,'TMS/signup.html',{'form':form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('TMS:UserRegistration')


    else:
        form=AuthenticationForm()
    return render(request, 'TMS/login.html')


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('TMS:login_view')






