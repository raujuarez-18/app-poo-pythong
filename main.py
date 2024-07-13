from model.persona import Persona
from model.curso import Curso

#creando la instancia de Persona en el objeto objpersona
objpersona = Persona("Luis","Salvatierra",
                     "12304040",
                     "lsalvatierra@gmail.com")

objpersona.saludar()

#creando la instancia de Curso en el objeto objCurso
objCurso = Curso("PG001", "programacion",5 )
objCurso.bienvenido()
objCurso.set_credito(4)
objCurso.bienvenido()
