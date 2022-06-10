class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        if producto.typ =='hc':
            id = 'hc'+str(producto.id)
            if id not in self.carrito.keys():
                self.carrito[id]={
                    "producto_id": id,
                    "nombre": producto.name,
                    "acumulado": producto.price,
                    "cantidad": 1,
                }
            else:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += 1000
            self.guardar_carrito()

        elif producto.typ =='h':
            id = 'h'+str(producto.id)
            if id not in self.carrito.keys():
                self.carrito[id]={
                    "producto_id": id,
                    "nombre": "hand - "+str(producto.id),
                    "acumulado": 1000,
                    "cantidad": 1,
                }
            else:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += 1000
            self.guardar_carrito()

        elif producto.typ =='al':
            id = 'al'+str(producto.id)
            if id not in self.carrito.keys():
                self.carrito[id]={
                    "producto_id": id,
                    "nombre": 'al '+ str(producto.id),
                    "acumulado": 1000,
                    "cantidad": 1,
                }
            else:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += 1000
            self.guardar_carrito()

        elif producto.typ =='b':
            id = 'b'+str(producto.id)
            if id not in self.carrito.keys():
                self.carrito[id]={
                    "producto_id": id,
                    "nombre": 'b '+ str(producto.id),
                    "acumulado": 1000,
                    "cantidad": 1,
                }
            else:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += 1000
            self.guardar_carrito()

        elif producto.typ =='des':
            id = 'des'+str(producto.id)
            if id not in self.carrito.keys():
                self.carrito[id]={
                    "producto_id": id,
                    "nombre": 'des '+ str(producto.id),
                    "acumulado": 1000,
                    "cantidad": 1,
                }
            else:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += 1000
            self.guardar_carrito()

        elif producto.typ =='kai':
            id = 'kai'+str(producto.id)
            if id not in self.carrito.keys():
                self.carrito[id]={
                    "producto_id": id,
                    "nombre": producto.name,
                    "acumulado": producto.price,
                    "cantidad": 1,
                }
            else:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += 1000
            self.guardar_carrito()

        elif producto.typ =='sell':
            id = 'sell'+str(producto.id)
            if id not in self.carrito.keys():
                self.carrito[id]={
                    "producto_id": id,
                    "nombre": producto.name,
                    "acumulado": producto.price,
                    "cantidad": 1,
                }
            else:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += 1000
            self.guardar_carrito()
            
        else:
            print('sss')
 
        

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.price
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True