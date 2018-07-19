# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {
        'hero_images': [
            'https://cdn.stocksnap.io/img-thumbs/960w/T65Y75HO94.jpg',
            'https://cdn.stocksnap.io/img-thumbs/960w/KJGLHB2KF4.jpg',
            'https://cdn.stocksnap.io/img-thumbs/960w/GL0X7W9QLC.jpg'
        ],
        'homepage_about': [
            'Lorem ipsum dolor sit amet, nusquam repudiare honestatis est an, atqui voluptaria ex sed. Mei dicit laoreet maiestatis id. Quaeque incorrupte no sit, et veniam timeam nam. Mea ne nominavi evertitur dissentiet. Id vis nullam delenit, ei eos sint scaevola mediocrem. Omittam euripidis ullamcorper pri id, movet aliquid perpetua ea eos. Vitae feugait ad nec.',
            'Ut mea vidit habeo. Ea duo prima epicuri, error quaeque duo et. Ferri verear cu vis, est id aliquid consulatu, admodum necessitatibus sit ex. Apeirian contentiones eu usu. Dicunt regione verterem ei eam, inani oblique molestie pri et. Vis no gloriatur efficiantur, nam no tollit laoreet imperdiet.'
        ]
    }
    return render(request, 'orderFood/index.html', context)

def admin(request):
    context = {
        'homepage_paragraph': request.GET.get('homepage_paragraph', '')
    }
    return render(request, 'orderFood/admin.html', context)