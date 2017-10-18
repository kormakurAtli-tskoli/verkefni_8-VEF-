#import bottle
from bottle import *
from beaker.middleware import SessionMiddleware

#Session kóði hér fyrir neðan, er alltaf eins, þurfum ekkert að spá í þessu...
session_opts = {
    'session.type': 'file',
    # 'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)
#Eiginlegur Session kóði hér fyrir ofan...

@route('/')
def index():
    return """
    <h2>Hvað viltu kaupa?</h2>
    <a href="set/stoll">stóll</a>
    <a href="set/bord">borð</a>
    <h3><a href="skoda">Skoða körfu</a></h3>
"""

@route('/set/<item>')
def set(item):
    s = request.environ.get('beaker.session')
    try:
      s['karfa'] = s['karfa']+", "+item
    except:
      s['karfa'] = item
    return """
    <h1>"""+item+""" hefur verið bætt í körfuna þína</h1>
    <h2>Hvað viltu kaupa?</h2>
    <a href="stoll">stóll</a>
    <a href="bord">borð</a>
    <h3><a href="/skoda">Skoða körfu</a></h3>
"""


@route('/skoda')
def set():
    s = request.environ.get('beaker.session')
    if s.get('karfa'):
        return 'Skoda session ' , s['karfa']
    else:
        return 'Session ekki til...'

@route('/eyda')
def set():
    s = request.environ.get('beaker.session')
    s.delete()
    return 'Eyðum session'

@route('/multi')
def set():
    s = request.environ.get('beaker.session')
    for i in range(10):
        s[i] = i

    return 'Búum til mörg session í einu' , str(s[9])

run(app=app)#þessi aðeins öðruvísi...
