from django.shortcuts import render,redirect
from .models import Packages, Prediction
#from . import ml_code as ml
from django.contrib.auth.models import User,auth
from django.contrib import messages 
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
# Create your views here.
def index1(request):
    return render(request,"index1.html")

def about(request):
    return render(request,"about.html")

def register(request):
    if(request.method=="POST"):
        
        username=request.POST['username']
        email=request.POST['email']
    
        pwd=request.POST['pwd']
        pwd1=request.POST['pwd1']
        if pwd==pwd1:
          if User.objects.filter(username=username).exists():
              messages.info(request,'Username Taken')
              return redirect('register')
          
          elif User.objects.filter(email=email).exists():
              messages.info(request,'Email already registered')
              return redirect('register')
          else:
              user=User.objects.create_user(username=username,email=email,password=pwd)
              user.save();
              messages.info(request,'Registered Successfully')
              return redirect('login')
        else:
              messages.info(request,'Password Not Matching')
              return redirect('register')
    
    
    return render(request,"register.html")

def login(request):
    if (request.method=="POST"):
     username=request.POST['username']   
     pwd=request.POST['pwd']
     
     user=auth.authenticate(username=username, password=pwd)
     print(user)
     if user is not None:
         auth.login(request,user)
         return render(request,"prediction.html")
     else:
         messages.info(request,'Invalid Credentials')
         return redirect('login')
     
    return render(request,"login.html")

def packages(request):
    p=Packages.objects.all()
    return render(request,"packages.html",{"p":p})

def resetpassword(request):

    if (request.method=="POST"):
        
         username=request.POST['username']   
         pwd=request.POST['newpassword']
         user=User.objects.filter(username=username).exists()
         print(user)
         if user:
               u = User.objects.get(username=username)
               u.set_password(pwd)
               u.save()
               messages.info(request,'Password Changed Successfully !')
               return redirect('login')
         else:
             messages.info(request,'Oops): User Doesnot exist !')
             return redirect('resetpassword')
               
    return render(request,"resetpassword.html")

def contact(request):
    return render(request,"contact.html")
"""

def get_price(bedroom):
    df=pd.read_csv("E:\\Django\\HousePricePrediction\\static\\csv\\Housingdata.csv")
    x=df.drop(["date","id","sqft_lot","sqft_basement","zipcode","sqft_living15","sqft_lot15"],axis=1)
    x.head()
    X=x.drop("price",axis=1)
    y=x[["price"]]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.50)
    reg=LinearRegression()
    reg.fit(X_train,y_train)
    pred=reg.predict(X_test)
    r2_score(pred,y_test)
    sns.heatmap(y.isnull())
    value = reg.predict([[3,2.25,2570,7242,2.0,0,0,3,7,2170,400,1951]])
    print(value)
    return 1

"""
"""
def prediction(request):
    return render(request,"prediction.html")
   bedroom = ''
    if(request.method=="POST"):
        
        bedroom=request.POST['bedroom']
        bathroom=request.POST['bathroom']
        sliving=request.POST['sqft_living']
        sabove=request.POST['sqft_above']
        ybuilt=request.POST['yr_built']
        yrenovated=request.POST['yr_renovated']
        view=request.POST['view']
        floors=request.POST['floors']
        lat=request.POST['lat']
        long=request.POST['long']
        waterfront=request.POST['waterfront']
        grade=request.POST['grade']
        df=pd.read_csv("E:\Django\HousePricePrediction\static\csv\Housingdata.csv")
        X_train=df.drop(["date","id","sqft_lot","sqft_basement","condition","zipcode","sqft_living15","sqft_lot15","price"],axis=1)
        #x.head()
        #X=x.drop("price",axis=1)
        y_train=df[["price"]]
        #X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.50)
        reg=DecisionTreeRegressor()
        reg.fit(X_train,y_train)
        pred=reg.predict([[bedroom,bathroom,sliving,sabove,ybuilt,yrenovated,view,floors,lat,long,waterfront,grade]])
        x=pred
    
        save_data = Prediction(bedroom=bedroom, bathroom=bathroom, sqft_living=sliving, sqft_above=sabove, yr_built=ybuilt, yr_renovated=yrenovated, view=view, floors=floors, lat=lat, long=long, waterfront=waterfront, grade=grade)
        save_data.save()
        return render(request, "result.html",{"bed":bedroom,"bathroom":bathroom,"sliving":sliving,"sabove":sabove,"ybuilt":ybuilt,"yrenovated":yrenovated,"view":view,"floors":floors,"lat":lat,"long":long,"waterfront":waterfront,"grade":grade,"x":x})
    
        #p=Prediction.objects.all()"""
def prediction(request):
    return render(request,"prediction.html")

def result(request):
    bedroom = ''
    if (request.method == "POST"):
        bedroom = request.POST['bedroom']
        bathroom = request.POST['bathroom']
        sliving = request.POST['sqft_living']
        sabove = request.POST['sqft_above']
        ybuilt = request.POST['yr_built']
        yrenovated = request.POST['yr_renovated']
        view = request.POST['view']
        floors = request.POST['floors']
        lat = request.POST['lat']
        long = request.POST['long']
        waterfront = request.POST['waterfront']
        grade = request.POST['grade']
        df = pd.read_csv(r'C:\Users\Udhayakumar\Downloads\HousePricePrediction\HousePricePrediction\static\csv\Housingdata.csv')
        X_train = df.drop(
            ["date", "id", "sqft_lot", "sqft_basement", "condition", "zipcode", "sqft_living15", "sqft_lot15", "price"],
            axis=1)
        # x.head()
        # X=x.drop("price",axis=1)
        y_train = df[["price"]]
        # X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.50)
        reg = DecisionTreeRegressor()
        reg.fit(X_train, y_train)
        pred = reg.predict(
            [[bedroom, bathroom, sliving, sabove, ybuilt, yrenovated, view, floors, lat, long, waterfront, grade]])
        x = pred

        save_data = Prediction(bedroom=bedroom, bathroom=bathroom, sqft_living=sliving, sqft_above=sabove,
                               yr_built=ybuilt, yr_renovated=yrenovated, view=view, floors=floors, lat=lat, long=long,
                               waterfront=waterfront, grade=grade)
        save_data.save()

        return render(request, "result.html",
                      {"bed": bedroom, "bathroom": bathroom, "sliving": sliving, "sabove": sabove, "ybuilt": ybuilt,
                       "yrenovated": yrenovated, "view": view, "floors": floors, "lat": lat, "long": long,
                       "waterfront": waterfront, "grade": grade, "x": x})
        


def logout(request):
    return render(request, 'logout')
        
