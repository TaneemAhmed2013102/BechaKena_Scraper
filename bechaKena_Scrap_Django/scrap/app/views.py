from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import BookShelf
# from .models import Book
# from .models import ANESTHESIOLOGY
# from .models import CARDIOLOGY
# from .models import CARDIAC_SURGERY
# from .models import DERMATOLOGY
# from .models import ENT
# from .models import ORTHOPEDICS
# from .models import UROLOGY
# from .models import NEUROLOGY
# from .models import Book2
# from .models import Doctor
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import json
import re


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def taneem(request):
    data = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
    }
    return JsonResponse(data)


def books_shelf(request):
    books = BookShelf.objects.all()
    book_data = []

    for i in books:
        book_data.append({
            'id': i.id,
            'title': i.title,
            'price': float(i.price),
            'author': i.author,
            'rokormari_id': i.rokomari_id,
            'image_path': i.image_path,
            'company_logo': i.company_logo  
        })

    return JsonResponse({'books': book_data})


def scrape_rokomari(request):

    url = 'https://www.rokomari.com/book/author/930/rabindranath-tagore?ref=mm_p3&page=3'
    response = requests.get(url)

    if response.status_code == 200:

        soup = fetch_and_parse_with_selenium(url)
        book_list = soup.find_all('div', {'class': 'book-list-wrapper'})
        # print(book_list)
        # return HttpResponse(book_list)
        book_data = []

        for book in book_list:
            title = book.find('h4', {'class': 'book-title'}).text.strip()
            author = book.find('p', {'class': 'book-author'}).text.strip()
            price = book.find('p', {'class': 'book-price'}
                              ).find('span').text.strip()
            image_path = book.find(
                'div', {'class': 'book-img'}).find('img').get('src')
            rokomari_id = book.find(
                'div', {'class': 'cart-btn-area'}).find('button').get('product-id')

            book_data.append({
                'title': title,
                'price': convertStringToInteger(price),
                'author': author,
                'image_path': image_path,
                'rokomari_id': rokomari_id,
                'company_logo': 'https://www.rokomari.com/static/200/images/rokomari_logo.png'
            })
        insert_into_shelf(book_data)
        return JsonResponse({'books': book_data})
    else:
        return HttpResponse(f"Failed to fetch data. Status code: {response.status_code}")


def scrape_boibitan(request):

    url = 'https://boibitan.com/author/gurudev-rabindranath-tagore-0ep4a?page=2'
    response = requests.get(url)

    if response.status_code == 200:

        soup = fetch_and_parse_with_selenium(url)
        book_list = soup.find_all('div', {'class': 'product-default inner-quickview inner-icon pl-3 pr-3'})
        book_data = []

        for book in book_list:
            title = book.find('h3', {'class': 'product-title'}).text.strip()
            author = book.find('div', {'class': 'category-list'}).text.strip()
            price = book.find('span', {'class': 'product-price'}).text.strip()
            image_path = book.find('figure').find('img').get('src')
            boibitan_name = book.find('h3', {'class': 'product-title'}).text.strip()
            

            book_data.append({
                'title': title,
                'price': convertStringToInteger(price),
                'author': author,
                'image_path': image_path,
                'company_logo': "https://boibitan.com/public/uploads/all/63cd26644307b.jpeg",
                'boibitan_name': boibitan_name
            })
        insert_into_shelf(book_data)
        return JsonResponse({'books': book_data})
    else:
        return HttpResponse(f"Failed to fetch data. Status code: {response.status_code}")


def fetch_and_parse_with_selenium(url, browser='chrome'):
    
    if browser.lower() == 'chrome':
        options = ChromeOptions()
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError('Invalid browser specified')

    driver.get(url)
   
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(3)

        # button = driver.find_element_by_xpath(
        #     "//img[@alt='close']")
        # # button = driver.find_element_by_id('js--notification-btn-close')

        # # Click the button
        # button.click()

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    html = driver.page_source
    
    driver.quit()
    
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def insert_into_shelf(books):

    for book in books:
        title = book.get('title')
        price = book.get('price')
        author = book.get('author')
        rokomari_id = book.get('rokomari_id')
        boibitan_name = book.get('boibitan_name')
        image_path = book.get('image_path', '')
        company_logo = book.get('company_logo','')

        if rokomari_id:
            BookShelf.objects.update_or_create(
                rokomari_id=rokomari_id,
                defaults={
                    'title': title,
                    'price': price,
                    'author': author,
                    'image_path': image_path,
                    'company_logo':company_logo
                }
            )
        elif boibitan_name:
            BookShelf.objects.update_or_create(
                boibitan_name=boibitan_name,
                defaults={
                    'title': title,
                    'price': price,
                    'author': author,
                    'image_path': image_path,
                    'company_logo':company_logo
                }
            )

