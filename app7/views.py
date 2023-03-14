from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':"basha","age":23,'contact':6303949550}
    return render(request,'jinja.html',context=d)
