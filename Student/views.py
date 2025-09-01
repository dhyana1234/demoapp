from django.shortcuts import redirect, render
from .models import*


# Create your views here.

def Student_view(request):
    if request.method=="POST":
        data=request.POST
        Student_image=request.FILES.get('Student_image')
        Student_name=data.get('Student_name')
        # Student_no=data.get('Student_no')
        English=data.get('English')
        Science=data.get('Science')
        Maths=data.get('Maths')
        Gujarati=data.get('Gujarati')
        Computer=data.get('Computer')
        Sanskrit=data.get('Sanskrit')
        Hindi=data.get('Hindi')
        
        print(Student_image)
        print(Student_name)
        # print(Student_no)
        print(English)
        print(Science)
        print(Maths)
        print(Gujarati)
        print(Computer)
        print(Sanskrit)
        print(Hindi)

        Student.objects.create(
            Student_image=Student_image,
            Student_name=Student_name,
            # Student_no=Student_no,
            English=English,
            Science=Science,
            Maths=Maths,
            Gujarati=Gujarati,
            Computer=Computer,
            Sanskrit=Sanskrit,
            Hindi=Hindi
        )
    queryset=Student.objects.all()
    return render(request,'student.html',{"queryset":queryset})

def delete_Student_view(request,id):
    queryset=Student.objects.get(id = id)
    queryset.delete()
    return redirect('/student/')