# Importando as classes

from Professor import Professor
from Aluno import Aluno
from Aula import Aula

# Instanciando os objetos

professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos")

# Chamando os métodos

aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())