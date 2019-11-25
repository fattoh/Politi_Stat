"""
Definition of views.
"""
import csv
from collections import deque

from ipware import get_client_ip
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from django.http import HttpResponseRedirect
from app.models import Statments , User_Rates
from django.contrib import messages


posts = ['Do you interested at political news (Generally, or US specially) ?',
             'How long do you take to complete the tasks approximately (as hours)?',
             'How do you evaluate the difficulties of the tasks?',
             'Do you review some statements to help you in rating other ones? And how much approximately?',
             'Any other suggestions/comments ?????'
             ]
def home(request):
    Stats = Statments.objects.all()
    #Load statments to database from CSV
  #  with open('1.csv') as csv_file:
   #     csv_reader = csv.reader(csv_file, delimiter=',')
        
    #    for row in csv_reader:         
     #            book = Statments(id = row[0] ,statment=row[1], Paragraph=row[2])
      #           book.save()
                 

  
    
    d = deque(posts)
    d.extendleft(reversed(Stats))
    
    
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'Stats':Stats,
            
            'posts':posts,
            
            'd':d
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def test(request):
    Stats = Statments.objects.all()
    ip, is_routable = get_client_ip(request)
    s2=''
    for x in Stats:
        tmp='stat'+str(x.id)
        s1 ="S_id ="+str(x.id)+ "||R=" +str( request.POST.get(tmp))+'#'
        s2 = s2 + s1
    indexer = len(Stats)+1
    p2=''
    for counter, y in enumerate(posts):
        i = counter + indexer
        tmp='posts'+str(i)
        rr =request.POST.get(tmp)
        p1 ="Q_id"+str(counter+1) +"||A="+ str(rr )+'#'
        p2 = p2 + p1
    


    book = User_Rates(userRate_id=str(ip), rates=s2,qustions=p2)
    book.save()


   # tmp = 'attachment; filename='+str(ip)+'.csv'
    #response = HttpResponse(content_type='text/csv')
    #response['Content-Disposition'] = tmp
    #writer = csv.writer(response)
    #writer.writerow(['new Annotation'])
    
    #writer.writerow(['StatmentID','user Rate'])
    #for x in Stats:
     
     #tmp='stat'+str(x.id)
     
  #writer.writerow([str(x.id), request.POST.get(tmp)])
    messages.success(request, ('Thank you!'))
    return  HttpResponseRedirect('/')


