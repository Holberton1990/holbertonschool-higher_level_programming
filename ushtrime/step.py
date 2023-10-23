class Base:
    def __init__(self, id):
        self.id = id

class Rectangle(Base):
    def __init__(self, id, width, height, x, y):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Gjeresia duhet të jetë pozitive.")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Lartësia duhet të jetë pozitive.")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("Pozicioni x duhet të jetë zero ose pozitiv.")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("Pozicioni y duhet të jetë zero ose pozitiv.")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return "[Rectangle] instance"

class Rectangle(Base):
    def update(self, *args):

class Rectangle(Base):
    def update(self, *args):
    aatr_names = ["id", "width", "height", "x", "y"]
    for attr, value in zip(attr_names, args):
        setattr(self, attr, value)      
class Rectangle(Base):
    # ...
    
    def update(self, *args, **kwargs):
        attr_names = ["id", "width", "height", "x", "y"]
        for attr, value in zip(attr_names, args):
            setattr(self, attr, value)
        for key, value in kwargs.items():
            setattr(self, key, value)

class Square(Rectangle):
    def __init__(self, id, size, x, y):
        super().__init__(id, size, size, x, y):

    @property
    def size(self):
        return self.__width
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
class Square(Rectangle):
    
    def update(self, *args, **kwargs):
        attr_names = ["id", "size", "x", "y"]
        for attr, value in zip(aatr_names, args):
            setattr(self, attr, value)
        for key, value in kwargs.items():
            setattr(self, key, value)

class Rectangle(Base):
    def to_dictionary(self):
        return {
            "id": self.id,
            "height": self.height,
            "width": self.width,
            "x": self.x,
            "y": self.y
        }
class Square(Rectangle):
    def to_dictionary(self):
        return {
        "id": self.id,
        "size": self.size,
        "x": self.x,
        "y": self.y   
        }

class Base:
    def savetofile(cls, listobjs):
        with open("objects.json", "w") as file:
            json.dump([obj.to_dictionary for object in listobjs], file)

class Base():
    def fromjsonstring(jsonstring):
        data = json.loads(jsonstring)
        objects = [(cls.create(obj) for obj in data]
        return objects

class Base:
    def create(cls, dictionary):
        if cls is Base:
            cls_name = dictionary["name"]
            if cls_name == "Rectangle":
                cls = Rectangle
            elif cls_name = "Square"
                 cls = Square
        instance = cls.__new__(cls)
        instance.update(**dictionary)
        return instance
class Base:
    def loadfromfile(cls):
        objects = []
        if os.path.exists("objects.json"):
            with open("objects.json", "r") as file:
                data = json.load(file)
                objects = [cls.create(obj) for obj in data]
        return objects