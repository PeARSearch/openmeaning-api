import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'openmeaning.settings'

from openmeaning.api.models import Vector

def populate_openmeaning_db():
  with open(os.path.join(os.path.dirname(__file__), "openvectors.dm")) as f:
    dmlines = f.readlines()
    f.close()
    for l in dmlines:
      items = l.rstrip('\n').split('\t')
      w = unicode(items[0], "utf-8")
      v = ",".join(items[1:])
      Vector.objects.create(word=w, vector=v)

populate_openmeaning_db()
