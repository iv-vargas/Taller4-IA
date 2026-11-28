"""Punto 5. Inferencia mediante encadenamiento hacia adelante."""
from models.logic import match_premises, substitute


def forward_chain(kb):
    """Retorna una tupla con los hechos originales y derivados, sin duplicados.

    Cada ronda usa los hechos disponibles al comenzarla. La base de entrada
    debe conservarse.
    kb.facts contiene objetos Atom; kb.rules contiene objetos Rule con los
    atributos premises y conclusion. Los hechos se comparan directamente.

    Tips:
    - match_premises(regla.premises, hechos) genera (sustitución, hechos usados).
      Si no hay coincidencias, no genera resultados. La sustitución es un
      diccionario, por ejemplo {'?p': 'ana'}.
    - substitute(regla.conclusion, sustitución) retorna un nuevo objeto Atom
      con las variables reemplazadas por los valores de la sustitución.
      
      
      
      
      Codigo propuesto antes de la revisión con IA. Se hizo siguiendo los pseudocódigos del curso:
      En los comentarios al lado del codigo explicamos brevemente los cambios sugeridos por la IA a cada parte de nuestro codigo.
      
      hechos_copia = []
          for hecho in kb.facts:
              if hecho not in hechos_copia:
                  hechos_copia.append(hecho)   Inicialmente se creaba la copia vacia y se copiaba manualmente para asegurarnos que no tenemos hechos repetidos.
                                                La IA nos ayudó a notar que este loop no es necesario porque la implementación de KnowledgeBase no permite duplicados (lanza un error si hay repetidos). 
                                                Por este motivo copiamos directamente hechos.
                                                
                                                Por otro lado, la IA propuso tener un set que guarda todo lo conocido (iniciales + inferidos) de esta forma es mas rapido porque la busqueda en set es O(1)
                  
          while True:                                   
              foto = hechos_copia.copy()                
              nuevos_hechos = []                        
      
              for regla in kb.rules:                    
                  for sustitucion, _usados in match_premises(regla.premises, foto):     En lugar de pasarle a match premises la "foto" nos indicó que podemos pasar hechos directamente porque este no cambia durante la ronda.
                      conclusion = substitute(regla.conclusion, sustitucion)
                      if conclusion not in hechos_copia and conclusion not in nuevos_hechos:    Como creamos un set de vistos, ya no hace falta revisar en hechos_copia y nuevos hechos por separado, pues vistos contiene todo lo conocido
                                                                                                La verificación de una conclusión entonces puede hacerse sencillamente con: not in vistos.
                          nuevos_hechos.append(conclusion)
                          
              if len(nuevos_hechos) == 0:               
                  break                           en lugar de detener el loop la IA nos sugirió retornar los hechos
      
              for h in nuevos_hechos:                  En lugar de añadir uno a uno los nuevos hechos, nos sugirió usar el metodo .extend el cual añade al final de una lista todos los elementos de otro iterable.
                  hechos_copia.append(h)
      
          
          return tuple(hechos_copia)  Ya no se usa este return final porque ahora retornamos si no hay nuevos hechos en la ronda.
      
    """

    hechos = list(kb.facts)     
    vistos = set(hechos)       

    while True:                
        nuevos_hechos = []            
        for regla in kb.rules:
            for sustitucion, _usados in match_premises(regla.premises, hechos): 
                conclusion = substitute(regla.conclusion, sustitucion)          
                if conclusion not in vistos:      
                    vistos.add(conclusion)
                    nuevos_hechos.append(conclusion)
        if not nuevos_hechos:
            return tuple(hechos)  
        hechos.extend(nuevos_hechos)     
    # FIN DEL BLOQUE DEL ESTUDIANTE
