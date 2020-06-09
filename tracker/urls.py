from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('indepth/', views.charts, name="indepth"),
    path('map/', views.map, name="map"),
    path('wiki/', views.wiki, name="wiki"),
    path('about/', views.about, name="about"),



    path('MH/', views.statemh, name="mh"),
    path('TN/', views.statetn, name="tn"),
    path('DL/', views.statedl, name="dl"),
    path('GJ/', views.stategj, name="gj"),
    path('RJ/', views.staterj, name="rj"),

    path('MP/', views.statemp, name="mp"),
    path('UP/', views.stateup, name="up"),
    path('WB/', views.statewb, name="wb"),
    path('BR/', views.statebr, name="br"),
    path('AP/', views.stateap, name="ap"),
    path('KA/', views.stateka, name="ka"),

    path('TG/', views.statetg, name="tg"),
    path('JK/', views.statejk, name="jk"),
    path('HR/', views.statehr, name="hr"),
    path('PB/', views.statepb, name="pb"),
    path('OR/', views.stateor, name="or"),
    path('AS/', views.stateas, name="as"),
    path('KL/', views.statekl, name="kl"),
    path('UT/', views.stateut, name="ut"),
    path('JH/', views.statejh, name="jh"),
    path('CT/', views.statect, name="ct"),

    path('HP/', views.statehp, name="hp"),
    path('TR/', views.statetr, name="tr"),
    path('CH/', views.statech, name="ch"),
    path('MN/', views.statemn, name="mn"),
    path('LA/', views.statela, name="la"),
    path('GA/', views.statega, name="ga"),
    path('PY/', views.statepy, name="py"),
    path('NL/', views.statenl, name="nl"),
    path('AN/', views.statean, name="an"),
    path('ML/', views.stateml, name="ml"),
    path('AR/', views.statear, name="ar"),
    path('DN/', views.statedn, name="dn"),
    path('MZ/', views.statemz, name="mz"),
    path('SK/', views.statesk, name="sk"),
    path('LD/', views.stateld, name="ld"),

]
