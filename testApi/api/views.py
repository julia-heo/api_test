from django.shortcuts import get_object_or_404, get_list_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests, json, base64, time

@api_view(['GET'])
def testView(request):
    # url = 'https://api.tosspayments.com/v1/transactions'
    # paymentKey = ""
    # params = {
    #     # 'auth': API_KEY,
    #     'startDate': '2015-09-01T00:00:00',
    #     'endDate': '2023-09-10T00:00:00'
    # }
    params="?startDate=2022-07-28T00:00:00.000&endDate=2022-07-31T23:59:59.999"
    # headers = {
    #     "Authorization" : "Basic dGVzdF9za19EcGV4TWdrVzM2bXdrQW9ueWJKOEdiUjVvek8wOg==",
    #     "Content-Type": "application/json"
    #     }
    # response = requests.get(url+paymentKey,headers=headers, params=params)
    # # response = requests.get(url+params,headers=headers)
    # products_data = response.json()
    
    # return Response(products_data)
  
    url = "https://api.tosspayments.com/v1/transactions/"
    secertkey = "test_sk_D4yKeq5bgrpKRd0JYbLVGX0lzW6Y"
    userpass = secertkey + ':'
    encoded_u = base64.b64encode(userpass.encode()).decode()
    
    headers = {
        "Authorization" : "Basic %s" % encoded_u,
        "Content-Type": "application/json"
    }
    
    res = requests.get(url+params, headers=headers)
    resjson = res.json()
    return Response(resjson)


@api_view(['GET'])
def tockenView(request):

    return render(request,'apitest.html')

# @api_view(['GET'])
# def meView(request):
#     url='https://testapi.openbanking.or.kr/oauth/2.0/token'
#     # client_id = '21cf6ab2-9b7c-47df-a2b7-3dbfad00b279'
#     # client_secret = '5c570523-d7b5-45f7-b34b-5fa0cbc8fc14'
#     # scope = 'oob'
#     # grant_type = 'client_credentials'
#     headers={
#         'Authorization':'BearereyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJNMjAyMzAyMjk5Iiwic2NvcGUiOlsib29iIl0sImlzcyI6Imh0dHBzOi8vd3d3Lm9wZW5iYW5raW5nLm9yLmtyIiwiZXhwIjoxNzAyNzc0Nzg4LCJqdGkiOiJmNWY1OGU0OC04OTcxLTQ5MjktOTZmYi0wNDA3NWQwZGI0MGYifQ.-21LNpA1AvFJQm6PAEp4Hy8_9k9mdss4vZYzPj78-ms'
#     }
#     params="/?bank_tran_id=F123456789U4BC31239Z&user_seq_no=M202302299&bank_code_std=361&member_bank_code=023&from_month=202005&to_month=202105"
    
#     res = requests.get(url+params, headers=headers)
#     resjson = res.json()
#     return Response(resjson)

@api_view(['GET'])
def homeView(request):
    return render(request,'home.html')