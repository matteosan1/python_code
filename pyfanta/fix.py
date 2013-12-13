import Squadra
import pickle

s = pickle.load(open("/home/sani/Documents/Fantamaniaco/black_hole_thoiry.fnm"))

print len(s.formazioni)
s.formazioni = s.formazioni + [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]*35

pickle.dump(s, open("/home/sani/Documents/Fantamaniaco/pippo.fnm", 'w'))

