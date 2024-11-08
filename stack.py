class stack:
    def __init__(self):
        self.pila = []
        
    def esta_vacia(self):
        return len(self.pila) == 0
    #metodo push
    def agregar_elemento(self,elemento):
        self.pila.append(elemento)
    #metodo pop
    def agregar_elemento(self,elemento):
        self.pila.remove(elemento)
    
if __name__ == "__main__":
    stacks = stack()
    
if stacks.esta_vacia():
    print("La pila esta vacia")
