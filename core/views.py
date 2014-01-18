__author__ = 'Aditya'

import os, lawyered, StringIO
from django.shortcuts import render
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper


def home(request):
    if request.method == "POST":
        qd = request.POST
        post = dict(qd.iterlists())
        will_info = {'name': post['name'][0], 'age': post['age'][0], 'dependent': post['dependent'][0]}
        address = {'address': post['address'], 'street_name': post['street_name'], 'city': post['city'],
                   'state': post['state'], 'pin': 0 if post['pin'][0] == '' else int(post['pin'][0])}
        will_info['address'] = address['address'][0] + ", " + address['street_name'][0] + ", " + \
                                address['city'][0] + ", " + address['state'][0] + ", " + str(address['pin'])

        properties = {}
        for i in range(1, int(post['prop_num'][0]) + 1):
            properties[i] = {'type': post[str(i)], 'beneficiary': post['prop-benef'][i - 1],
                             'address': post['prop-addr'][i - 1]}
        will_info['properties'] = properties

        jewels = {}
        for i in range(1, int(post['jewel_num'][0]) + 1):
            file_path = None
            if request.FILES['pic']:
                file_path = 'core/media/' + 'jewel_' + str(i) + '.jpeg'
                store_file(request.FILES['pic'], file_path)
            jewels[i] = {'beneficiary': post['jewel-benef'][i - 1], 'description': post['jewel-desc'][i - 1],
                         'file_path': file_path}
        will_info['jewels'] = jewels
        print will_info
        response = HttpResponse(mimetype='application/pdf', content_type='application/pdf')
        response.write(lawyered.fillin(will_info))
        return response
    return render(request, "home.html")


def store_file(file_obj, path):
    print path
    with open(path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

