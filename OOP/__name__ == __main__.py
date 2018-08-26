from OOP import test1

test1.zohan.run()

class Car:

    """MyClass"""

    def __init__(self):
        self.color = "blue"

    def run(self):
        print("Еду")

if __name__ == "__main__":  # Указуем питону что хотим запустить код, если он выполняется как автономный фаил
    print("god")
    honda = Car()
    print(honda.run())