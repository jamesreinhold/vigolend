from django.shortcuts import render

from .models import TeamMember


def index(request):
    """
    View function for rendering homepage
    """
    return render(
        request, 'pages/home.html'
    )


def borrow(request):
    """
    View function for rendering Borrower page
    """
    return render(
        request, 'pages/borrow.html'
    )


def invest(request):
    """
    View function for rendering Invest page
    """
    return render(
        request, 'pages/invest.html'
    )


def about_us(request):
    """
    View function for rendering about us page
    """
    team_members = TeamMember.objects.all()

    context = {'team_members': team_members}

    return render(
        request, 'pages/about.html', context
    )


def teams(request):
    """
    View function for rendering our teams page
    """
    return render(
        request, 'pages/home.html'
    )
