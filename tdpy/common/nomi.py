import random

cognomi = ["Rossi","Russo","Ferrari","Esposito","Bianchi","Romano","Colombo","Ricci","Marino","Greco","Bruno","Gallo","Conti","De Luca","Mancini","Costa","Giordano","Rizzo","Lombardi","Moretti","Barbieri","Fontana","Santoro","Mariani","Rinaldi","Caruso","Ferrara","Galli","Martini","Leone","Longo","Gentile","Martinelli","Vitale","Lombardo","Serra","Copppola","De Santis","D\' Angelo","Marchetti","Parisi","Villa","Conte","Ferraro","Ferri","Fabbri","Bianco","Marini","Grasso","Valentini","Messina","Sala","De Angelis","Gatti","Pellegrini","Palumbo","Sanna","Farina","Rizzi","Monti","Cattaneo","Morelli","Amato","Silvestri","Mazza","Testa","Grassi","Pellegrino","Carbone","Giuliani","Benedetti","Barone","Rossetti","Caputo","Montanari","Guerra","Palmieri","Bernardi","Martino","Fiore","De Rosa","Ferretti","Bellini","Basile","Riva","Donati","Piras","Vitali","Battaglia","Sartori","Neri","Costantini","Milani","Pagano","Ruggiero","Sorrentino","D\'Amico","Orlando","Negri","Mantovani"]

nomi = ["Andrea","Luca","Marco","Francesco","Matteo","Alessandro","Davide","Simone","Federico","Lorenzo","Mattia","Stefano","Giuseppe","Riccardo","Daniele","Michele","Alessio","Antonio","Giovanni","Nicola","Gabriele","Fabio","Alberto","Giacomo","Giulio","Filippo","Gianluca","Paolo","Roberto","Salvatore","Emanuele","Edoardo","Enrico","Vincenzo","Nicolo","Leonardo","Jacopo","Manuel","Mirko","Tommaso","Pietro","Luigi","Giorgio","Angelo","Dario","Valerio","Domenico","Claudio","Alex","Christian"]

def nome():
    n = random.sample(nomi, 1)
    c = random.sample(cognomi, 1)
    return n[0]+" "+c[0]

if __name__ == '__main__':
    print nome()
