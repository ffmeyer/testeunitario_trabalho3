class Restaurant:
    """Model de restaurante simples."""

    ZERO_CLIENTS_SERVED = 0

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = self.ZERO_CLIENTS_SERVED
        self.open = False

    def describe_restaurant(self):
        """
        #1 - incluir retorno do metodo str, e alteracao do restaurant.name
        """
        """Imprima uma descrição simples da instância do restaurante."""
        return f"""Esse restaurante chama {self.restaurant_name} and serve comida {self.cuisine_type}.
        "Esse restaurante está servindo {self.number_served} consumidores desde que está aberto."""

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        """
           2# - ao abrir o restaurante, open deveria ser true e  number_served deveria ser 0 (0 clientes)            
        """
        if not self.open:
            self.open = True
            self.number_served = self.ZERO_CLIENTS_SERVED
            return f'{self.restaurant_name} agora está aberto!'
        else:
            return f'{self.restaurant_name} já está aberto!'

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = self.ZERO_CLIENTS_SERVED
            return f'{self.restaurant_name} agora está fechado!'
        else:
            return f'{self.restaurant_name} já está fechado!'

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        """
        #3 - Para manter o padrao, alterei a string para já esta fechado, igual ao metodo close restaurant
        """
        if self.open:
            self.number_served = total_customers
        else:
            return f'{self.restaurant_name} já está fechado!'

    def increment_number_served(
        self, more_customers
    ):  # nao deveria ter um decrement number served?
        """#4 - O sistema nao estava incrementando a quantidade atual, somente reconfigurando o mesmo (seria uma
                copia de set_number.
        #5 Para manter o padrao, alterei a string para já esta fechado, igual ao metodo close
        restaurant
        """

        """Aumenta número total de clientes atendidos por este restaurante."""
        if self.open:
            self.number_served = self.number_served + more_customers
        else:
            return f'{self.restaurant_name} já está fechado!'
