from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ServiceRequestForm, PhoneNumberForm
from .models import JobRequest
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable, GeocoderServiceError

from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import JobRequest  # Import the JobRequest model
from django.urls import reverse

def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            new_request = form.save()  # Save the new request instance

            # Get the existing job requests
            job_requests = JobRequest.objects.all()

            return render(request, 'app/driver_dashboard.html', {'job_requests': job_requests})

    else:
        form = ServiceRequestForm()

    return render(request, 'app/ride_details_form.html', {'form': form})


def home(request):
    return render(request, 'app/layout.html')  # Update to 'app/index.html'

def driver_dashboard(request):
    job_requests = JobRequest.objects.all()

    # Create a geocoder instance
    geolocator = Nominatim(user_agent="your_app_name")

    for request in job_requests:
        pickup_location = geolocator.reverse((request.pickup_location_latitude, request.pickup_location_longitude), exactly_one=True)
        destination = geolocator.reverse((request.destination_latitude, request.destination_longitude), exactly_one=True)
        
        # Update the job request with human-readable addresses
        request.pickup_location = pickup_location.address if pickup_location else "Address not found"
        request.destination = destination.address if destination else "Address not found"

    return render(request, 'app/driver_dashboard.html', {'job_requests': job_requests})


@require_POST
def accept_request(request):
    request_id = request.POST.get('request_id')
    phone_number = request.POST.get('phone_number')
    
    try:
        job_request = JobRequest.objects.get(id=request_id)
        job_request.driver_accepted = True
        job_request.phone_number = phone_number
        job_request.save()
        return JsonResponse({"message": "Job accepted successfully."})
    except JobRequest.DoesNotExist:
        return JsonResponse({"message": "Job request not found."}, status=400)


def decline_request(request, request_id):
    job_request = JobRequest.objects.get(id=request_id)
    job_request.delete()
    return redirect(reverse('driver_dashboard'))


def get_address(request):
    zip_code = request.GET.get('zip')
    
    # Create a geocoder instance
    geolocator = Nominatim(user_agent="your_app_name")
    
    try:
        location = geolocator.geocode(zip_code)
        if location:
            return JsonResponse({"address": location.address})
        else:
            return JsonResponse({"address": "Address not found."})
    except Exception as e:
        return JsonResponse({"address": "Error fetching address."})
