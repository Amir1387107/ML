from django.shortcuts import render, HttpResponse
import re
import requests
from bs4 import BeautifulSoup
from .models import Car
# Create your views here.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import normalize
from sklearn.metrics import mean_squared_error, mean_absolute_error, max_error, r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report
from tabulate import tabulate
from IPython.display import display, HTML
from io import StringIO
import prettytable


def ML(request):
    data = Car.objects.all().filter(price__regex=r'^\d+$', name1__icontains='سمند', name1__contains='LX').defer('date_added', 'city', 'details', 'link', 'link2', 'image')

    # df = pd.DataFrame()
    df = pd.DataFrame(data.values(), columns=['name1', 'price', 'km_worked'])
    # for data in data:
    #     df['name1'] = str(data.name1)
    #     df['price'] = int(data.price)
    #     df['km_worked'] = int(data.km_worked)
        # print(f'{str(data.name1)} {int(data.price)} {int(data.km_worked)}')


    x = np.array(df[['km_worked']].iloc[:])

    y = np.array(df['price'].iloc[:])

    # print(x, 'pass', '\n', y)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.01, random_state=0, train_size=0.99)
    # print(x_train, '\n', 'pass', '\n', y_train)

    knn = KNeighborsClassifier(n_neighbors=8)
    knn.fit(x_train, y_train)

    # lr = LogisticRegression()
    # lr.fit(x_train, y_train)

    y_pred = knn.predict(x_train)

    print(max_error(y_pred, y_train))

    mae = mean_absolute_error(y_train, y_pred)
    print("MAE:", mae)
    print(r2_score(y_train, y_pred))
    print()
    plt.scatter(y_pred, y_train, color='blue')
    plt.xlabel('pred')
    plt.ylabel('actual')
    plt.show()
    # print(tabulate(df.head(20), headers='keys', tablefmt='psql'))

    return HttpResponse(df.to_html())









def index(request):
    return render(request, 'ML/index.html')


def Khodro45(request):
    r = requests.get('https://khodro45.com/used-car/')

    soup = BeautifulSoup(r.text, 'html.parser')

    num = 38
    num1 = 0

    for a in range(len(soup.find_all('div', attrs={'data-item': 'true'}))):
        car = Car()
        a = ''
        b = ''
        for i in range(6):
            val2 = soup.find_all("span")
            val2_1 = val2[num]
            if i == 0:
                a = val2_1.text
            if i == 1:
                b = val2_1.text
            if i == 2:
                car.name1 = f'{str(val2_1.text)}{a}{b}'
            if i == 3:
                val1 = str(val2_1.text)
                car.price = val1
            if i == 4:
                car.date_added = val2_1.text
            if i == 5:
                car.city = val2_1.text

            num += 2

        vall2 = soup.find_all("div", attrs={'class': "DigestSingleData text-center text-black-800 text-nowrap"})
        vall2_1 = vall2[2*num1]
        var = str(vall2_1.text).replace(',', '')
        var = var.replace(' کیلومتر', '')
        var = var.replace(' ک', '')
        var = int(var)

        car.km_worked = var

        va2 = soup.find_all("div", attrs={'class': "DigestSingleData text-center text-black-800 text-warp"})
        va2_1 = va2[num1]

        car.details = va2_1.text

        var = soup.find_all('a', attrs={'class': "btn p-0 w-100 link"})

        link = var[num1].get('href')
        link = f'https://khodro45.com{link}'

        car.link = link
        car.link2 = 'https://khodro45.com'

        var = soup.find_all('div', attrs={
            'class': "picture-holder position-relative d-flex flex-col al-start bg-gray-light-2"})
        var1 = var[num1].get('style')

        img = var1[21:117]

        car.image = img

        if Car.objects.filter(name1=car.name1, name2=car.name2, details=car.details, date_added=car.date_added,
                              model=car.model, price=car.price, city=car.city, image=car.image, link=car.link,
                              km_worked=car.km_worked).exists():
            pass
        else:
            car.save()

        num1 += 1
        num += 1



    return render(request, 'ML/Done.html')


