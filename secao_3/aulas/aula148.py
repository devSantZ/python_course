# Exemplos práticos do uso de dender methods


class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x, self.y})'
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other
            
    
if __name__ == '__main__':
    p1 = Ponto(2, 42)
    p2 = Ponto(224, 95)
    
    p3 = p1 + p2
    print(p3)
    
    print('p1 é maior que p2?', p1 > p2)
    print('p1 é maior que p2?', p1 < p2)

