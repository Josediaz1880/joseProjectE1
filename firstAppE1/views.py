from urllib import request
from django.shortcuts import render
from importlib.machinery import SourceFileLoader
# Create your views here.

def index (request):
        data = {
        "nombre" : 'José',
        "apellido" : 'Díaz',
        "profesion" : 'Casi ingeniero, ojalá',
        "edad" : '22',
        "ciudad" : 'Talca',
        "perfil" : '/static/img/vikings.svg'
    }
        return render (request, 'index.html',data)


def renderproyecto1(request):
    data = {
        "nombreproyecto" : 'Robby Leonardi',
        "detalle" : 'Robby diseñó el sitio de su portafolio como un videojuego que el visitante realmente puede jugar.',
        "cliente" : 'publico en general',
        "año" : '2020',
        "imagencita" : '/static/img/imgproyecto1.png',
        "enlace" : 'http://www.rleonardi.com'
    }
    return render (request, 'proyectos.html', data) 


def renderproyecto2(request):
    data = {
        "nombreproyecto" : 'Yul Moreau',
        "detalle" : 'segundo detalle',
        "cliente" : 'cliente recibido dos',
        "año" : '2004',
        "imagencita" : '/static/img/imgproyecto2.png',
        "enlace" : 'https://y78.fr'

    }
    return render (request, 'proyectos.html', data) 


def renderproyecto3(request):
    data = {
        "nombreproyecto" : 'Daniel Spatzek',
        "detalle" : 'Detalle del proyecto3',
        "cliente" : 'cliente recibido3',
        "año" : '2001',
        "imagencita" : '/static/img/imgproyecto3.png',
        "enlace" : 'https://www.danielspatzek.com/home/'
    }
    return render (request, 'proyectos.html', data) 
