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
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.name,
                "acumulado": producto.price,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.price
        self.guardar_carrito()

    def agregar_almuerzo(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.name,
                "acumulado": producto.price,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.price
        self.guardar_carrito()

    def agregar_handclassic(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "handclassic_id": producto.id,
                "nombre": producto.name,
                "acumulado": 1000,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.price
        self.guardar_carrito()

    def agregarBowl(self, bowl):
        id = str(bowl.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "bowl_id": bowl.id,
                "proteina": bowl.proteina.name,
                "base": bowl.base.name,
                "salsa1": bowl.salsa1.name,
                "salsa2": bowl.salsa2.name,
                "extra1": bowl.extra1.name,
                "extra2": bowl.extra2.name,
                "extra3": bowl.extra3.name,
                "extra4": bowl.extra4.name,
                "extra5": bowl.extra5.name,
                "extra6": bowl.extra6.name,
                "extra7": bowl.extra7.name,
                "extra8": bowl.extra8.name,
                "extra9": bowl.extra9.name,
                "extra10": bowl.extra10.name,
                "acumulado": 1000,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.price
        self.guardar_carrito()

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