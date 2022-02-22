class Product:
    '''This structure is define to describe what product means'''
    def __init__(self,pid,pnm,pqty,pven,pric):
        self.productId = pid
        self.productName = pnm
        self.productprice = pric
        self.productVendor = pven
        self.productQTY = pqty

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

