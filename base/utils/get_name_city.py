import requests
import time
#
# def get_public_ip()-> str:
#     """
#     Get my public IP address.
#     :return: ip address
#     """
#     response = requests.get("https://api.ipify.org?format=json")
#
#     if response.status_code == 200:
#         data = response.json()
#         return data.get("ip")
#     else:
#         return None
#
#
# def get_location_by_ip(ip_address: str) -> dict:
#     """
#     Get location information by IP address.
#     :param ip_address: ip address
#     :return: dictionary with location information
#     """
#     url = f"https://ipapi.co/{ip_address}/json/?language=ru"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#         return {
#             "Город": data.get("city"),
#             "Регион": data.get("region"),
#             "Страна": data.get("country_name"),
#         }
#     elif response.status_code == 429:
#         # Пауза перед повторным запросом
#         time.sleep(5)  # Подождать 5 секунд
#         # Повторный запрос
#         return get_location_by_ip(ip_address)
#     else:
#         return None
#
#
# # Получение текущего публичного IP-адреса
# my_ip = get_public_ip()
# if my_ip:
#     print("My Public IP Address:", my_ip)
#
#     # Получение информации о местоположении по IP-адресу
#     location_info = get_location_by_ip(my_ip)
#     if location_info:
#         print("Information about My IP Address:")
#         for key, value in location_info.items():
#             print(f"{key}: {value}")
#     else:
#         print("Failed to retrieve location information for my IP.")
# else:
#     print("Failed to retrieve my public IP address.")

class IpLocationInfo:
    def __init__(self):
        # self.ip_address = ip_address
        self.location_info = self._get_location_by_ip()

    def _get_public_ip(self):
        response = requests.get("https://api.ipify.org?format=json")
        if response.status_code == 200:
            data = response.json()
            return data.get("ip")
        else:
            return None

    def _get_location_by_ip(self):
        self.ip_address = self._get_public_ip()
        url = f"https://ipapi.co/{self.ip_address}/json/?language=ru"
        print(url)
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return {
                "Город": data.get("city"),
                "Регион": data.get("region"),
                "Страна": data.get("country_name"),
            }
        elif response.status_code == 429:
            time.sleep(5)
            return self._get_location_by_ip()
        else:
            return None


# Пример использования:
ip_location = IpLocationInfo()
# print("Публичный IP-адрес:", ip_location.ip_address)

if ip_location.location_info:
    print("Информация о местоположении по IP:")
    for key, value in ip_location.location_info.items():
        print(f"{key}: {value}")
else:
    print("Не удалось получить информацию о местоположении.")