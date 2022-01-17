num1 = 42 #declara variable
num2 = 2.3 # declara variable
boolean = True # declara variable boolena
string = 'Hello World' # declara variable, es un string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # declara arreglo
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # declara diccionario
fruit = ('blueberry', 'strawberry', 'banana')#declara tupla
print(type(fruit)) # imprime la clase (tupla)
print(pizza_toppings[1]) #imprime el elemento 1 del arreglo pizza_toppings
pizza_toppings.append('Mushrooms') # agrega elemento Mushorooms al arreglo pizza_toppings
print(person['name']) # imprimer el elemento name ( jhon) del diccionario person
person['name'] = 'George'#cambia el elemento name de jhon a goerge
person['eye_color'] = 'blue'#agrega el elemento eye_color: blue al diccionario person
print(fruit[2])#imprimer el elemtno de la posicion 2 de la tupla fruit

if num1 > 45: 
    print("It's greater") #condicional si el numero es mayor que 45 imprime It's greater
else: 
    print("It's lower") # sino It's lower

if len(string) < 5: 
    print("It's a short word!") # condicional de el la longitud del string en menor que 5 imprime it's a short word!
elif len(string) > 15:
    print("It's a long word!") # condiiona si el string es mayor que 15 imprime It's a long word!
else:
    print("Just right!") # sino imprime Just right!

for x in range(5):
    print(x) # imprime los 5 aumentnado de 1 en 1 valores 0,1,2,3,4
for x in range(2,5): 
    print(x) #imprime los del 2 al 5 
for x in range(2,10,3): 
    print(x) #imprimer los valores del 2 al 10 aumentado en 3 en 3

x = 0 # declara la variable x = 0
while(x < 5): 
    print(x)  #condicional imprime todos los valores menores que 5 aumentado de 1 en 1
    x += 1 

pizza_toppings.pop() # elimina el ultimo elemento del arreglo pizza_toppings
pizza_toppings.pop(1)# elimina el elemento de la posicion 1 del arreglo pizza_toppings


print(person) # imprimer el diccionario person
person.pop('eye_color') # eliminar el elemento eye_color del diccionario
print(person) # imprimir nuevamente el diccionario ya modificado
print(pizza_toppings)
for topping in pizza_toppings:
    if topping == 'Pepperoni': # si topping es pepperoni continua        
        continue
    print('After 1st if statement') # imprime el mensaje por cada elemtnto depues del elemento pepperoni
    if topping == 'Olives': # si el topping es olives se rompe el bucle
        break

def print_hello_ten_times(): # declara la funcion
    for num in range(10):
        print('Hello') # se imprime 10 veces hello por el rango que es 10

print_hello_ten_times() # se llama a la funcion

def print_hello_x_times(x): # declara la funcion
    for num in range(x):
        print('Hello') # se imprime x veces hello debido al range que es x

print_hello_x_times(4) # se llama la funcion donde x = 4

def print_hello_x_or_ten_times(x = 10): # se declara la funcion dende x puede tomar cualquier valor o 10
    for num in range(x): 
        print('Hello') # imprime el valor x veces o 10 por defecto

print_hello_x_or_ten_times() #imprime el valor 10 veces 
print_hello_x_or_ten_times(4) # imprime el valor 4 veces debido a que x = 4


"""
Bonus section
"""
num3 = 72 # declara el valor num3 = 72
print(num3) # imprime el valor num3
fruit[0] = 'cranberry' # error no se puede cambiar un valor de la posicion 0 al tuple fruit
print(person['favorite_team']) # error el elemnto favorite_team no esta declarada el en diccionario person
print(pizza_toppings[7]) # error no existe el valor en la posicion 7 del arreglo
print(boolean) # imprime la variable boolean True
fruit.append('raspberry') #no se puede agregar un elemento a tuple 
fruit.pop(1)# no se puede eliminar un elemetno de un tuple