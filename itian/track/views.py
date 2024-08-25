from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import Track
from .forms import TrackForm


def track_list(request):
    tracks = Track.objects.all()  # Query the database for all tracks
    context = {'tracks': tracks}
    return render(request, 'track/trackList.html', context)


def track_create(request):
    if request.method == 'POST':
        form = TrackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new Track instance to the database
            return redirect('track_list')
    else:
        form = TrackForm()

    return render(request, 'track/createTrack.html', {'form': form})


def track_update(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == 'POST':
        form = TrackForm(request.POST, instance=track)
        if form.is_valid():
            form.save()  # Update the existing Track instance
            return redirect('track_list')
    else:
        form = TrackForm(instance=track)

    return render(request, 'track/updateTrack.html', {'form': form, 'track': track})


@require_POST
def track_delete(request, id):
    track = get_object_or_404(Track, id=id)
    track.delete()  # Delete the track from the database
    return JsonResponse({'success': True})


def track_details(request, id):
    track = get_object_or_404(Track, id=id)
    return render(request, 'track/trackDetails.html', {'track': track})
