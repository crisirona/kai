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
                    "acumulado": 1000,
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
                    "nombre": producto.name,
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
        elif producto.typ =='sell':
            id = 'sell'+str(producto.id)
            if id not in self.carrito.keys():
                self.carrito[id]={
                    "producto_id": id,
                    "nombre": producto.name,
                    "acumulado": 1000,
                    "cantidad": 1,
                }
            else:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += 1000
            self.guardar_carrito()
        else:
            print('sss')
 
        

    # def agregar_almuerzo(self, producto):
    #     id = str('a'+producto.id)
    #     if id not in self.carrito.keys():
    #         self.carrito[id]={
    #             "producto_id": producto.id,
    #             "nombre": producto.name,
    #             "acumulado": producto.price,
    #             "cantidad": 1,
    #         }
    #     else:
    #         self.carrito[id]["cantidad"] += 1
    #         self.carrito[id]["acumulado"] += producto.price
    #     self.guardar_carrito()

    # def agregar_handclassic(self, producto):
    #     id = str('hc'+producto.id)
    #     if id not in self.carrito.keys():
    #         self.carrito[id]={
    #             "handclassic_id": producto.id,
    #             "nombre": producto.name,
    #             "acumulado": 1000,
    #             "cantidad": 1,
    #         }
    #     else:
    #         self.carrito[id]["cantidad"] += 1
    #         self.carrito[id]["acumulado"] += 1000
    #     self.guardar_carrito()

    # def agregarBowl(self, bowl):
    #     id = str('b'+bowl.id)
    #     if id not in self.carrito.keys():
    #         self.carrito[id]={
    #             "bowl_id": bowl.id,
    #             "proteina": bowl.proteina.name,
    #             "base": bowl.base.name,
    #             "salsa1": bowl.salsa1.name,
    #             "salsa2": bowl.salsa2.name,
    #             "extra1": bowl.extra1.name,
    #             "extra2": bowl.extra2.name,
    #             "extra3": bowl.extra3.name,
    #             "extra4": bowl.extra4.name,
    #             "extra5": bowl.extra5.name,
    #             "extra6": bowl.extra6.name,
    #             "extra7": bowl.extra7.name,
    #             "extra8": bowl.extra8.name,
    #             "extra9": bowl.extra9.name,
    #             "extra10": bowl.extra10.name,
    #             "acumulado": 1000,
    #             "cantidad": 1,
    #         }
    #     else:
    #         self.carrito[id]["cantidad"] += 1
    #         self.carrito[id]["acumulado"] += producto.price
    #     self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    # def eliminar_hc(self, producto):
    #     id = str(producto.id)
    #     if id in self.carrito:
    #         del self.carrito[id]
    #         self.guardar_carrito()


    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.price
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    # def restar_hc(self, producto):
    #     id = str(producto.id)
    #     if id in self.carrito.keys():
    #         self.carrito[id]["cantidad"] -= 1
    #         self.carrito[id]["acumulado"] -= 1000
    #         if self.carrito[id]["cantidad"] <= 0: self.eliminar_hc(producto)
    #         self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True