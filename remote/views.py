from django.shortcuts import render

# Create your views here.
def upload(request):
    if request.method == 'POST':
        if 'scan_asin' in request.POST:
            pass
        elif 'upload_asin' in request.POST:
            pass
        elif 'download_asin' in request.POST:
            pass
    return render(request,'uploadxlsx.html')
