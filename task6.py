from pprint import pprint

class Wizard():
    
    def __init__(self, name, age, faculty):
        self.name, self.age, self.faculty = name, age, faculty
        self.key = (name, faculty)
    
    def __repr__(self):
        return "Wizard ('%s', '%s', '%s')" % (self.name, self.age, self.faculty)
    
    def __eq__(self, other):
        if type(other) == Wizard:
            return 
        elif type(other) == str:
            return fuzzy_compfrte(other)
        else:
            return

'''
def compare(s1, s2):
    ngrams = [
            s1[i: i+3] for i in range(len(s1))
    ]
    count = 0
    for ngram in ngrams:
        count += s2.count(ngram)
    return count / max(len(s1), len(s2))


FAC_WORDS = {'Griffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff'}
def by_faculty(Q):
    Q = Q - FAC_WORDS
    W = set(self.faculty.split())
    rez[" "]
    for a, b in product (Q, W):
        rez += [(compare(a, b), (a, b))]
    return max(rez)[0]
'''

def lev_distance(a,b):
    len_a = len(a)
    len_b = len(b)
    d2_memo = [[0 for i in range(len_b+1)] for k in range(len_a+1)]
    return l_d(a,b,d2_memo,len_a,len_b)
    

def l_d(a,b,d2_memo,len_a,len_b):
    
    for i in range(1,len_a+1):
        for m in range(1,len_b+1):
            k = 0 if a[i-1] == b[m-1] else 2
            d2_memo[i][m] = min(d2_memo[i-1][m] + 1 ,
                                d2_memo[i][m-1] + 1 ,
                                d2_memo[i-1][m-1] + k
                                )
    return d2_memo[len_a][len_b]

def run():
    mimsey = Wizard('Mimsey', 13, 'Griffindor')
    tamseen = Wizard('Tamseen', 14, 'Slytherin')
    midgeon = Wizard('Midgeon', 15, 'Ravenclaw')
    porpington = Wizard('Porpington', 13, 'Hufflepuff')
    students = {mimsey.key:mimsey, tamseen.key:tamseen, 
            midgeon.key:midgeon, porpington.key:porpington}
    pprint(students)
    
    name = input('Search by name. Please enter your name:')
    for student in students:
        print(student[1])
        if lev_distance(student[0].lower(), name.lower()) <= 2:
            print(students[student])
        else:
            print('There are no student by', name)

if __name__ == '__main__':
    run()
