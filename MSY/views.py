from multiprocessing import context
import math 
from django.shortcuts import render, redirect
from .models import *
from MSY.forms import *
from django.shortcuts import get_object_or_404
from sklearn.linear_model import LinearRegression
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required(login_url=settings.LOGIN_URL)
def task (request):
    datamsy = dataikan.objects.all()
    context ={
        "title"   : "Ini halaman Homepage",
        "heading" : "Ini halaman Hompe Page",
        "datamsy" : datamsy,
    }
    return render (request,"admin/task.html", context)

@login_required(login_url=settings.LOGIN_URL)
def msy (request):
    datamsy = dataikan.objects.all()
    data = []
    for obj in datamsy:
        data.append({'trip': obj.trip, 'CPUE':obj.CPUE()})
        X = np.array([d['trip'] for d in data]).reshape(-1, 1)
        Y = np.array([d['CPUE'] for d in data]).reshape(-1, 1)
        model = LinearRegression()
        model.fit(X,Y)
        slope = model.coef_
        intercept = model.intercept_
        # Convert the numpy arrays to lists
        slope_list = slope.tolist()
        intercept_list = intercept.tolist()
         # Extract the values from the lists
        slope_value = slope_list[0][0]
        intercept_value = intercept_list[0]
        intercept_value =float(intercept_value)
        slope_value =float(slope_value)
        intercept = float(intercept)
        slope = float(slope)
       # Format the values using the f format code
        equation = "y = {slope:.2f}x + {intercept:.2f}".format(slope=slope_value, intercept=intercept_value)
        # prediksi
        # for TRIP in TRIPS
        #     oprasi = TRIP *(intercept - (slope * TRIP))
    results = []
    pred= results
    last_intercept_value = intercept
    last_slope_value = slope
    result_list = []
    for objs in datamsy:
        TRIP = objs.trip
        result = TRIP*(last_intercept_value-((last_slope_value*(-1))*TRIP))
        results.append(result)
        result_list.append(result)
        zipped= zip(datamsy,result_list)
    for obj, result in zipped:
        obj.result = result
    context ={
        "title"   : "Ini halaman Homepage",
        "heading" : "Ini halaman Hompe Page",
        "datamsy" : datamsy,
        "intercept":intercept,
        "slope"    :slope,
        "equation" :equation,
        "result"   : result,
        "results"   : results,
    }
    return render (request,"msy.html", context)

@login_required(login_url=settings.LOGIN_URL)
def add_data (request):
    template = "admin/adddata.html"
    if request.POST:
        form = Fromdataikan(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form     = Fromdataikan()
            msy_add  ="Tambahkan Data MSY"
            pesan    ="Data Berhasil di Tambahkan"
            context  ={
                "Title" : msy_add,
                "Subtitle" : msy_add,
                "form": form,
                "pesan":pesan,
            }
            return render(request,template,context)

    else:
        form     = Fromdataikan()
        msy_add  ="Tambahkan Data MSY"
        context  ={
                "Title" : msy_add,
                "Subtitle" : msy_add,
                "form": form,
        }
        return render(request, template ,context)
@login_required(login_url=settings.LOGIN_URL)
def up_data(request, id):
    updata = dataikan.objects.get(pk=id)
    edit = "Edit Data MSY"
    template = "admin/updata.html"
    if request.POST:
        form= Fromdataikan(request.POST, request.FILES, instance=updata)
        if form.is_valid():
            form.save()
            pesan = "data berhasil di update"
            context={
                "Title" : edit,
                "Subtitle" : edit,
                "pesan" : pesan,
                "form": form,
                "updata": updata
            }
            return render (request, template ,context)
    else :
        form = Fromdataikan(instance=updata)
        context={
            "Title" : edit,
            "Subtitle" : edit,
            "form": form,
            "updata": updata
        }
        return render (request, template ,context)
@login_required(login_url=settings.LOGIN_URL)
def del_data(request,id):
    deldata= dataikan.objects.get(pk=id)
    deldata.delete()
    return redirect("/task/")

@login_required(login_url=settings.LOGIN_URL)
def file_upload(request):
    uploaded_file = UploadedFile.objects.all()
    for obj in uploaded_file:
        name = obj.name
    nama = name
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('upload')
    else:
        form = UploadFileForm()
    context = {
        "form": form,
        "name" : nama,
        
        }
    return render(request, 'admin/geojson.html',context)




# def user (request):
#     datamsy = dataikan.objects.all()
#     intercepts = []  # create an empty list to store the intercept values
#     for obj in datamsy:
#         intercept = obj.get_intercept()  # call the get_intercept method on each object
#         intercepts.append(intercept)  # append the intercept value to the list
#     context ={
#         "title"   : "Ini halaman Homepage",
#         "heading" : "Ini halaman Hompe Page",
#         "datamsy" : datamsy,
#         "intercepts" : intercepts
#     }
#     return render (request,"user.html", context)


# Create your views here.
# backup



