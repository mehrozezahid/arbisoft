from django.core.urlresolvers import reverse
from django.db.models import Max, Min, F
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

import os

# Create your views here.
from myapp.models import Filename, Filedata


def index(request):

    context = RequestContext(request)

    #path = p
    path = '/home/mahrozezahid/Documents/PyCharmProjects/Tasks/weatherdata'
    raw_data = {}
    monthly_data = {}
    keys_index = []

    if request.method == 'POST':

        raw_data = read_files(path)

        monthly_data, keys_index = formatting(raw_data)

        insert_filenames(raw_data)

        insert_filedata(monthly_data)

        return HttpResponseRedirect(reverse('myapp:menu'))

    else:

        return render_to_response(
            'myapp/index.html', context
        )


def menu(request):

    context = RequestContext(request)

    if request.method == 'POST':

        if request.POST.get("report1"):
            return HttpResponseRedirect(reverse('myapp:report1'))

        elif request.POST.get("report2"):  # You can use else in here too if there is only 2 submit types.
            return HttpResponseRedirect(reverse('myapp:report2'))

    return render_to_response(
        'myapp/menu.html', context
    )


def report1(request):

    context = RequestContext(request)

    result = {}

    # file_names = Filename.objects.all()

    # for name in file_names:
    #
    #     print(name)
    #
    #     days = Filedata.objects.filter(file_name__file_name=name)
    #     da = days.filter(file_name__file_name__contains='2000')
    #
    #     #print da
    #
    #     for d in da:
    #         print d.file_name, d.pkt, d.max_temperaturec
    #
    #     break


    years = Filedata.objects.all().values_list('year').distinct()
    for y in years:

        days = Filedata.objects.filter(year=y[0])
        d1 = days.latest('max_temperaturec')
        d2 = days.latest('max_humidity')
        d3 = days.order_by('-min_temperaturec').first()

        print y, d1.year, d1.max_temperaturec, d2.year, d2.max_humidity, d3.year, d3.min_temperaturec

    return render_to_response(
        'myapp/report1.html',
        {'data': []}, context
    )


def read_files(path):
    '''reading all input data files from directory'''

    data = {}

    for dir_entry in os.listdir(path):
        dir_entry_path = os.path.join(path, dir_entry)
        if os.path.isfile(dir_entry_path):
            with open(dir_entry_path, 'r') as my_file:
                data[dir_entry] = my_file.read()

    return data


def formatting(data):
    '''Formatting the raw data into ordered key value pairs so that
    values can easily be read'''

    temp_dict_1 = {}
    monthly_data = {}
    keys_index = []

    # first loop for data formatting
    for entry_key, entry_value in data.items():

        # year = entry_key.split("_")[2]
        # month = entry_key.split("_")[3]
        # month = month.split(".")[0]

        temp_dict_1 = entry_value.splitlines()
        monthly_data[entry_key] = temp_dict_1[0:]

        temp_dict_1 = []       # emptying temporary list for next iteration

    # print(monthly_data)

    # removing file header and footer for each file
    for key, value in monthly_data.items():

        monthly_data[key] = value[1:-1]

    #print(monthly_data)

    # splitting measurements string for each day into separate values
    for key, value in monthly_data.items():

        for k in range(len(value)):

            value[k] = value[k].split(",")

            if k == 0:

                for j in value[k]:
                    keys_index.append(j)

        monthly_data[key] = value[1:]

    #print(keys_index)
    return (monthly_data, keys_index)


def insert_filenames(raw_data):

    keys = []
    keys = raw_data.keys()

    for i in keys:

        p = Filename(file_name=i)
        p.save()


def insert_filedata(data):

    objects = []

    # for each file name that exists
    for key, value in data.items():

        # get the corresponding foreign key object that exists in Filename table in db
        filename = Filename.objects.get(file_name=key)

        print(filename)

        # getting the year from file name
        yr = int(str(filename).split("_")[2])

        print yr

        for i in value:

            objects.append(Filedata(file_name=filename, year=yr, pkt=i[0],
                                    max_temperaturec=int(i[1]) if i[1].isdigit() else None,
                                    mean_temperaturec=int(i[2]) if i[2].isdigit() else None,
                                    min_temperaturec=int(i[3]) if i[3].isdigit() else None,
                                    dew_pointc=int(i[4]) if i[4].isdigit() else None,
                                    meandew_pointc=int(i[5]) if i[5].isdigit() else None,
                                    mindew_pointc=int(i[6]) if i[6].isdigit() else None,
                                    max_humidity=int(i[7]) if i[7].isdigit() else None,
                                    mean_humidity=int(i[8]) if i[8].isdigit() else None,
                                    min_humidity=int(i[9]) if i[9].isdigit() else None,
                                    max_sea_level_pressurehPa=int(i[10]) if i[10].isdigit() else None,
                                    mean_sea_level_pressurehPa=int(i[11]) if i[11].isdigit() else None,
                                    min_sea_level_pressurehPa=int(i[12]) if i[12].isdigit() else None,
                                    max_visibilityKm=int(i[13]) if i[13].isdigit() else None,
                                    mean_visibilityKm=int(i[14]) if i[14].isdigit() else None,
                                    min_visibilityKm=int(i[15]) if i[15].isdigit() else None,
                                    max_wind_speedKmh=int(i[16]) if i[16].isdigit() else None,
                                    mean_wind_speedKmh=int(i[17]) if i[17].isdigit() else None,
                                    max_gust_speedkmh=int(i[18]) if i[18].isdigit() else None,
                                    precipitationcm=float(i[19]) if i[19].isdigit() else None,
                                    cloud_cover=int(i[20]) if i[20].isdigit() else None,
                                    events=i[21],
                                    wind_dir_degrees=int(i[22]) if i[22].isdigit() else None
                                    ))

    Filedata.objects.bulk_create(objects)
    # Filedata.objects.all().delete()
    # Filename.objects.all().delete()


