from django.shortcuts import render

# Create your views here.
from mainapps.models import Computer, Reservation, Student


def index(request):
    if request.method == 'POST':
        if (request.POST.get('student_id') == request.POST.get('Password')):
            if (request.POST.get('student_name') == None):
                data = Reservation.objects.get(computer_id=int(request.POST.get('id_com')))
                data.computer.status = True
                data.computer.save()
                data.delete()
            else:
                chk = False
                for i in Student.objects.all():
                    if (i.id == int(request.POST.get('student_id'))):
                        chk = True
                if (chk == False):
                    Student.objects.create(
                        id=int(request.POST.get('student_id')),
                        name=request.POST.get('student_name'),
                        surname=request.POST.get('student_surname'),
                        year=int(request.POST.get('student_year')),
                    )
                obj = Reservation.objects.create(
                    student_id=int(request.POST.get('student_id')),
                    computer_id=int(request.POST.get('id_com')),
                    start_date=request.POST.get('start_time'),
                    end_date=request.POST.get('End_time'),
                    date=str(request.POST.get('date_time'))
                )
                for l in Computer.objects.all():
                    if (l.id == obj.computer.id):
                        obj.computer.status = False
                    obj.computer.save()
    context = {
        'computer': Computer.objects.all(),
        'loop': [1, 2, 3, 4, 5, 6, 7, 8],
        'reservation': Reservation.objects.all()
    }
    return render(request, 'index.html', context)
