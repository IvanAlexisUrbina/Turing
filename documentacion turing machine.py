class TuringMachine:
    """
    Clase que representa una Máquina de Turing para sumar dos números binarios.
    """

    def __init__(self, tape):
        """
        Inicializa la Máquina de Turing con una cinta de entrada y establece el estado inicial.

        Parámetros:
            tape (list): Una lista que representa la cinta de entrada, donde cada elemento es un carácter ('0', '1' o '_').
        """
        self.tape = tape
        self.head_position = 0
        self.state = 'q0'

    def transition(self):
        """
        Realiza transiciones de estado de la Máquina de Turing hasta alcanzar el estado final 'qf'.
        Imprime el resultado de la suma cuando la máquina alcanza el estado final.
        """
        while self.state != 'qf':
            if self.state == 'q0':
                if self.tape[self.head_position] == '0':
                    self.state = 'q0'
                    self.move_head('R')
                elif self.tape[self.head_position] == '1':
                    self.state = 'q0'
                    self.move_head('R')
                else:
                    self.state = 'q1'
                    self.move_head('L')

            elif self.state == 'q1':
                if self.tape[self.head_position] == '0':
                    self.state = 'q1'
                    self.move_head('L')
                elif self.tape[self.head_position] == '1':
                    self.state = 'q1'
                    self.move_head('L')
                else:
                    self.state = 'q2'
                    self.move_head('R')

            elif self.state == 'q2':
                if self.tape[self.head_position] == '0':
                    self.tape[self.head_position] = '_'
                    self.state = 'q3'
                    self.move_head('R')
                elif self.tape[self.head_position] == '1':
                    self.tape[self.head_position] = '_'
                    self.state = 'q4'
                    self.move_head('R')

            elif self.state == 'q3':
                if self.tape[self.head_position] == '0':
                    self.state = 'q3'
                    self.move_head('R')
                elif self.tape[self.head_position] == '1':
                    self.state = 'q3'
                    self.move_head('R')
                else:
                    self.state = 'q5'
                    self.move_head('L')

            elif self.state == 'q4':
                if self.tape[self.head_position] == '0':
                    self.state = 'q4'
                    self.move_head('R')
                elif self.tape[self.head_position] == '1':
                    self.state = 'q4'
                    self.move_head('R')
                else:
                    self.state = 'q5'
                    self.move_head('L')

            elif self.state == 'q5':
                self.state = 'qf'

        print("Suma completa:", ''.join(self.tape))

    def move_head(self, direction):
        """
        Mueve la cabeza de lectura/escritura de la Máquina de Turing hacia la izquierda o la derecha en la cinta.

        Parámetros:
            direction (str): La dirección en la que se moverá la cabeza ('R' para derecha, 'L' para izquierda).
        """
        if direction == 'R':
            self.head_position += 1
        elif direction == 'L':
            self.head_position -= 1


# Ejemplo de uso:
tape = list("1011_1101")  # Por ejemplo, 1011 + 1101
tm = TuringMachine(tape)
tm.transition()
