import datetime

data = datetime.datetime.now()
Diasemana = ('segunda feira','terceira feira','quarta feira', 'quinta feira','sexta feira','sabado','domingo')

diasemana = datetime.date.weekday(data)

arquivo = open('teste.txt','w')
arquivo.write(str(data))
arquivo.close()
print(data.strftime('%d/%m/%Y'))
print(Diasemana[diasemana])

arquivo = open('teste.txt','r')
data = arquivo.read()
arquivo.close()

data = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S.%f")+ datetime.timedelta(days=1)
diasemana = datetime.date.weekday(data)

print(data.strftime('%d/%m/%Y'))
print(Diasemana[diasemana])
