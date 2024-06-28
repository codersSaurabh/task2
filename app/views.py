from django.shortcuts import render,redirect
from .models import doctor,Patient
def home(request):
    return render(request,"home.html")
# doctor register
def doctorRegister(request):
    if('doctor' in request.session ):
        #return to doctor page
        user=request.session['doctor']
        data=doctor.objects.filter(Username=user).values()[0]  
        return render(request,"profile.html",{"data":data,"profile":"Doctor"} )
    if(request.method=="POST"):
        FName=request.POST.get("Fname","")
        LName=request.POST.get("Lname","")
        Email=request.POST.get("email","")
        Password=request.POST.get("password","")
        CPassword=request.POST.get("cpassword","")
        Country=request.POST.get("country","") 
        Profile=request.FILES['image']
        Username=request.POST.get("Uname","")
        if (Password==CPassword):
            if(len(doctor.objects.filter(Username=Username).values())>0 or len(doctor.objects.filter(Email=Email).values())>0):
                return render(request,"doctorForm.html",{'msg':"Email or Username already exist",'thank':True,"color":"red"})
            Doctor=doctor(FName=FName,LName=LName,Password=Password,Email=Email,Address=Country,Profile=Profile,Username=Username)
            Doctor.save()
            return render(request,"doctorForm.html",{'msg':"Detail has been submitted",'thank':True,"color":"green"})

                
        else:
             return render(request,"doctorForm.html",{'msg':"password not match",'thank':True,"color":"red"})
    return render(request,"doctorForm.html")
#doctor log in
def doctorlogin(request):
         if("doctor" in request.session):
            user=request.session["doctor"]
            data=doctor.objects.filter(Username=user).values()
            return render(request,"profile.html",{"data":data[0],"profile":'Doctor'})
         if(request.method=='POST'):
            
            Username= request.POST.get("Username","") 
            password = request.POST.get("password","")

            data=doctor.objects.filter(Username=Username,Password=password).values() 
            if(len(data)==1):
                    request.session['doctor'] = Username
                    #redirect to doctor page
                    
                    return render(request,"profile.html",{"data":data[0],"profile":'Doctor'})
                            
            else:
               
                 return render(request,'doctorlogin.html',{'msg':'username or password is not valid','thank':True})
                
         return render(request,"doctorlogin.html")
#logout doctor
def doctorlogout(request):
    
    try:
        del request.session['doctor']
    except:
        return redirect("/")
    
    return redirect("/")
#patient Form
def PatientRegister(request):
     if("patient" in request.session):
            user=request.session["patient"]
            data=Patient.objects.filter(Username=user).values()[0]
            return render(request,"profile.html",{"data":data,"profile":'Patient'})
     if(request.method=="POST"): 
            FName=request.POST.get("Fname","")
            LName=request.POST.get("Lname","")
            Email=request.POST.get("email","")
            Password=request.POST.get("password","")
            CPassword=request.POST.get("cpassword","")
            Country=request.POST.get("country","")
            
            Profile=request.FILES["image"]
            Username=request.POST.get("Uname","")
            if (Password==CPassword):
                if(len(doctor.objects.filter(Username=Username,Email=Email).values())>0):
                    return render(request,"patientForm.html",{'msg':"Email or Username already exist",'thank':True,"color":"red"})
                patient=Patient(FName=FName,LName=LName,Password=Password,Email=Email,Address=Country,Profile=Profile,Username=Username)
                patient.save()
                return render(request,"patientForm.html",{'msg':"Detail has been submitted",'thank':True,"color":"green"})         
            else:
             return render(request,"patientForm.html",{'msg':"password not match",'thank':True,"color":"red"})
     return render(request,"patientForm.html")
#patient login
def Patientlogin(request):
         if("patient" in request.session):
            user=request.session["patient"]
            data=Patient.objects.filter(Username=user).values()[0]
            return render(request,"profile.html",{"data":data,"profile":'Patient'})
         if(request.method=='POST'):
            
            Username= request.POST.get("Username","") 
            password = request.POST.get("password","")

            data=Patient.objects.filter(Username=Username,Password=password).values()
            if(len(data)==1):
                    request.session['patient'] = Username
                    #redirect to doctor page
                    
                    return render(request,"profile.html",{"data":data[0],"profile":'Patient'})           
            else:
                 return render(request,'patientlogin.html',{'msg':'username or password is not valid','thank':True})
                
         return render(request,"patientlogin.html")
#logout patient
def patientlogout(request):
    print("hello")
    try:
        del request.session['patient']
    except:
        return redirect("/")
    return redirect("/")
#forgetdoctor
def forgetDoctor(request):
    if(request.method=='POST'):
        Username = request.POST.get("Uname","")  
        password = request.POST.get("password","")
        repassword=request.POST.get('repassword',"")
        if(password==repassword):
            try:
                
                if(request.path=='/doctorlogin/resetpassword/'):
                    data= doctor.objects.get(Username=Username)
                else:
                    data=Patient.objects.get(Username=Username)
                    # print("doctor",doctors)
                if(data):
                    data.Password=password
                    data.save()
                    return render(request,"resetpassword.html",{"msg":"password changed!!",'color':'green'})
                    
            except Exception as e:
                
                return render(request,"resetpassword.html",{'msg':'username does not exist!!','color':'red'})
        else:
         return render(request,"resetpassword.html",{'msg':"Pssword don't match!!",'color':'red'})
    
    return render(request,"resetpassword.html")