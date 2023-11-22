
from django.db.models import  Count, Avg
from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models import Q
import datetime


# Create your views here.
from Remote_User.models import review_Model,ClientRegister_Model,flight_delay_prediction_model,recommend_Model,search_ratio_model,flight_delay_model


def serviceproviderlogin(request):
    if request.method  == "POST":
        admin = request.POST.get('username')
        password = request.POST.get('password')
        if admin == "SProvider" and password =="SProvider":
            flight_delay_prediction_model.objects.all().delete()
            flight_delay_model.objects.all().delete()
            return redirect('View_Remote_Users')

    return render(request,'SProvider/serviceproviderlogin.html')


def viewtreandingquestions(request,chart_type):
    dd = {}
    pos,neu,neg =0,0,0
    poss=None
    topic = flight_delay_prediction_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics=t['ratings']
        pos_count=flight_delay_prediction_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss=pos_count
        for pp in pos_count:
            senti= pp['names']
            if senti == 'positive':
                pos= pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics]=[pos,neg,neu]
    return render(request,'SProvider/viewtreandingquestions.html',{'object':topic,'dd':dd,'chart_type':chart_type})

def Search_Flight_Delay(request): # Search

   if request.method == "POST":
        kword = request.POST.get('keyword')
        print(kword)

        obj = flight_delay_prediction_model.objects.all().filter(names__contains=kword)

        obj1 = flight_delay_prediction_model.objects.get(names__contains=kword)

        delay=obj1.Historical_Flight_Delay
        edelay=obj1.Expected_Delay

        tdelay=delay-edelay



        return render(request, 'SProvider/Search_Flight_Delay.html', {'objs': obj,'tdelay': tdelay})
   return render(request, 'SProvider/Search_Flight_Delay.html')

def View_All_FlightDelay_Prediction_Details(request):

    obj1 = flight_delay_prediction_model.objects.values(
        'Departure_Country',
        'Departure_Airport',
        'Flight_Name',
        'names',
        'Date',
        'Departure_Scheduled_Time',
        'Pre_Flight',
        'Expected_Delay',
        'Historical_Flight_Delay',
        'Arrival_Country',
        'Arrival_Airport',
        'Airport_Delay_Reason',
        'Air_Route_Delay_Reason',
        'Other_Reason')

    flight_delay_model.objects.all().delete()
    for t in obj1:

        Departure_Country=t['Departure_Country']
        Departure_Airport=t['Departure_Airport']
        Flight_Name=t['Flight_Name']
        Flight_Number=t['names']
        Date=t['Date']
        Departure_Scheduled_Time=t['Departure_Scheduled_Time']
        Pre_Flight=t['Pre_Flight']
        Expected_Delay=t['Expected_Delay']
        Historical_Flight_Delay=t['Historical_Flight_Delay']
        Arrival_Country=t['Arrival_Country']
        Arrival_Airport=t['Arrival_Airport']
        Airport_Delay_Reason=t['Airport_Delay_Reason']
        Air_Route_Delay_Reason=t['Air_Route_Delay_Reason']
        Other_Reason=t['Other_Reason']

        total_delay =Historical_Flight_Delay-Expected_Delay


        flight_delay_model.objects.create(Departure_Country=Departure_Country,Departure_Airport=Departure_Airport,names=Flight_Number,Flight_Name=Flight_Name,Date=Date,Departure_Scheduled_Time=Departure_Scheduled_Time,Pre_Flight=Pre_Flight,Expected_Delay=Expected_Delay,Historical_Flight_Delay=Historical_Flight_Delay,Total_Flight_Delay=total_delay,Arrival_Country=Arrival_Country,Arrival_Airport=Arrival_Airport,Airport_Delay_Reason=Airport_Delay_Reason,Air_Route_Delay_Reason=Air_Route_Delay_Reason,Other_Reason=Other_Reason)

    obj = flight_delay_model.objects.all().filter(Total_Flight_Delay__gt=10)
    return render(request, 'SProvider/View_All_FlightDelay_Prediction_Details.html', {'objs': obj})

def View_Remote_Users(request):
    obj=ClientRegister_Model.objects.all()
    return render(request,'SProvider/View_Remote_Users.html',{'objects':obj})

def ViewTrendings(request):
    topic = flight_delay_prediction_model.objects.values('topics').annotate(dcount=Count('topics')).order_by('-dcount')
    return  render(request,'SProvider/ViewTrendings.html',{'objects':topic})

def negativechart(request,chart_type):
    dd = {}
    pos, neu, neg = 0, 0, 0
    poss = None
    topic = flight_delay_prediction_model.objects.values('ratings').annotate(dcount=Count('ratings')).order_by('-dcount')
    for t in topic:
        topics = t['ratings']
        pos_count = flight_delay_prediction_model.objects.filter(topics=topics).values('names').annotate(topiccount=Count('ratings'))
        poss = pos_count
        for pp in pos_count:
            senti = pp['names']
            if senti == 'positive':
                pos = pp['topiccount']
            elif senti == 'negative':
                neg = pp['topiccount']
            elif senti == 'nutral':
                neu = pp['topiccount']
        dd[topics] = [pos, neg, neu]
    return render(request,'SProvider/negativechart.html',{'object':topic,'dd':dd,'chart_type':chart_type})


def charts(request,chart_type):
    chart1 = flight_delay_prediction_model.objects.values('names').annotate(dcount=Avg('Historical_Flight_Delay'))
    return render(request,"SProvider/charts.html", {'form':chart1, 'chart_type':chart_type})

def charts1(request,chart_type):
    chart1 = flight_delay_model.objects.values('names').annotate(dcount=Avg('Total_Flight_Delay'))
    return render(request,"SProvider/charts1.html", {'form':chart1, 'chart_type':chart_type})

def View_Flight_Delay_Details(request):
    obj =flight_delay_prediction_model.objects.all()
    return render(request, 'SProvider/View_Flight_Delay_Details.html', {'list_objects': obj})

def likeschart(request,like_chart):
    charts =flight_delay_prediction_model.objects.values('names').annotate(dcount=Avg('Historical_Flight_Delay'))
    return render(request,"SProvider/likeschart.html", {'form':charts, 'like_chart':like_chart})

def View_Flights_NoDelay(request):
    obj = flight_delay_model.objects.all().filter(Q(Total_Flight_Delay__gt=0),Q(Total_Flight_Delay__lt=12))
    return render(request, 'SProvider/View_Flights_NoDelay.html', {'objs': obj})







