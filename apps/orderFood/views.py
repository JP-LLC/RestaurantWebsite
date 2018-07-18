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
        ]
    }
    return render(request, 'orderFood/index.html', context)