# Crear estas clases
# Define los atributos, métodos, constructores... que consideres necesarios.
from datetime import datetime


# cursos:id,nombre, creditos, añosdeestudio
# alumno:id, nombre, email
# matricula:idmatricula, fechamatricula, idalumno, idcurso

# Necesitamos:
#   mostrar la ficha del curso
#   mostrar la ficha de alumno
#   alumno1 se matricula en un curso
#   alumno2 se matricula en dos cursos
#   mostrar los datos de matrículo
# reto*:método que muestra las mátriculas realizadas en mi centro
class Curso:
    def __init__(self, nombre_curso, creditos, anos_de_estudio):
        self.nombre_curso = nombre_curso
        self.creditos = creditos
        self.anos_de_estudio = anos_de_estudio

    def consultarCurso(self):
        print(f'Los datos del curso son:\n'
              f'Nombre: {self.nombre_curso}\n'
              f'Créditos: {self.creditos}\n'
              f'Años de estudio: {self.anos_de_estudio}\n')


class Alumno:
    def __init__(self, id_alumno, nombre_alumno, email):
        self.id_alumno = id_alumno
        self.nombre_alumno = nombre_alumno
        self.email = email

    def consultarAlumno(self):
        print(f'Los datos del alumno son:\n'
              f'ID Alumno: {self.id_alumno}\n'
              f'Nombre: {self.nombre_alumno}\n'
              f'Email: {self.email}\n')


class Matricula(Curso, Alumno):
    def __init__(self, id_matricula, fecha_matricula, nombre_curso, creditos,
                 anos_de_estudio, id_alumno, nombre_alumno, email):
        self.id_matricula = id_matricula
        self.fecha_matricula = fecha_matricula
        super().__init__(nombre_curso, creditos, anos_de_estudio)
        super(Curso, self).__init__(id_alumno, nombre_alumno, email)

    def consultarCurso(self):
        print(f'Los datos del curso son:\n'
              f'Nombre: {self.nombre_curso}\n'
              f'Créditos: {self.creditos}\n'
              f'Años de estudio: {self.anos_de_estudio}\n')

    def consultarAlumno(self):
        print(f'Los datos del alumno son:\n'
              f'ID Alumno: {self.id_alumno}\n'
              f'Nombre: {self.nombre_alumno}\n'
              f'Email: {self.email}\n')

    def consultarMatricula(self):
        print(f'Los datos de matriculación son:\n'
              f'ID Matrícula: {self.id_matricula}\n'
              f'Fecha matrícula: {self.fecha_matricula}\n')


# datos del alumno 1
# introducimos los datos del alumno1
alumno1 = Alumno(1, 'Alex', 'alex.ingeniero@yahoo.es')

# información de los cursos
curso1 = Curso('Ingenieria de sofware', 400, '4 años')

# matriculación

matricula1 = Matricula(1, datetime.now(), curso1.nombre_curso, curso1.creditos, curso1.anos_de_estudio,
                       alumno1.id_alumno, alumno1.nombre_alumno, alumno1.email)

# datos del alumno 2
# introducimos los datos del alumno2
alumno2 = Alumno(2, 'Nerea', 'nerea.sin.gluten@yahoo.es')

# información de los cursos
curso2 = Curso('Derecho', 200, '2años')
curso3 = Curso('ADE', 200, '2 años')

# matriculación

matricula2 = Matricula(2, datetime.now(), curso2.nombre_curso, curso2.creditos, curso2.anos_de_estudio,
                       alumno2.id_alumno, alumno2.nombre_alumno, alumno2.email)
matricula3 = Matricula(3, '22-09-2022', curso3.nombre_curso, curso3.creditos, curso3.anos_de_estudio, alumno2.id_alumno,
                       alumno2.nombre_alumno, alumno2.email)

# mostramos las fichas de los dos alumnos
alumnos = [alumno1, alumno2]
for alumno in alumnos:
    print(f'Los datos del alumno son:\n'
          f'ID Alumno: {alumno.id_alumno}\n'
          f'Nombre: {alumno.nombre_alumno}\n'
          f'Email: {alumno.email}\n')

# mostramos las fichas de los cursos
curso = [curso1, curso2, curso3]
for cursos in curso:
    print(f'Los datos del curso son:\n'
          f'Nombre: {cursos.nombre_curso}\n'
          f'Créditos: {cursos.creditos}\n'
          f'Años de estudio: {cursos.anos_de_estudio}\n')

# mostrar datos matriculación
matriculas = [matricula1, matricula2, matricula3]
for matricula in matriculas:
    print(f'Los datos de matriculación son:\n'
          f'ID Matrícula: {matricula.id_matricula}\n'
          f'Fecha matrícula: {matricula.fecha_matricula}\n')
