class Calificaciones:
    def __init__(self):
        self.calificaciones = []

    def ingresar_calificaciones(self):
        print("Ingrese al menos 5 calificaciones (0-100):")
        while len(self.calificaciones) < 5:
            try:
                cal = float(input(f"Ingrese calificación {len(self.calificaciones)+1}: "))
                if 0 <= cal <= 100:
                    self.calificaciones.append(cal)
                else:
                    print("La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Debe ingresar un número válido.")
    
        while True:
            mas = input("¿Desea agregar otra calificación? (s/n): ").lower()
            if mas == "s":
                try:
                    cal = float(input(f"Ingrese calificación {len(self.calificaciones)+1}: "))
                    if 0 <= cal <= 100:
                        self.calificaciones.append(cal)
                    else:
                        print("La calificación debe estar entre 0 y 100.")
                except ValueError:
                    print("Debe ingresar un número válido.")
            elif mas == "n":
                break
            else:
                print("Ingrese 's' o 'n'")

    
    def promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0

    def registro_calificaciones(self):
        if not self.calificaciones:
            print("No hay calificaciones registradas.")
            return
        print("\n------ DETALLES DE CALIFICACIONES ------")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Calificación máxima: {max(self.calificaciones)}")
        print(f"Calificación mínima: {min(self.calificaciones)}")
        print(f"Promedio: {self.promedio():.2f}")
        print("----------------------------------------\n")

    def menu(self):
        while True:
            print("1. Ingresar calificaciones")
            print("2. Calcular promedio")
            print("3. Mostrar registro de calificaciones")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.ingresar_calificaciones()
            elif opcion == "2":
                if not self.calificaciones:
                    print("No hay calificaciones registradas.\n")
                else:
                    print(f"El promedio es: {self.promedio():.2f}\n")
            elif opcion == "3":
                self.registro_calificaciones()
            elif opcion == "4":
                print("¡Saliendo del programa!")
                break
            else:
                print("Opción inválida. Intente de nuevo.\n")


notas = Calificaciones()
notas.menu()
