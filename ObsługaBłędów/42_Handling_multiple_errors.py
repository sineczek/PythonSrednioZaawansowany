clients = {
    'INFO': 0.5,
    'DATA': 0.2,
    'SOFT': 0.2,
    'INTER': 0.1,
    'OMEGA': 0.0
}

myClient = input('Enter Client name : ')
totalCost = 7200
try:
    ratio = float(input('Enter new ratio: '))
    print('The default % ratio for {} is {}, a new ratio is {}'.format(myClient, clients[myClient], ratio))
    print('The cost for {} is {}'.format(myClient, ratio * totalCost))
    print('The new ratio in comparison to old ratio is {}'.format(clients[myClient] / ratio))
except KeyError as e:
    print('Client {} is not on the list.\nDetails:\n{}'.format(myClient, [c for c in clients.keys()], e))
except (ValueError, ZeroDivisionError) as e:
    print(
        'There is a problem wint entered value for ratio - it must be a number greater than 0.\nDetails:\n{}'.format(e))
# bloki można łączyć
# except ZeroDivisionError as e:
#    print('The new ratio cannot be 0.\nDetails:\n{}'.format(e))

except Exception as e:
    print('Sorry we have an error ...\nDetils:\n{}'.format(e))
