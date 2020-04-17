from django.shortcuts import render

from .models import Device, Switch


def device_list(request):

    switches = Switch.objects.all()
    devices = Device.objects.all()

    context = {
        'switches': switches,
        'devices': devices
    }
    return render(request, 'devices/devices.html', context)