# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
novos_membros = ["Sutcliffe","Pete Best"]
for i in range( 2 ):
    membro = input(f'Adicione {novos_membros[i]}:'.format(novos_membros) )
    beatles.append(membro)

print("Step 3:", beatles)

# step 4                     #Sem loop fica simplesmente:
for i in range(2):           #del beatles[-1]
    del beatles[-1]          #del beatles[-1]


print("Step 4:", beatles)

# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))



'''3.4.1.13 LAB: O básico das listas - os Beatles

LAB

Tempo estimado
10-15 minutos

Nível de dificuldade
Fácil

Objetivos
Familiarizar o aluno a:

a criação e modificação de listas simples;
utilizar métodos para modificar listas.
Cenário
Os Beatles foram um dos grupos musicais mais populares dos anos 1960, e a banda mais best-seller da história. Algumas pessoas consideram-nas o ato mais influente da era do rock. De facto, foram incluídos na compilação da revista Time das 100 pessoas mais influentes do século XX.

A banda passou por muitas mudanças de formação, culminando em 1962 com o line-up de John Lennon, Paul McCartney, George Harrison, e Richard Starkey (mais conhecido como Ringo Starr).


Escreva um programa que reflita estas mudanças e lhe permita praticar com o conceito de listas. A sua tarefa é:

passo 1: criar uma lista vazia com o nome beatles;
passo 2: utilizar o método append() para adicionar os seguintes membros da banda à lista: John Lennon, Paul McCartney, e George Harrison;
passo 3: utilizar o loop for e o método append() para solicitar ao utilizador que adicione os seguintes membros da banda à lista: Stu Sutcliffe, e Pete Best;
passo 4: utilizar a instrução del para remover Stu Sutcliffe e Pete Best da lista;
passo 5: utilizar o método insert() para adicionar Ringo Starr ao início da lista.
A propósito, é fã dos Beatles? (Os Beatles são uma das bandas favoritas de Greg. Mas calma...quem é o Greg....?)

console
# step 1
print("Step 1:", beatles)

# step 2
print("Step 2:", beatles)

# step 3
print("Step 3:", beatles)

# step 4
print("Step 4:", beatles)

# step 5
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
'''