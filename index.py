from bottle import *
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'file',
    # 'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

@route('/')
def index():
  s = request.environ.get('beaker.session')
  s['test'] = s.get('test',0) + 1
  s.save()
  return """
    <h2>Hvað viltu kaupa?</h2>
    <a href="set/stoll">stóll</a>
    <a href="set/bord">borð</a>
    <a href="set/heftari">heftari</a>
    <a href="set/sofasett">sófasett</a>
    <h3><a href="skoda">Skoða körfu</a></h3>
"""

@route('/set/<item>')
def set(item):
    s = request.environ.get('beaker.session')
    try:
      s['karfa'].append(item)
    except:
      s['karfa'] = [item]
    return """
    <h2>Hvað viltu kaupa?</h2>
    <a href="stoll">stóll</a>
    <a href="bord">borð</a>
    <a href="heftari">heftari</a>
    <a href="sofasett">sófasett</a>
    <h3><a href="/skoda">Skoða körfu</a></h3>
    <h1 style="color:red">"""+item+""" hefur verið bætt í körfuna þína</h1>
"""


@route('/skoda')
def set():
    s = request.environ.get('beaker.session')
    x = ""
    buid = []
    if s.get('karfa'):
      for i in s['karfa']:
        if s['karfa'].count(i) != 0:
          if i not in buid:
            x = x + str(s['karfa'].count(i)) + " - " + i + "<br>"
        buid.append(i)
      return "<h2>Karfan mín...</h2>"+x+"""<br><h4><a href="/eyda">Hreinsa körfu</a></h4><h3><a href="/">Aftur í vefverslun</a></h3>"""
    else:
        return """<h2>Karfan mín...</h2><h3 style="color:red">Karfan er tóm!</h3><h3><a href="/">Aftur í vefverslun</a></h3>"""

@route('/eyda')
def set():
    s = request.environ.get('beaker.session')
    s.delete()
    return """<h2>Karfan mín...</h2><h3 style="color:red">Karfan er tóm!</h3><h3><a href="/">Aftur í vefverslun</a></h3>"""

run(app=app)
