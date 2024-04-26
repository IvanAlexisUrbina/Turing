class TuringMachine:
    def __init__(self, tape):
        self.tape = tape
        self.head_position = 0
        self.state = 'q0'

    def transition(self):
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
        if direction == 'R':
            self.head_position += 1
        elif direction == 'L':
            self.head_position -= 1


# Entrada: dos números binarios separados por un '_'
tape = list("1011_1101")  # Por ejemplo, 1011 + 1101

tm = TuringMachine(tape)
tm.transition()
