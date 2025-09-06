class Empleado:
    def __init__(self):
        self.empleados = []

    def registrar_empleado(self):
        nombre = input("Ingrese nombre del empleado: ")
        puesto = input("Ingrese puesto: ")
        try:
            sueldo = float(input("Ingrese sueldo: "))
        except ValueError:
            print("Debe ingresar un número para el sueldo.")
            return
        self.empleados.append({
            "nombre": nombre,
            "puesto": puesto,
            "sueldo": sueldo,
            "bono": 0  
        })
        print(f"Empleado {nombre} registrado correctamente.\n")

    def calcular_bono(self, empleado):
        try:
            porcentaje = float(input(f"Ingrese porcentaje de bono para {empleado['nombre']}: "))
        except ValueError:
            print("Debe ingresar un número.")
            return 0
        bono = empleado["sueldo"] * porcentaje / 100
        empleado["bono"] = bono
        print(f"Bono de ${bono:.2f} asignado a {empleado['nombre']}.\n")
        return bono

    def calcular_sueldo_neto(self, empleado):
        total = empleado["sueldo"] + empleado["bono"]
        impuestos = total * 0.10 if total > 3000 else 0
        sueldo_neto = total - impuestos
        return sueldo_neto, impuestos

    def mostrar_recibo(self, empleado):
        sueldo_neto, impuestos = self.calcular_sueldo_neto(empleado)
        print("\n------ RECIBO DE PAGO ------")
        print(f"Empleado: {empleado['nombre']}")
        print(f"Puesto: {empleado['puesto']}")
        print(f"Sueldo base: ${empleado['sueldo']:.2f}")
        print(f"Bono: ${empleado['bono']:.2f}")
        print(f"Impuestos: ${impuestos:.2f}")
        print(f"Sueldo neto: ${sueldo_neto:.2f}")
        print("----------------------------\n")

    def menu(self):
        while True:
            print("1. Registrar empleado")
            print("2. Asignar bono a un empleado")
            print("3. Mostrar recibos de todos los empleados")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_empleado()

            elif opcion == "2":
                if not self.empleados:
                    print("No hay empleados registrados.\n")
                else:
                    print("\nEmpleados registrados:")
                    for idx, emp in enumerate(self.empleados, start=1):
                        print(f"{idx}. {emp['nombre']} (Sueldo: ${emp['sueldo']:.2f})")
                    try:
                        eleccion = int(input("Seleccione el número del empleado: "))
                        if 1 <= eleccion <= len(self.empleados):
                            empleado_seleccionado = self.empleados[eleccion - 1]
                            self.calcular_bono(empleado_seleccionado)
                        else:
                            print("Número de empleado inválido.\n")
                    except ValueError:
                        print("Debe ingresar un número.\n")

            elif opcion == "3":
                if not self.empleados:
                    print("No hay empleados registrados.\n")
                else:
                    for emp in self.empleados:
                        self.mostrar_recibo(emp)

            elif opcion == "4":
                print("¡Saliendo del programa!")
                break

            else:
                print("Opción inválida. Intente de nuevo.\n")

empresa = Empleado()
empresa.menu()
