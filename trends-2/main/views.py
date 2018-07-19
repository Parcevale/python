from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse

def main(request):
	print('some text')
	content = { 
		'title': {'name':'ololo'},
		'links_menu': "links_menu",
		'same_products': "same_products"
	}

	return render(request, 'mainapp/index.html', content)
def contacts(request):
	return render(request, 'mainapp/contacts.html')
def catalog(request):
	return render(request, 'mainapp/catalog.html')
def debug(request):
	return JsonResponse({"request": dict(request)})
	# return HttpResponse(f'hello, i\'m your debug window {json.dumps(request)}',content_type="application/json" )
# Create your views here.





# queryset = YourModel.objects.filter(some__filter="some value").values()
# return JsonResponse({"models_to_return": list(queryset)})