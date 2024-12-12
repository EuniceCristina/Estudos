from models import User, Receita
from config import start_db, session, destroy_db

start_db()

nomes='eunice'
user = User(nome=nomes)
session.add(user)
session.commit()



receita1 = Receita(nome='receita1',user_id=user.id)
receita2 = Receita(nome='miojo', user_id=user.id)
session.add_all([receita1,receita2])
session.commit()

print(user)

re = session.query(Receita).first()
print(re.nome)
print(re.id)
print(re.user_id)

destroy_db()
