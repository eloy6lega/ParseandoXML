from bs4 import BeautifulSoup

print('Prueba en Python')

with open('Clientes.xml','r') as f:
    data=f.read()
#print(data)

Bs_data = BeautifulSoup(data,'xml')
#print(Bs_data)
telefonos = Bs_data.find_all('telefono')
print(telefonos)

b_id_cl = Bs_data.find('cliente', {'ID':'C001'})
#print(b_id_cl)

for tag in Bs_data.find_all('cliente', {'ID':'C001'}):
    tag['ciudad'] = "MADRID"

print(Bs_data.prettify())
