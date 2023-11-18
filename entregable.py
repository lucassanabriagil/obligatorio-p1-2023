import random
class Empleado:
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.salario = salario


class Piloto(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score
        self.numero_auto = numero_auto
        self.puntaje_campeonato = 0
        self.lesionado = False
        self.score_final = 0


class Mecanico(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score


class DirectorEquipo(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)


class Auto:
    def __init__(self, modelo, año, score):
        self.modelo = modelo
        self.año = año
        self.score = score
        


class Gestor:
    def __init__(self):
        self.empleados = []
        self.autos = []
        self.empleados_generales = []
        self.equipos = {}

    def validar_id(self, id_empleado):
        if len(str(id_empleado)) != 8:
            raise ValueError("El ID debe tener 8 números.")

    def validar_fecha_nacimiento(self, fecha_nacimiento):
        
        pass

    def validar_score(self, score):
        if not 1 <= score <= 99:
            raise ValueError("El score debe estar entre 1 y 99.")

    def validar_numero_auto(self, numero_auto):
        if numero_auto is not None and not isinstance(numero_auto, int):
            raise ValueError("El número de auto debe ser un número entero.")

    def alta_empleado(self):
            print("Ingrese los datos del empleado:")
            empleado = None  
            try:
                id_empleado = int(input("Ingrese cedula: "))
                self.validar_id(id_empleado)

                nombre = input("Ingrese nombre: ")
                fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
                self.validar_fecha_nacimiento(fecha_nacimiento)

                nacionalidad = input("Ingrese nacionalidad: ")
                salario = float(input("Ingrese salario: "))

                cargo = int(input("Ingrese cargo (1: Piloto, 2: Piloto de reserva, 3: Mecánico, 4: Jefe de equipo): "))
                if cargo == 1:
                    score = int(input("Ingrese score del piloto (1-99): "))
                    self.validar_score(score)

                    numero_auto = int(input("Ingrese número de auto del piloto: "))
                    self.validar_numero_auto(numero_auto)
                    empleado = Piloto(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score, numero_auto)
                elif cargo == 2:
                    score = int(input("Ingrese score del piloto de reserva (1-99): "))
                    self.validar_score(score)
                    empleado = Piloto(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score, None)
                elif cargo == 3:
                    score = int(input("Ingrese score del mecánico (1-99): "))
                    self.validar_score(score)
                    empleado = Mecanico(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario, score)
                elif cargo == 4:
                    empleado = DirectorEquipo(id_empleado, nombre, fecha_nacimiento, nacionalidad, salario)

                if empleado:
                    self.empleados.append(empleado)
                    self.empleados_generales.append(empleado)  
                    print("Empleado registrado exitosamente.")

            except ValueError as e:
                print(f"Error: {e}. Ingrese un valor válido para el campo correspondiente.")


    def validar_año(self, año):
        if not isinstance(año, int):
            raise ValueError("El año del auto debe ser un número entero.")

    def alta_auto(self):
        print("Ingrese los datos del auto:")
        try:
            modelo = input("Ingrese modelo del auto: ")
            año = int(input("Ingrese año del auto: "))
            self.validar_año(año)

            score = int(input("Ingrese score del auto (1-99): "))
            self.validar_score(score)

            auto = Auto(modelo, año, score)
            self.autos.append(auto)
            print("Modelo de auto registrado exitosamente.")

        except ValueError as e:
            print(f"Error: {e}. Ingrese un valor válido para el campo correspondiente.")

    def alta_equipo(self):
        print("Ingrese los datos del equipo:")
        try:
            nombre_equipo = input("Ingrese nombre del equipo: ")

            print("Autos disponibles:")
            for idx, auto in enumerate(self.autos, start=1):
                print(f"{idx}. Modelo: {auto.modelo}, Año: {auto.año}, Score: {auto.score}")

            idx_auto_elegido = int(input("Seleccione un auto para el equipo (ingrese el número correspondiente): ")) - 1
            auto_elegido = self.autos[idx_auto_elegido]

            empleados_equipo = []

            # Reutilizar empleados ya creados
            while True:
                print("\nSeleccione un empleado existente para agregar al equipo:")
                print("0. Ver empleados existentes")
                print("1. Seleccionar empleado")
                print("2. Volver al menu principal")
                opcion = input("Seleccione una opción: ")
                if opcion == '0':
                    print("Empleados existentes:")
                    for idx, empleado in enumerate(self.empleados_generales, start=1):
                        print(f"{idx}. {empleado.nombre} - {type(empleado).__name__}")

                elif opcion == '1':
                    print("Seleccione un empleado para agregar al equipo:")
                    for idx, empleado in enumerate(self.empleados_generales, start=1):
                        print(f"{idx}. {empleado.nombre} - {type(empleado).__name__}")

                    idx_empleado = int(input("Ingrese el número correspondiente al empleado: ")) - 1
                    empleado_seleccionado = self.empleados_generales[idx_empleado]
                    empleados_equipo.append(empleado_seleccionado)
                    print(f"{empleado_seleccionado.nombre} agregado al equipo.")

                else:
                    break

            equipo = {
                "nombre": nombre_equipo,
                "auto": auto_elegido,
                "empleados": empleados_equipo
            }
            self.equipos[nombre_equipo] = list(filter(lambda empleado: isinstance(empleado, Piloto), empleados_equipo))

            # Asignar el nombre del equipo al atributo 'equipo' de los pilotos seleccionados
            pilotos_seleccionados = filter(lambda empleado: isinstance(empleado, Piloto), empleados_equipo)
            for piloto in pilotos_seleccionados:
                piloto.equipo = nombre_equipo
            print("Equipo registrado exitosamente.")
            

            return equipo

        except ValueError as e:
            print(f"Error: {e}. Ingrese un valor válido para el campo correspondiente.")

    def simular_carrera(self):
        print("\n---- Simulación de Carrera ----")

        # Input de pilotos lesionados
        pilotos_lesionados = input("Ingrese números de auto de pilotos lesionados separados por coma (si ninguno, dejar vacío): ").split(',')
        for piloto in self.empleados:
            if isinstance(piloto, Piloto) and str(piloto.numero_auto) in pilotos_lesionados:
                piloto.lesionado = True

        # Input de pilotos que abandonan la carrera
        pilotos_abandonan = input("Ingrese números de auto de pilotos que abandonan separados por coma (si ninguno, dejar vacío): ").split(',')
        for piloto in self.empleados:
            if isinstance(piloto, Piloto) and str(piloto.numero_auto) in pilotos_abandonan:
                print(f"{piloto.nombre} ha abandonado la carrera.")
                # Restablecer el puntaje final del piloto que abandona
                piloto.score_final = 0

        # Input de pilotos con error en pits
        pilotos_error_pits = input("Ingrese números de auto de pilotos con error en pits separados por coma (si ninguno, dejar vacío): ").split(',')
        for piloto in self.empleados:
            if isinstance(piloto, Piloto) and str(piloto.numero_auto) in pilotos_error_pits:
                print(f"{piloto.nombre} ha tenido un error en los pits (-5 puntos).")
                piloto.score_final -= 5

        # Input de pilotos con penalidad
        pilotos_penalidad = input("Ingrese números de auto de pilotos con penalidad separados por coma (si ninguno, dejar vacío): ").split(',')
        for piloto in self.empleados:
            if isinstance(piloto, Piloto) and str(piloto.numero_auto) in pilotos_penalidad:
                print(f"{piloto.nombre} ha recibido una penalidad (-8 puntos).")
                piloto.score_final -= 8

        # Ordenar los pilotos por puntaje final de manera descendente
        pilotos_activos = [piloto for piloto in self.empleados if isinstance(piloto, Piloto) and not piloto.lesionado]
        pilotos_activos.sort(key=lambda x: x.score_final, reverse=True)

        # Asignar puntos a los pilotos según su posición en la carrera
        puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
        for i, piloto in enumerate(pilotos_activos):
            if i < len(puntos):
                piloto.puntaje_campeonato += puntos[i]

        # Restablecer estado de lesiones al finalizar la carrera
        for piloto in pilotos_activos:
            piloto.lesionado = False

        # Imprimir pilotos ordenados por el resultado de la carrera
        print("Resultados de la Carrera:")
        for i, piloto in enumerate(pilotos_activos, start=1):
            print(f"{i}. {piloto.nombre}")

        print("Carrera simulada exitosamente.")

        for piloto in pilotos_activos:
            if piloto.lesionado:
                piloto.score_final = 0
            else:
                suma_score_mecanicos = sum(empleado.score for empleado in self.empleados if isinstance(empleado, Mecanico))
                score_auto = piloto.score
                score_piloto = piloto.score

                cantidad_errores_en_pits = len([p for p in pilotos_error_pits if p == str(piloto.numero_auto)])
                cantidad_penalidad_infringir_norma = len([p for p in pilotos_penalidad if p == str(piloto.numero_auto)])

                piloto.score_final = suma_score_mecanicos + score_auto + score_piloto - 5 * cantidad_errores_en_pits - 8 * cantidad_penalidad_infringir_norma

        # Ordenar los pilotos por score_final de manera descendente
        pilotos_activos.sort(key=lambda x: x.score_final, reverse=True)
        pass
    def top_10_pilotos_mas_puntos(self):
        pilotos = [empleado for empleado in self.empleados if isinstance(empleado, Piloto)]
        pilotos_ordenados = sorted(pilotos, key=lambda x: x.puntaje_campeonato, reverse=True)
        return [f"{piloto.nombre}: {piloto.puntaje_campeonato} puntos" for piloto in pilotos_ordenados[:10]]

    def resumen_campeonato_constructores(self):
        # Sumar puntos por equipo
        puntos_por_equipo = {}
        for empleado in self.empleados:
            if isinstance(empleado, Piloto):
                equipo = empleado.equipo.nombre if empleado.equipo else "Sin equipo"
                if equipo not in puntos_por_equipo:
                    puntos_por_equipo[equipo] = 0
                puntos_por_equipo[equipo] += empleado.puntaje_campeonato

        return puntos_por_equipo

    def top_5_pilotos_mejores_pagos(self):
        # Obtener los 5 empleados (pilotos) con los salarios más altos
        pilotos = [empleado for empleado in self.empleados if isinstance(empleado, Piloto)]
        pilotos_ordenados_salario = sorted(pilotos, key=lambda x: x.salario, reverse=True)
        return [f"{piloto.nombre}: ${piloto.salario}" for piloto in pilotos_ordenados_salario[:5]]

    def top_3_pilotos_habilidosos(self):
        # Obtener los 3 pilotos más habilidosos por su score
        pilotos_ordenados_score = sorted([empleado for empleado in self.empleados if isinstance(empleado, Piloto)],
                                         key=lambda x: x.score, reverse=True)
        return [f"{piloto.nombre}: Score {piloto.score}" for piloto in pilotos_ordenados_score[:3]]

    def jefes_de_equipo(self):
        # Obtener jefes de equipo y su equipo
        jefes_equipo = [f"{empleado.nombre} - Equipo: {empleado.equipo.nombre}" for empleado in self.empleados if isinstance(empleado, DirectorEquipo)]
        return sorted(jefes_equipo)  # Ordenar por nombre del jefe de equipo

    def realizar_consulta(self):
        print("\nSeleccione el tipo de consulta:")
        print("1. Top 10 pilotos con más puntos en el campeonato")
        print("2. Resumen campeonato de constructores (equipos)")
        print("3. Top 5 pilotos mejores pago")
        print("4. Top 3 pilotos más habilidosos")
        print("5. Retornar jefes de equipo")

        tipo_consulta = input("Seleccione una opción de consulta: ")

        if tipo_consulta == '1':
            resultados = self.top_10_pilotos_mas_puntos()
        elif tipo_consulta == '2':
            resultados = self.resumen_campeonato_constructores()
        elif tipo_consulta == '3':
            resultados = self.top_5_pilotos_mejores_pagos()
        elif tipo_consulta == '4':
            resultados = self.top_3_pilotos_habilidosos()
        elif tipo_consulta == '5':
            resultados = self.jefes_de_equipo()
        else:
            resultados = "Consulta no válida."

        if resultados == "Consulta no válida.":
            print("Consulta no válida. Por favor, seleccione una opción válida.")
        else:
            print("\n----- Resultados de la consulta -----")
            for idx, resultado in enumerate(resultados, start=1):
                print(f"{idx}. {resultado}")

    def consultar(self, tipo_consulta):
        if tipo_consulta == "pilotos_puntos":
            pilotos_por_puntos = sorted(self.empleados, key=lambda x: x.puntaje_campeonato, reverse=True)[:10]
            return pilotos_por_puntos

        elif tipo_consulta == "resumen_constructores":
            equipos = {}
            for empleado in self.empleados:
                if isinstance(empleado, Piloto):
                    if empleado.numero_auto in equipos:
                        equipos[empleado.numero_auto] += empleado.puntaje_campeonato
                    else:
                        equipos[empleado.numero_auto] = empleado.puntaje_campeonato
            return sorted(equipos.items(), key=lambda x: x[1], reverse=True)

        elif tipo_consulta == "top_pago":
            pilotos_por_salario = sorted(self.empleados, key=lambda x: x.salario, reverse=True)[:5]
            return pilotos_por_salario

        elif tipo_consulta == "top_habilidosos":
            pilotos_por_habilidad = sorted(self.empleados, key=lambda x: x.score, reverse=True)[:3]
            return pilotos_por_habilidad

        elif tipo_consulta == "jefes_equipo":
            jefes_de_equipo = [empleado for empleado in self.empleados if isinstance(empleado, DirectorEquipo)]
            jefes_de_equipo = sorted(jefes_de_equipo, key=lambda x: x.nombre)
            
            equipos_lideres = []
            for jefe in jefes_de_equipo:
                for empleado in self.empleados:
                    if isinstance(empleado, Piloto) and empleado.numero_auto == jefe.id:
                        equipos_lideres.append((jefe, empleado.numero_auto))

            return equipos_lideres

        else:
            return "Consulta no válida."
    
    
    def menu_principal(self):
        while True:
            print("\n----- Menú Principal -----")
            print("1. Alta de empleado")
            print("2. Alta de auto")
            print("3. Alta de equipo")
            print("4. Simular carrera")
            print("5. Realizar consulta")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.alta_empleado()
            elif opcion == '2':
                self.alta_auto()
            elif opcion == '3':
                equipo = self.alta_equipo()
                
            elif opcion == '4':
                self.simular_carrera()
            elif opcion == '5':
                self.realizar_consulta()
            elif opcion == '6':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def realizar_consulta(self):
        print("\nSeleccione el tipo de consulta:")
        print("1. Top 10 pilotos con más puntos en el campeonato")
        print("2. Resumen campeonato de constructores (equipos)")
        print("3. Top 5 pilotos mejores pagados")
        print("4. Top 3 pilotos más habilidosos")
        print("5. Retornar jefes de equipo")

        tipo_consulta = input("Seleccione una opción de consulta: ")

        if tipo_consulta == '1':
            resultados = self.top_10_pilotos_mas_puntos()
        elif tipo_consulta == '2':
            resultados = self.resumen_campeonato_constructores()
        elif tipo_consulta == '3':
            resultados = self.top_5_pilotos_mejores_pagos()
        elif tipo_consulta == '4':
            resultados = self.top_3_pilotos_habilidosos()
        elif tipo_consulta == '5':
            resultados = self.jefes_de_equipo()
        else:
            print("Consulta no válida. Por favor, seleccione una opción válida.")
            return

        print("\n----- Resultados de la consulta -----")
        for idx, resultado in enumerate(resultados, start=1):
            print(f"{idx}. {resultado}")
            


if __name__ == "__main__":
    gestor = Gestor()
    gestor.menu_principal()
