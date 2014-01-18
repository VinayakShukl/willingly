__author__ = 'Aditya'

from django.shortcuts import render

def home(request):

    if request.method=="POST":
        qd = request.POST
        post = dict(qd.iterlists())
        will_info = {'name': post['name'], 'age': post['age'], 'dependent': post['dependent']}
        address = {'address': post['address'], 'street_name': post['street_name'], 'city': post['city'],
                   'state': post['state'], 'pin': 0 if post['pin'][0]=='' else int(post['pin'][0])}
        will_info['address'] = address

        properties = {}
        for i in range(1, int(post['prop_num'][0])+1):
            properties[i] = {'type': post[str(i)], 'beneficiary':post['prop-benef'][i-1], 'address': post['prop-addr'][i-1]}

        will_info['properties'] = properties
            # print '\nProperty', i
            # print '\tType: ', post[str(i)]
            # print '\tBeneficiary: ', post['prop-benef'][i-1]
            # print '\tAddress: ', post['prop-addr'][i-1]

        jewels = {}
        for i in range(1, int(post['jewel_num'][0])+1):
            jewels[i] = {'beneficiary': post['jewel-benef'][i-1], 'description':post['jewel-desc'][i-1] }
            # print '\nJewel', i
            # print '\tBeneficiary: ', post['jewel-benef'][i-1]
            # print '\tDesc: ', post['jewel-desc'][i-1]
        will_info['jewels'] = jewels
        print will_info
        print post

    return render(request, "home.html")
