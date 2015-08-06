from django.core.urlresolvers import reverse
from django.db.models import Min
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from myapp.models import Filename, Filedata

import os


def index(request):

    context = RequestContext(request)

    if request.method == 'POST':

        path = request.POST['path']
        raw_data = read_files(path)

        monthly_data, keys_index = formatting(raw_data)

        insert_filenames(raw_data)

        insert_filedata(monthly_data, keys_index)

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

    result = report1_calc()

    return render_to_response(
        'myapp/report1.html',
        {'data': result}, context
    )


def report2(request):

    context = RequestContext(request)

    result = report2_calc()

    return render_to_response(
        'myapp/report2.html',
        {'data': result}, context
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
    """Formatting the raw data into ordered key value pairs so that
    values can easily be read"""

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

    keys = raw_data.keys()

    for i in keys:

        p = Filename(file_name=i)
        p.save()


def insert_filedata(data, keys_index):

    objects = []

    # for each file name that exists
    for key, value in data.items():

        # get the corresponding foreign key object that exists in Filename table in db
        filename = Filename.objects.get(file_name=key)

        # getting the year from file name
        yr = int(str(filename).split("_")[2])

        for i in value:

            objects.append(Filedata(file_name=filename, year=yr, pkt=i[keys_index.index('PKT')],
                                    max_temperaturec=int(i[keys_index.index('Max TemperatureC')]) if i[keys_index.index('Max TemperatureC')].isdigit() else None,
                                    mean_temperaturec=int(i[keys_index.index('Mean TemperatureC')]) if i[keys_index.index('Mean TemperatureC')].isdigit() else None,
                                    min_temperaturec=int(i[keys_index.index('Min TemperatureC')]) if i[keys_index.index('Min TemperatureC')].isdigit() else None,
                                    dew_pointc=int(i[keys_index.index('Dew PointC')]) if i[keys_index.index('Dew PointC')].isdigit() else None,
                                    meandew_pointc=int(i[keys_index.index('MeanDew PointC')]) if i[keys_index.index('MeanDew PointC')].isdigit() else None,
                                    mindew_pointc=int(i[keys_index.index('Min DewpointC')]) if i[keys_index.index('Min DewpointC')].isdigit() else None,
                                    max_humidity=int(i[keys_index.index('Max Humidity')]) if i[keys_index.index('Max Humidity')].isdigit() else None,
                                    mean_humidity=int(i[keys_index.index(' Mean Humidity')]) if i[keys_index.index(' Mean Humidity')].isdigit() else None,
                                    min_humidity=int(i[keys_index.index(' Min Humidity')]) if i[keys_index.index(' Min Humidity')].isdigit() else None,
                                    max_sea_level_pressurehPa=int(i[keys_index.index(' Max Sea Level PressurehPa')]) if i[keys_index.index(' Max Sea Level PressurehPa')].isdigit() else None,
                                    mean_sea_level_pressurehPa=int(i[keys_index.index(' Mean Sea Level PressurehPa')]) if i[keys_index.index(' Mean Sea Level PressurehPa')].isdigit() else None,
                                    min_sea_level_pressurehPa=int(i[keys_index.index(' Min Sea Level PressurehPa')]) if i[keys_index.index(' Min Sea Level PressurehPa')].isdigit() else None,
                                    max_visibilityKm=int(i[keys_index.index(' Max VisibilityKm')]) if i[keys_index.index(' Max VisibilityKm')].isdigit() else None,
                                    mean_visibilityKm=int(i[keys_index.index(' Mean VisibilityKm')]) if i[keys_index.index(' Mean VisibilityKm')].isdigit() else None,
                                    min_visibilityKm=int(i[keys_index.index(' Min VisibilitykM')]) if i[keys_index.index(' Min VisibilitykM')].isdigit() else None,
                                    max_wind_speedKmh=int(i[keys_index.index(' Max Wind SpeedKm/h')]) if i[keys_index.index(' Max Wind SpeedKm/h')].isdigit() else None,
                                    mean_wind_speedKmh=int(i[keys_index.index(' Mean Wind SpeedKm/h')]) if i[keys_index.index(' Mean Wind SpeedKm/h')].isdigit() else None,
                                    max_gust_speedkmh=int(i[keys_index.index(' Max Gust SpeedKm/h')]) if i[keys_index.index(' Max Gust SpeedKm/h')].isdigit() else None,
                                    precipitationcm=float(i[keys_index.index('PrecipitationCm')]) if i[keys_index.index('PrecipitationCm')].isdigit() else None,
                                    cloud_cover=int(i[keys_index.index(' CloudCover')]) if i[keys_index.index(' CloudCover')].isdigit() else None,
                                    events=i[keys_index.index(' Events')],
                                    wind_dir_degrees=int(i[keys_index.index('WindDirDegrees')]) if i[keys_index.index('WindDirDegrees')].isdigit() else None
                                    ))

    Filedata.objects.bulk_create(objects)
    # Filedata.objects.all().delete()
    # Filename.objects.all().delete()


def report1_calc():

    result = {}

    years = Filedata.objects.all().values_list('year').distinct()

    for y in years:

        days = Filedata.objects.filter(year=y[0])
        d1 = days.latest('max_temperaturec')
        d2 = days.latest('max_humidity')
        d3 = days.filter(min_temperaturec__isnull=False).values_list('min_temperaturec').annotate(Min('min_temperaturec')).order_by('min_temperaturec')[0]
        d4 = days.filter(min_humidity__isnull=False).values_list('min_humidity').annotate(Min('min_humidity')).order_by('min_humidity')[0]

        result[d1.year] = {'max_temp': d1.max_temperaturec, 'min_temp': d3[0],
                           'max_humidity': d2.max_humidity, 'min_humidity': d4[0]}

    return result


def report2_calc():

    result = {}

    years = Filedata.objects.all().values_list('year').distinct()

    for y in years:

        days_in_year = Filedata.objects.filter(year=y[0])
        hottest_day = days_in_year.latest('max_temperaturec')

        result[hottest_day.year] = {'Date': hottest_day.pkt, 'Temp': hottest_day.max_temperaturec}

    print result
    return result
