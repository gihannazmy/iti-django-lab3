from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import Trainee
from .forms import TraineeForm


def trainee_list(request):
    trainees = Trainee.objects.all()  # Query the database for all trainees
    context = {'trainees': trainees}
    return render(request, 'trainee/traineeList.html', context)


def trainee_create(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new Trainee instance to the database
            return redirect('trainee_list')
    else:
        form = TraineeForm()

    return render(request, 'trainee/createTrainee.html', {'form': form})


def trainee_update(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()  # Update the existing Trainee instance
            return redirect('trainee_list')
    else:
        form = TraineeForm(instance=trainee)

    return render(request, 'trainee/updateTrainee.html', {'form': form, 'trainee': trainee})


@require_POST
def trainee_delete(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()  # Delete the trainee from the database
    return JsonResponse({'success': True})


def trainee_details(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    return render(request, 'trainee/traineeDetails.html', {'trainee': trainee})
