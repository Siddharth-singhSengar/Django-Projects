from django.shortcuts import render
import requests
import json

# Create your views here.
#GFlnXGhTX2UAbNkeNd5N2w==8gPswInH5lv9P2sx
def home(request):

    if request.method=='POST':
        query=request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query,headers={'X-Api-Key': 'GFlnXGhTX2UAbNkeNd5N2w==8gPswInH5lv9P2sx'})
        try:
            api=json.loads(api_request.content)
            print(api_request.content)
       
        except Exception as e :
            api = "oops! There was an error"
            print(e)
        return render(request,'home.html',{'api':api})

    else:
        return render(request, 'home.html',{'query':'Enter a valid query'})

    

    return render(request, 'home.html')