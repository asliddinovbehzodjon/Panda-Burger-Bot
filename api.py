import requests
from environs import Env
env = Env()
env.read_env()
import json
URL= f"{env.str('BASE_URL')}/en/api"
BASE_URL=f"{env.str('BASE_URL')}"
from location import manzil
def create_user(telegram_id:str,language:str=None,name:str=None):
    try:
        response = requests.post(url=f"{URL}/botuser/",
                                 data={'telegram_id': telegram_id, 'name': name, 'language': language})
        return response.status_code
    except:
        return 400
def get_all_users():
    try:
        response = requests.get(url=f"{URL}/botuser/",
                                 )
        return json.loads(response.text)

    except:
        return []
def get_user(telegram_id):
    try:
        response = requests.post(url=f"{URL}/user/", data={'telegram_id': telegram_id})
        if response.status_code == 204:
            return 'Not Found'
        else:
            return json.loads(response.text)
    except:
        return {}


def change_user_language(telegram_id,language):
    try:
        response = requests.post(url=f"{URL}/lang/", data={'telegram_id': telegram_id, 'language': language})
        if response.status_code == 204:
            return 'Not Found'
        else:
            return json.loads(response.text)
    except:
        pass
def add_channel(channel_id:str,channel_name:str=None,channel_members_count:str=None):
    try:
        response = requests.post(url=f"{URL}/channels/", data={'channel_id': channel_id, 'channel_name': channel_name,'channel_members_count':channel_members_count})
        if response.status_code == 201:
            return 'ok'
        else:
            return 'bad'
    except:
        pass
def get_all_channels():
    try:
        response = requests.get(url=f"{URL}/channels/",
                                 )
        return json.loads(response.text)

    except:
        return []
def get_channel(channel_id):
    try:
        response = requests.post(url=f"{URL}/channel/",
                                 data={'channel_id':channel_id})
        if response.status_code==206:
            return json.loads(response.text)
        else:
            return {}

    except:
        return {}
def delete_channel(channel_id):
    try:
        response = requests.post(url=f"{URL}/delete_channel/",
                                 data={'channel_id':channel_id})
        if response.status_code==200:
            return 'Ok'
        else:
            return "Bad"
    except:
        return "Bad"
# Custom
def get_categories(language):
    try:
        response = requests.get(f"{BASE_URL}/{language}/api/category/")
        data = json.loads(response.text)
        categories = [i['name'] for i in data]
        return categories
    except Exception as e:
        print(e)
        return []
######### Get bot russian and uzbek categories ###############
def get_all_categories():
    try:
        response = requests.get(f"{URL}/category/")
        data = json.loads(response.text)
        category_uz = [i['name_uz'] for i in data]
        category_ru = [i['name_ru'] for i in data]
        return category_ru + category_uz
    except Exception as e:
        print(e)
        return []
############# Get Search Category ###################
def category_info(category,language):
    try:
        response = requests.get(f"{BASE_URL}/{language}/api/category/?search={category}")
        data = json.loads(response.text)
        all_info = {}
        subcategories = []
        products = []
        for i in data:
            if i.get('subcategory',[]) !=[]:
               subcategories+=i.get('subcategory')
            else:
                if i.get('products',None) !=[]:
                    products+=i.get('products')

        all_info['subcategory'] =subcategories
        all_info['products'] = products
        return all_info
    except Exception as e:
        all_info = {}
        all_info['subcategory'] = []
        all_info['products'] = []
        return all_info
############# SubCategory ##########
def subcategory_info(subcategory,language):
    try:
        response = requests.get(f"{BASE_URL}/{language}/api/subcategory/?search={subcategory}")
        data = json.loads(response.text)
        all_data  = {}
        products = []
        for i in data:
            products+=i.get('products',[])
        all_data['products'] = products
        return all_data
    except Exception as e:
        return {'products':[]}
# print(category_info('Пицца',language='ru'))
######### Get Product #####################
def get_product(id,language):
    try:
        response = requests.get(f"{BASE_URL}/{language}/api/product/{id}/")
        data = json.loads(response.text)
        return data
    except Exception as e:
        print(e)
        return {}
def change_phone(telegram_id,phone):
    try:
        response = requests.post(f'{URL}/phone/', data={'telegram_id': telegram_id, 'phone': phone})
        return response.status_code
    except Exception as e:
        print(e)
        pass
############## Change Address ###############
def change_address(telegram_id,latitude,longitude):
    try:
        response = requests.post(f'{URL}/address/',
                                 data={'telegram_id': telegram_id, 'latitude': latitude, 'longitude': longitude})
        return response.text
    except Exception as e:
        print(e)
        pass
############### Shop Info ##################
def shop_info(telegram_id,language):
    try:
        response = requests.post(f'{BASE_URL}/{language}/api/shop/', data={'telegram_id': telegram_id})
        data = json.loads(response.text)
        return data
    except Exception as e:
        print(e)
        pass
############# Set Order ##################
def set_order(telegram_id,product,quantity):
    try:
        response = requests.post(f'{URL}/set_order/',
                                 data={'telegram_id': telegram_id, 'product': product, 'quantity': quantity})
        data = json.loads(response.text)
        return data
    except Exception as e:
        print(e)
        pass
############## Delete Basket ##################
def delete_basket(telegram_id):
    try:
        response = requests.post(f'{URL}/delete_basket/', data={'telegram_id': telegram_id})
        data = json.loads(response.text)
        return data
    except Exception as e:
        print(e)
        pass
########### Delete Item ##################
def delete_item(telegram_id,product):
    try:
        response = requests.post(f'{URL}/delete_item/', data={'telegram_id': telegram_id, "product": product})
        data = json.loads(response.text)
        return data
    except Exception as e:
        print(e)
        pass
def address(telegram_id):
   try:
       response = requests.post(f"{URL}/user/", data={'telegram_id': telegram_id})
       data = json.loads(response.text)
       try:
           return manzil(latitude=data['latitude'], longitude=data['longitude'])
       except:
           return False

   except Exception as e:
       print(e)
       pass
def all_info(telegram_id):
    try:
        response = requests.post(f"{BASE_URL}/en/api/user/", data={'telegram_id': telegram_id})
        data = json.loads(response.text)
        return data
    except:
        return {}

