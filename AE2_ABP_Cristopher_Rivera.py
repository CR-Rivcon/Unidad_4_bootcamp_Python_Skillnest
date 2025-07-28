class TarjetaCredito:
    def __init__(self, limite_credito=100000, intereses=0.0):
        self.saldo_pagar = 0
        self.limite_credito = limite_credito
        self.intereses = intereses

    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

# Crear 3 tarjetas
tarjeta1 = TarjetaCredito(limite_credito=100000, intereses=0.01)
tarjeta2 = TarjetaCredito(limite_credito=200000, intereses=0.01)
tarjeta3 = TarjetaCredito(limite_credito=150000, intereses=0.01)

# Primera tarjeta: 2 compras, 1 pago, cobra intereses y muestra info (encadenado)
tarjeta1.compra(15000).compra(30000).pago(20000).cobrar_interes().mostrar_info_tarjeta()

# Segunda tarjeta: 3 compras, 2 pagos, cobra intereses y muestra info (encadenado)
tarjeta2.compra(1000).compra(12000).compra(19000).pago(5000).pago(15000).cobrar_interes().mostrar_info_tarjeta()

# Tercera tarjeta: 5 compras, excede límite, muestra info (encadenado)
tarjeta3.compra(10000).compra(20000).compra(10000).compra(65000).compra(50000).mostrar_info_tarjeta()
