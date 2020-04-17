from django.shortcuts import render

from .models import Device, Switch


def device_list(request):

    switches = Switch.objects.all().order_by('name')
    devices = Device.objects.all().order_by('name')

    context = {
        'switches': switches,
        'devices': devices
    }
    return render(request, 'devices/devices.html', context)