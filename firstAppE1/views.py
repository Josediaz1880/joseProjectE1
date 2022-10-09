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
        "enlace" : 'http://www.rleonardi.com',
        "desarrolladores" : '100',
        "norma" : 'norma ISO/IEC 33000',
        "calificacion" : '10 de 10',
        "siguiente" : '/proyectos2'

    }
    return render (request, 'proyectos.html', data) 


def renderproyecto2(request):
    data = {
        "nombreproyecto" : 'Yul Moreau',
        "detalle" : 'Se inspira en los años 80 y dedica su portafolio a esta época. Con un diseño de página única con videos incrustados.',
        "cliente" : 'cliente privado',
        "año" : '2012',
        "imagencita" : '/static/img/imgproyecto2.png',
        "enlace" : 'https://y78.fr',
        "desarrolladores" : '75',
        "norma" : 'norma ISO 9001',
        "calificacion" : '8 de 10',
        "siguiente" : '/proyectos3'
 
    }
    return render (request, 'proyectos.html', data) 


def renderproyecto3(request):
    data = {
        "nombreproyecto" : 'Daniel Spatzek',
        "detalle" : 'utiliza un montón de trucos y animaciones de CSS que le dan vida al portafolio y crean una experiencia verdaderamente dinámica.',
        "cliente" : 'empresa de desarrollo',
        "año" : '2016',
        "imagencita" : '/static/img/imgproyecto3.png',
        "enlace" : 'https://www.danielspatzek.com/home/',
        "desarrolladores" : '50',
        "norma" : 'norma ISO/IEC 14598',
        "calificacion" : '7 de 10',
        "siguiente" : '/proyectos'
    }
    return render (request, 'proyectos.html', data) 
