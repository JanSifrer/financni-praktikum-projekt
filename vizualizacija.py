from bottle import *
from generator_tock import *
from decimal import *
import os
import urllib

#Privzete nastavitve
SERVER_PORT = os.environ.get('BOTTLE_PORT', 8080)
RELOADER = os.environ.get('BOTTLE_RELOADER', True)
ROOT = os.environ.get('BOTTLE_ROOT', '/')

def rtemplate(*largs, **kwargs):
    """
    Izpis predloge s podajanjem spremenljivke ROOT z osnovnim URL-jem.
    """
    return template(ROOT=ROOT, *largs, **kwargs)

# Odkomentiraj, če želiš sporočila o napakah
debug(True)  # za izpise pri razvoju

@get('/')
def index():
    return rtemplate('zacetna.html', data = [])

@post('/podatki')
def podatki_post():
    verjetnost = request.forms.verjetnost
    verjetnost=Decimal(verjetnost)
    cas = request.forms.cas
    cas=int(cas)
    radij = request.forms.radij
    radij=Decimal(radij)
    koraki = request.forms.koraki
    koraki=int(koraki)
    tocke_za_simulacijo = request.forms.tocke_za_simulacijo
    tocke_za_simulacijo = int(tocke_za_simulacijo)
    zacetne = request.forms.zacetne
    zacetne=int(zacetne)
    #tocke = generiraj_n_tock(tocke_za_simulacijo)
    #a,b,ze_poznane_slike = narisi_m_okuzenih_tock(tocke_za_simulacijo, zacetne, tocke, cas, radij)
    ze_poznane_slike = okuzi_sosede(tocke_za_simulacijo, zacetne, verjetnost, cas, 1000, radij, koraki, True)
    return rtemplate('zacetna.html', data=ze_poznane_slike)



# reloader=True nam olajša razvoj (ozveževanje sproti - razvoj)
run(host='localhost', port=SERVER_PORT, reloader=RELOADER)