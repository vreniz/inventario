# Mensaje de bienvenida al usuario
print("Welcome to the Inventory data entry")
# Variable de control para repetir el proceso
iteracion= True
# Ciclo principal del programa
while iteracion:
    
    # -----------------------------
    # Solicitar y validar el nombre del producto
    # (solo permite letras y espacios, no vacío)
    # -----------------------------
 nombreval = False
 while not nombreval:# PUEDE SER TAMBIÉN UN WHILE NOMBREVAL==FALSE:
        nombre = input("Enter Product Name: ")
        if nombre.strip() == "":
            print("Error name can not be empty")
        elif nombre.replace(" ", "").isalpha():
            nombreval = True
        else:
            print("Error ❌: name must contain only letters and spaces")
    # -----------------------------
    # Solicitar y validar el precio del producto
    # (número flotante positivo, acepta coma o punto)
    # -----------------------------
 while True: 
     entrada_precio = input("Enter product price: ") # 
     entrada_clean = entrada_precio.replace(",", ".") 
     if entrada_clean.count(".") > 1: 
        print("Error ❌, invalid format (too many decimals)") 
        continue 
     try: #1
         precio = float(entrada_clean) 
         if precio > 0: 
            break 
         else:
             print("Error ❌, price must be a positive number") 
     except ValueError:
         print("Error ❌, Please enter a valid number for price (e.g. 1.0 or 1,0) ") 
    # -----------------------------
    # Solicitar y validar la cantidad del producto
    # (número entero positivo, no admite string y tiene que ser diferente de 0)
    # -----------------------------        
 while True: # 
      entrada_cantidad = input("Enter Product Quantity: ") 
      try: #1
            cantidad= int(entrada_cantidad) 
            if cantidad > 0: 
             break 
            elif cantidad == 0: 
                 print("Error ❌, quantity cannot be zero")
            else: 
                print("Error ❌, the quantity must be a positive integer") 
      except ValueError: 
          print("Error ❌, Please enter a valid integer number for Quantity ")   
    # -----------------------------
    # Calcular el costo total
    # ----------------------------- 
 costo_total=(precio * cantidad) 
    # -----------------------------
    # Mostrar los resultados al usuario
    # -----------------------------
 print(f"Product Name: {nombre} | Price: {precio} | Quantity: {cantidad} | Total: {costo_total}")
    # -----------------------------
    # Preguntar al usuario si desea continuar
    # -----------------------------
 continuar = input("Do you wish to enter a new product? yes/no: ").strip().lower()
  # Validar que la opción sea correcta
 while continuar !="yes" and continuar !="no":
     print("Option NOT valid ❌")
     continuar = input("Do you wish to enter a new product? yes/no: ").strip().lower()
  # Controlar la continuación del programa
 if continuar == "yes":
  iteracion = True
 else:
  iteracion = False
  print("Thanks for entering new data!!!")
# -------------------------------------------------
# Este programa permite ingresar datos de productos
# (nombre, precio y cantidad), valida cada entrada,
# calcula el costo total y muestra los resultados.
# Además, permite al usuario ingresar múltiples productos hasta que lo desee.
# -------------------------------------------------