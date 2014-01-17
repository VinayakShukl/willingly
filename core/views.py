__author__ = 'Aditya'

from django.shortcuts import render

def home(request):

    if request.method=="POST":
        qd = request.POST
        post = dict(qd.iterlists())
        print 'Name: ', post['name']
        print 'Dependent: ', post['dependent']
        print 'Address: ', post['address']
        print 'Age: ', post['age']
        print '# Properties: ', post['prop_num']

        print post

        for i in range(1, int(post['prop_num'][0])+1):
            print '\tType: ', post[str(i)]
            print '\tBeneficiary: ', post['prop-benef'][i-1]
            print '\tAddress: ', post['prop-addr'][i-1]

    return render(request, "home.html")
