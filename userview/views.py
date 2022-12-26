from multiprocessing import context
import math 
from django.shortcuts import render, redirect
from .models import *
from MSY.forms import *
from userview.models import *
from django.shortcuts import get_object_or_404
from sklearn.linear_model import LinearRegression
from django.db.models import Count
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.conf import settings


from userview.forms import *


from django.http import HttpResponse
import os

def user (request):
    datamsy = dataikan.objects.all()
    template = "user.html"
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
    return render (request,template, context)

def table (request):
    datamsy = dataikan.objects.all()
    template = "tablemsy.html"
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
    return render (request,template, context)

def chart (request):
    datamsy = dataikan.objects.all()
    template = "chart.html"
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
    return render (request,template, context)
 
def about (request):
    template = "about.html"
    context ={
        "title"   : "About",
        "heading" : "Tentang Pembuat",
    }
    return render (request,template, context)

from django.shortcuts import render, redirect

def send_fax (request):
    if request.POST:
        form = FaxForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['alert'] = "Berhasil mengirim pesan ke admin!"
            return redirect('/user/')
        else : 
            return redirect('/adm/')

def persebaran(request):
    uploaded_file = UploadedFile.objects.all()
    for obj in uploaded_file:
        name = obj.name
    nama = name
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('persebaran')
    else:
        form = UploadFileForm()
    context = {
        "form": form,
        "name" : nama,
        
        }
    return render(request, 'persebaran.html',context)

# def gis(request):
#     gis = GIS("https://www.arcgis.com", key="your_api_key")
#     items = gis.content.search(query="title: GeoJSON File", item_type="GeoJSON")
#     item = items[0]
#     geojson_file = item.download()
#     with open("geojson.json", "w") as f:
#         f.write(geojson_file.read().decode())
#     import json
#     with open("geojson.json", "r") as f:
#         geojson = json.load(f)
#     context = {
#         "geojson": geojson
#     }
#     return render(request, "map.html", context)


# def gis(request):
#     with open('static/json/Klorofil_A_1.js', 'r') as f:
#         geojson = json.load(f)
#     context = {
#         'geojson': geojson,
#     }
#     return render(request, 'map.html', context)






    # file_path = UploadedFile.file.path
    # if os.path.exists(file_path):
    #     with open(file_path, 'rb') as fh:
    #         response = HttpResponse(fh.read(), content_type="application/force-download")
    #         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
    #         return response
        # raise Http404