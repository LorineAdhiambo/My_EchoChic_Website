from django.shortcuts import render, redirect
from django.conf import settings
import os
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'trends/home.html')

def team(request):
    team_members = [
        {
            'name': 'Lorine Adhiambo',
            'position': 'Founder',
            'bio': 'Lorine Adhiambo is the founder of EcoChic, a fashion brand dedicated to sustainability and style. With a passion for eco-friendly practices, Miss Lorine leads the company in offering ethically sourced and fashionable clothing for the modern consumer.',
            'image_url': 'media/C.E.O.jpg',
        },
        {
            'name': 'Victor Jared',
            'position': 'Photographer',
            'bio': 'Victor Jared is a skilled photographer at EcoChic, capturing the essence of sustainable fashion. With a keen eye for detail and a passion for eco-friendly practices, we bring the beauty of ethical fashion to life through stunning visuals.',
            'image_url': 'media/Jphoto.jpg',
        },
        {
            'name': 'Arielle Doreen',
            'position': 'Designer',
            'bio': 'Arielle Doreen is a talented designer at EcoChic, blending sustainability with modern fashion. Arielle creates stylish, ethically sourced clothing that embodies both innovation and environmental responsibility.',
            'image_url': 'media/AD.jpg',
        },
    ]  

    context = {'team_members': team_members}
    return render(request, 'trends/team.html', context)

def wardrobe(request):
    return render(request, 'trends/wardrobe.html')

def milestones(request):
    milestones = [
        {'title': 'Launch of EcoChic Website', 'description': 'The EcoChic website is now live, offering a wide range of sustainable fashion choices. Explore our eco-friendly collections and join us in making fashion more sustainable.', 'date': 'June 1, 2024'},
        {'title': 'Reached 100 Customers', 'description': 'We are excited to celebrate our first major milestone of reaching 100 customers. Thank you for supporting our mission of sustainability in fashion.', 'date': 'July 15, 2024'},
        {'title': 'Summer Collection Launch', 'description': 'We have unveiled our summer collection, featuring the latest trends in sustainable fashion. Discover our new eco-conscious designs and refresh your wardrobe.', 'date': 'August 10, 2024'}
    ]
    context = {'milestones': milestones}
    return render(request, 'trends/milestones.html', context)

def trending(request):
    trending = fetch_trends()
    return render(request, 'trends/trending.html', {'trends': trending})

# Placeholder function for fetch_trends
def fetch_trends():
    return [
        {'title': 'Eco-Friendly Fabrics', 'description': 'Discover the latest in eco-friendly fabrics that are making waves in sustainable fashion.'},
        {'title': 'Upcycled Fashion', 'description': 'Learn about the trend of upcycling old clothes into new, stylish pieces.'},
        {'title': 'Sustainable Brands', 'description': 'Check out these brands that are leading the way in sustainable fashion.'}
    ]


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('trends:home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})