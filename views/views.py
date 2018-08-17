# from django.shortcuts       import render, redirect, get_object_or_404
# from activities.models      import Event_Type, Venue, Host
# from news.models            import News



# def get_home_page(request):
    
#     # last_news    = News.objects.order_by('-published_date')[:3]
#     # activities   = get_object_or_404(Event_Type, event_type="ACTIVITY")
#     # courses      = get_object_or_404(Event_Type, event_type="TRAININGCOURSE")
#     # events       = get_object_or_404(Event_Type, event_type="EVENT")
    
#     # return render(request, "views/index.html", {'last_news': last_news, 'activities': activities, 'courses': courses, 'events': events})
#     return render(request, "views/deployment.html")



# def get_about_page(request):
#     return render(request, "views/about.html")
   
   
    
# def get_venue(request, name_venue):
    
#     venue        = get_object_or_404(Venue, name=name_venue)
    
#     return render(request, "views/venue.html", {'venue':venue} )



# def get_host(request, id):
    
#     host        = get_object_or_404(Host, pk=id)
    
#     return render(request, "views/host.html", {'host':host} )


# # def get_admin_panel(request):
# #     return redirect("/admin")
    
    
    