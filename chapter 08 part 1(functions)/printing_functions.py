
# def printing_model (name : str) -> None:
    
#     sentance = f"Hi {name.title()}, Welcome in our priting model "

#     print(sentance)

from pizza import make_pizza

i = 0
def printing_model ():
    # clear()
    global i
    i += 1
    print(f"\nThis is the printing model : {i}")
    make_pizza(16, 'pepperoni')
    make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

printing_model()