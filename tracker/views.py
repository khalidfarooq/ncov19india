from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'tracker/home.html')


def charts(request):

    return render(request, 'tracker/charts.html')


def map(request):
    return render(request, 'tracker/map.html')


def wiki(request):
    return render(request, 'tracker/wiki.html')


def about(request):
    return render(request, 'tracker/about.html')
###################################################


def statemh(request):
    return render(request, 'tracker/states/mh.html')


def statetn(request):
    return render(request, 'tracker/states/tn.html')


def statedl(request):
    return render(request, 'tracker/states/dl.html')


def stategj(request):
    return render(request, 'tracker/states/gj.html')


def staterj(request):
    return render(request, 'tracker/states/rj.html')


def statemp(request):
    return render(request, 'tracker/states/mp.html')


def stateup(request):
    return render(request, 'tracker/states/up.html')


def statewb(request):
    return render(request, 'tracker/states/wb.html')


def statebr(request):
    return render(request, 'tracker/states/br.html')


def stateap(request):
    return render(request, 'tracker/states/ap.html')


def stateka(request):
    return render(request, 'tracker/states/ka.html')


#####################################################
def statetg(request):
    return render(request, 'tracker/states/tg.html')


def statejk(request):
    return render(request, 'tracker/states/jk.html')


def statehr(request):
    return render(request, 'tracker/states/hr.html')


def statepb(request):
    return render(request, 'tracker/states/pb.html')


def stateor(request):
    return render(request, 'tracker/states/or.html')


def stateas(request):
    return render(request, 'tracker/states/as.html')


def statekl(request):
    return render(request, 'tracker/states/kl.html')


def stateut(request):
    return render(request, 'tracker/states/ut.html')


def statejh(request):
    return render(request, 'tracker/states/jh.html')


def statect(request):
    return render(request, 'tracker/states/ct.html')


######################################################

def statehp(request):
    return render(request, 'tracker/states/hp.html')


def statetr(request):
    return render(request, 'tracker/states/tr.html')


def statech(request):
    return render(request, 'tracker/states/ch.html')


def statemn(request):
    return render(request, 'tracker/states/mn.html')


def statela(request):
    return render(request, 'tracker/states/la.html')


def statega(request):
    return render(request, 'tracker/states/ga.html')


def statepy(request):
    return render(request, 'tracker/states/py.html')


def statenl(request):
    return render(request, 'tracker/states/nl.html')


def statean(request):
    return render(request, 'tracker/states/an.html')


def stateml(request):
    return render(request, 'tracker/states/ml.html')


def statear(request):
    return render(request, 'tracker/states/ar.html')


def statedn(request):
    return render(request, 'tracker/states/dn.html')


def statemz(request):
    return render(request, 'tracker/states/mz.html')


def statesk(request):
    return render(request, 'tracker/states/sk.html')


def stateld(request):
    return render(request, 'tracker/states/ld.html')