def convertStringToInteger(string):
    return ''.join([char for char in string if char.isdigit()])
            

# FOR MORE PRACTICE AND SCRAPING I HAVE WRITTEN THE LOWER CODES WHICH SCRAP DATAS FROM SOME WEBSITES!

# def books_list(request):
#     books = Book.objects.all()
#     book_data = []

#     for book in books:
#         book_data.append({
#             'id': book.id,
#             'title': book.title,
#             'price': float(book.price),
#             'author': book.author,
#             'rokormari_id': book.rokomari_id,
#             'image_path': book.image_path
#         })

#     return JsonResponse({'books': book_data})

# def doctors_list(request):
#     doctors = CARDIOLOGY.objects.all()
#     doctor_data = []

#     for i in doctors:
#         doctor_data.append({
#             'id': i.id,
#             'name': i.name,
#             'degree': i.degree,
#             'specialist': i.specialist,
#             'image_path': i.image_path
#         })

#     return JsonResponse({'doctors': doctor_data})


# def cardiology(request):
#     doctors = CARDIOLOGY.objects.all()
#     doctor_data = []

#     for i in doctors:
#         doctor_data.append({
#             'id': i.id,
#             'name': i.name,
#             'degree': i.degree,
#             'specialist': i.specialist,
#             'image_path': i.image_path
#         })

#     return JsonResponse({'doctors': doctor_data})


# def anesthesilogy(request):
#     doctors = ANESTHESIOLOGY.objects.all()
#     doctor_data = []

#     for i in doctors:
#         doctor_data.append({
#             'id': i.id,
#             'name': i.name,
#             'degree': i.degree,
#             'specialist': i.specialist,
#             'image_path': i.image_path
#         })

#     return JsonResponse({'doctors': doctor_data})


# def cardiac_Surgery(request):
#     doctors = CARDIAC_SURGERY.objects.all()
#     doctor_data = []

#     for i in doctors:
#         doctor_data.append({
#             'id': i.id,
#             'name': i.name,
#             'degree': i.degree,
#             'specialist': i.specialist,
#             'image_path': i.image_path
#         })

#     return JsonResponse({'doctors': doctor_data})


# def ent(request):
#     doctors = ENT.objects.all()
#     doctor_data = []

#     for i in doctors:
#         doctor_data.append({
#             'id': i.id,
#             'name': i.name,
#             'degree': i.degree,
#             'specialist': i.specialist,
#             'image_path': i.image_path
#         })

#     return JsonResponse({'doctors': doctor_data})

# def doctor(request):
#     dcs = Doctor.objects.all()
#     dcs_data = []

#     for i in dcs:
#         dcs_data.append({
#             'id': i.id,
#             'name': i.name,
#             'degree': i.degree,
#             'specialist': i.specialist,
#             'image_path': i.image_path,
#             'hospital': i.hospital
#         })

#     return JsonResponse({'doctors': dcs_data})

# def dermatology(request):
#     doctors = DERMATOLOGY.objects.all()
#     doctor_data = []

#     for i in doctors:
#         doctor_data.append({
#             'id': i.id,
#             'name': i.name,
#             'degree': i.degree,
#             'specialist': i.specialist,
#             'image_path': i.image_path
#         })

#     return JsonResponse({'doctors': doctor_data})


# def neurology(request):
#     doctors = NEUROLOGY.objects.all()
#     doctor_data = []

#     for i in doctors:
#         doctor_data.append({
#             'id': i.id,
#             'name': i.name,
#             'degree': i.degree,
#             'specialist': i.specialist,
#             'image_path': i.image_path
#         })

#     return JsonResponse({'doctors': doctor_data})


# def orthopedics(request):
#     doctors = ORTHOPEDICS.objects.all()
#     doctor_data = []

#     for i in doctors:
#         doctor_data.append({
#             'id': i.id,
#             'name': i.name,
#             'degree': i.degree,
#             'specialist': i.specialist,
#             'image_path': i.image_path
#         })

#     return JsonResponse({'doctors': doctor_data})


# def urology(request):
#     doctors = UROLOGY.objects.all()
#     doctor_data = []

#     for i in doctors:
#         doctor_data.append({
#             'id': i.id,
#             'name': i.name,
#             'degree': i.degree,
#             'specialist': i.specialist,
#             'image_path': i.image_path
#         })

#     return JsonResponse({'doctors': doctor_data})


# def books_list2(request):
#     books = Book2.objects.all()
#     book_data = []

#     for i in books:
#         book_data.append({
#             'id': i.id,
#             'title': i.title,
#             'price': float(i.price),
#             'author': i.author,
#             'image_path': i.image_path
#         })

#     return JsonResponse({'books': book_data})


# def insert_books_from_json(books):

#     for book in books:
#         title = book.get('title')
#         price = book.get('price')
#         author = book.get('author')
#         rokomari_id = book.get('rokomari_id')
#         image_path = book.get('image_path', '')