def Yazd2020(request):
    r = requests.get('https://yazd2020.ir/')

    soup = BeautifulSoup(r.text, 'html.parser')
    val = soup.find_all('div', attrs={'class': "car card"})

    num = 5
    num1 = 0

    for i in range(len(val)):
        car=Car()
        for i in range(5):
            val2 = soup.find_all('p')
            val2_1 = val2[num]
            if i == 0:
                car.name1 = val2_1.text
            if i == 1:
                car.details = val2_1.text
            if i == 2:
                val1 = str(val2_1.text)
                val1 = val1.replace('کارکرد: ', '')
                val1 = val1.replace('کیلومتر', '')
                car.km_worked = int(val1)
            if i == 3:
                car.details.__add__(val2_1.text)
            if i == 4:
                val1 = str(val2_1.text).replace('قیمت:', '')
                val1 = val1.replace('تومان', '')
                val1 = val1.replace(',', '')
                car.price = int(val1)

            num += 1

        var = soup.find_all('span', attrs={'class': 'btn btn-adsDate'})
        vall2_1 = var[num1]

        car.date_added = vall2_1.text


        var = soup.find_all('div', attrs={'class': 'pull-left'})
        var1 = str(var[num1+1])  # start from 1
        link = var1[105:154]
        link = f'https://yazd2020.ir/{link}'

        car.link = link
        car.link2 = 'https://yazd2020.ir/'


        val1 = soup.find_all('div', attrs={'class': "text-center card-image"})
        var = val1[num1].find('img')
        var = str(var)

        img = var[71:145]

        car.image = f'https://yazd2020.ir/{img}'

        if Car.objects.filter(name1=car.name1, details=car.details, date_added=car.date_added, price=car.price,
                              image=car.image, link=car.link,
                              km_worked=car.km_worked).exists():
            pass
        else:
            car.save()

        num1 += 1

    return render(request, 'ML/Done.html')


def HamrahMechanic(request):
    r = requests.get('https://www.hamrah-mechanic.com/cars-for-sale/')

    soup = BeautifulSoup(r.text, 'html.parser')
    val = soup.find_all('div', attrs={'class': 'list_list-item__XdvG4 gtm-cfs-16'})

    num = 5
    num1 = 0

    for i in range(len(val)):
        car = Car()

        var1 = soup.find_all('span', attrs={'class': 'carCard_header__subtitle__XJ7UZ'})
        var1 = var1[num1].text  # from 3
        car.details = var1

        var1 = soup.find_all('span', attrs={'class': 'carCard_specification__item-text__2c1Ub'})
        var1 = var1[2*(num1)].text
        car.city = var1

        var1 = soup.find_all('span', attrs={'class': 'carCard_specification__item-text__2c1Ub'})
        var1 = var1[1+(2 * num1)].text
        var1 = str(var1).replace('KM','')
        var1 = var1.replace(',', '')
        if var1 == 'صفر ':
            var1 = 0
        car.km_worked = int(var1)

        var1 = soup.find_all('div', attrs={'class': 'carCard_price-container__cost__BO_Hy'})
        var1 = str(var1[num1].text).replace('تومان', '')
        car.price = int(var1.replace(',', ''))

        var1 = soup.find_all('span', attrs={'class': 'carCard_header__name__ib5RB'})
        var1 = var1[num1].text  # start from 3

        car.name1 = var1

        var1 = soup.find_all('a', attrs={'class': 'carCard_container__naGbB'})
        var1 = str(var1[num1])
        link = var1[42:79]
        link = f'https://www.hamrah-mechanic.com/cars-for-sale/{link}'

        car.link = link
        car.link2 = 'https://www.hamrah-mechanic.com/cars-for-sale/'

        var1 = soup.find_all('div', attrs={'class': 'image_img__xobsF'})
        var1 = str(var1[num1])

        img = var1[429:1131]

        car.image = f'https://www.hamrah-mechanic.com/cars-for-sale/{img}'

        if Car.objects.filter(name1=car.name1, details=car.details, date_added=car.date_added, price=car.price,
                              image=car.image, link=car.link,
                              km_worked=car.km_worked).exists():
            pass
        elif Car.objects.filter(link=car.link).exists():
            pass
        else:
            car.save()

        num1 += 1

    return render(request, 'ML/Done.html')

