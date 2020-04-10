import gkeepapi

print("excute in python3!")

#Login e var
keep = gkeepapi.Keep()
success = keep.login('fortestestest82@gmail.com', 'gabrielserra')




#tipo de fixado e msg
#note = keep.createNote('Todo', 'Eat breakfast')
#note = keep.createNote('Tarefa de matematica', 'fazer pagina 20 para o dia 03/03')
note = keep.createNote('Tarefa de portugues', 'Fazer pagina 20 para nenhum dia ')
note.pinned = True
note.color = gkeepapi.node.ColorValue.Blue
keep.sync()
