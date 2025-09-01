from django.shortcuts import redirect, render
from .models import*

# Create your views here.
def restaurant_view(request):
    if request.method=="POST":
        data=request.POST
        image=request.FILES.get('image')
        description=data.get('description')
        name=data.get('name')

        print(name)
        print(description)
        print(image)
    
        Restaurant.objects.create(
            name=name,
            description=description,
            image=image
        )
        # queryset=Restaurant.objects.all()
        # context={'form':queryset}

        # return render(request,'form.html',context)
    queryset = Restaurant.objects.all()
    
    return render(request, 'form.html', {"queryset":queryset})

def Car_view(request):
    if request.method=="POST":
        data = request.POST
        Car_image = request.FILES.get('Car_image')
        Car_description = data.get('Car_description')
        Car_name = data.get('Car_name')
        
        print(Car_name)
        print(Car_description)
        print(Car_image)

        Car.objects.create(
            Car_image=Car_image,
            Car_description=Car_description,
            Car_name=Car_name,
        )

    queryset=Car.objects.all()
    return render(request,'Car.html',{"queryset":queryset})

def delete_Car_view(request,id):
    queryset = Car.objects.get(id = id)
    queryset.delete()
    return redirect('/Car/')

