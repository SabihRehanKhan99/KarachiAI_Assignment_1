import requests,json

api_key = "48a3fcb3d2bd4c26a8678c1050aec471"

headers={
 'Authorization': 'token '+api_key
}

url = 'https://api.weatherbit.io/v2.0/current'
query_params = {'lat': 35.7796,"lon":-78.6382, "key": api_key, "include":"minutely"}
# lat=35.7796&lon=-78.6382&key=API_KEY&include=minutely
response = requests.get(
    url,
    params=query_params,
)
print(response.status_code)
response.url
response.json()