#         # # Create a new Book instance and save it to the database
#         # new_book = Book(
#         #     id=id,
#         #     title=title,
#         #     price=price,
#         #     author=author,
#         #     rokomari_id=rokomari_id,
#         #     image_path=image_path
#         # )
#         # new_book.save()

#         # Update or create a new Book instance and save it to the database
#         Book.objects.update_or_create(
#             rokomari_id=rokomari_id,
#             defaults={
#                 'title': title,
#                 'price': price,
#                 'author': author,
#                 'image_path': image_path
#             }
#         )

# def insert_books_from_json2(books):

#     for book in books:
#         # Extract book data from JSON
#         title = book.get('title')
#         price = book.get('price')
#         author = book.get('author')
#         # Assuming a default value is provided for the image_path field
#         image_path = book.get('image_path', '')

#         # # Create a new Book instance and save it to the database
#         # new_book = Book(
#         #     id=id,
#         #     title=title,
#         #     price=price,
#         #     author=author,
#         #     rokomari_id=rokomari_id,
#         #     image_path=image_path
#         # )
#         # new_book.save()

#         # Update or create a new Book instance and save it to the database
#         Book2.objects.update_or_create(
#             title=title,
#             defaults={
#                 'price': price,
#                 'author': author,
#                 'image_path': image_path
#             }
#         )

# def insert_doctors_from_json(doctors):

#     for i in doctors:
#         # Extract book data from JSON
#         name = i.get('name')
#         degree = i.get('degree')
#         specialist = i.get('specialist')
      
#         image_path = i.get('image_path', '')
#         hospital = i.get('hospital', '')
        
#         Doctor.objects.update_or_create(
#             name=name,
#             defaults={
#                 'name': name,
#                 'degree': degree,
#                 'specialist': specialist,
#                 'image_path': image_path,
#                 'hospital': hospital
#             }
#         )

# def insert_doctors(doctors):

#     for i in doctors:
#         # Extract book data from JSON
#         name = i.get('name')
#         degree = i.get('degree')
#         specialist = i.get('specialist')
      
#         image_path = i.get('image_path', '')
        
#         CARDIOLOGY.objects.update_or_create(
#             name=name,
#             defaults={
#                 'name': name,
#                 'degree': degree,
#                 'specialist': specialist,
#                 'image_path': image_path,
#             }
#         )

# def scrape_doctors(request):

#     url = 'https://www.uhlbd.com/consultant/departments/cardiology'
#     response = requests.get(url)

#     if response.status_code == 200:

#         soup = fetch_and_parse_with_selenium(url)
#         doctors_list = soup.find_all('div', {'class': 'promo-box-bg'})
#         # print(book_list)
#         # return HttpResponse(book_list)
#         doctor_data = []

#         for i in doctors_list:
#             name = i.find('h4', {'class': 'inner-post-title'}).text.strip()
#             degree = i.find(
#                 'p', {'class': 'inner-post-sub-title'}).text.strip()
#             specialist = i.find(
#                 'h4', {'class': 'inner-post-cont-title'}).text.strip()
#             image_path = i.find(
#                 'div', {'class': 'promo-box-left'}).find('img').get('src')
#             # rokomari_id = book.find(
#             #     'div', {'class': 'cart-btn-area'}).find('button').get('product-id')

#             doctor_data.append({
#                 'name': name,
#                 'degree': degree,
#                 'specialist': specialist,
#                 'image_path': 'https://www.uhlbd.com/' + image_path,

#             })
#         insert_doctors(doctor_data)
#         return JsonResponse({'doctors': doctor_data})
#     else:
#         return HttpResponse(f"Failed to fetch data. Status code: {response.status_code}")


# def scrape_doctorsSquare(request):

#     url = 'https://www.squarehospital.com/doctors/department/UROLOGY'
#     response = requests.get(url)

#     if response.status_code == 200:

#         soup = fetch_and_parse_with_selenium(url)
#         doctors_list = soup.find_all('div', {'class': 'docItem'})
#         # print(book_list)
#         # return HttpResponse(book_list)
#         doctor_data = []

#         for i in doctors_list:
#             name = i.find('div', {'class': 'contentBox'}).find('h3').text.strip()
#             specialist = i.find(
#                 'p').text.strip()
#             image_path = i.find(
#                 'div', {'class': 'imgDiv'}).find('img').get('src')
            
#             doctor_data.append({
#                 'name': name,
#                 'degree': '',
#                 'specialist': specialist,
#                 'image_path': image_path,
#                 'hospital': "SQUARE HOSPITAL"

#             })
#         insert_doctors_from_json(doctor_data)
#         return JsonResponse({'doctors': doctor_data})
#     else:
#         return HttpResponse(f"Failed to fetch data. Status code: {response.status_code}")
