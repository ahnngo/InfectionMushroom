// Промоделировать процесс распространения инфекции лишая по участку кожи размером 21х21 клеток

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
#define INFECTED 6
#define IMMUNE 4
#define SIZE 23


class cell // Клетка (базовый класс)
{
public:
	virtual int status()=0; // Состояние клетки
	void set_location(int a, int b) { i=a; j=b; } // Функция, позволяющая занести координаты клетки
	int get_i() { return i; }
	int get_j() { return j; }
	virtual void print () const { cout<<". "; }
protected:
	int i, j;
};

class healthy: public cell // Производный класс "здоровая клетка" (базовый - клетка)
{
public:
	int status() { return 1; }
	int if_change() { return rand()%2;  } // Функция, определяющая вероятность заражения здоровой клетки
	void print () const { cout<<"- "; }
};

class immune: public cell // Производный класс для клетки, обладающей иммунитетом (базовый - клетка)
{
public:
	int status() { return 2; }
	immune(immune* n=0, int k=IMMUNE): count(k), next(n) {}; // Конструктор
	void set_next (immune* n) { next=n; }
	immune* get_next () { return next; }
	int change () { return (--count==0); } // Функция, определяющая, выздоровела ли клетка
	void print () const { cout<<"# "; }
	cell* make_healthy(cell* c); // Функция превращения иммунной клетки в здоровую
private:
	int count; // Счётчик времени
	immune* next;
};

cell* immune::make_healthy(cell* c) // Функция превращения иммунной клетки в здоровую
{
	healthy* h=new healthy;
	h->set_location(c->get_i(), c->get_j()); // Заносятся её координаты
	return h;
}

class infected: public immune // Производный класс для заражённой клетки (базовый - иммунная клетка)
{
public:
	int status() { return 3; }
	infected(): immune(0, INFECTED) {}; // Конструктор
	cell* make_imm(cell* c); // Функция превращения больной клетки в иммунную
	cell* infect(cell* c); // Функция заражения
	void print () const { cout<<"* "; }
};

cell* infected::make_imm(cell* c) // Функция превращения больной клетки в иммунную
{
	immune* i=new immune; // Создаётся новая иммунная клетка
	i->set_location(c->get_i(), c->get_j()); // Заносятся её координаты
	return i;
}

cell* infected::infect(cell* c) // Функция заражения
{
	if (c->status()==1 && ((healthy*)c)->if_change()) // Заражаем клетку, если она здоровая и имеет вероятность заражения 1
	{
		infected* i=new infected; // Создаётся новая заражённая клетка
		i->set_location(c->get_i(), c->get_j()); // Заносятся её координаты
		return i;
	}
	return c;
}

class list // Список клеток (очередь)
{
public:
	friend class skin;
	list() { tail=0; }
	void print() const;
private:
	immune* tail;
	immune* add(immune* c); // Функция добавления клетки в список
	immune* remove(); // Функция, убирающая из списка клетку
	immune* add_list(immune* t); // Функция, добавляющая к списку новый список клеток
};

immune* list::add_list(immune* t) // Функция, добавляющая к списку новый список клеток
{
	if (t!=0) // Если 2ой список не пуст, добавляем его
	{
		if (tail!=0) // Если 1ый список не пуст, то связываем два списка между собой
		{
			immune* head=tail->get_next(); // Голова 1го списка
			tail->set_next(t->get_next()); // Хвост 1го списка ссылается на голову 2го
			t->set_next(head); // Хвост 2го списка ссылается на голову 1го
		}
		tail=t; // Назначаем хвост
	}
	return tail;
}

void list::print() const
{
	if (tail!=0)
	{
		immune* temp=tail->get_next();
		do
		{
			temp->print();
			temp=temp->get_next();
		} 
		while (temp!=tail->get_next());
	}
}

immune* list::remove() // Функция, убирающая из списка клетку
{
	if (tail->get_next()==tail) // Если клетка в списке одна, нужно обнулить значение хвоста
	{
		immune* t=tail;
		tail=0;
		return t;
	}
	immune* head=tail->get_next(); // Запоминаем голову, которую нужно вернуть в качестве результата
	immune* temp=tail->get_next()->get_next(); // Вторая после головы клетка
	tail->set_next(temp); // Хвост связывается с новой головой
	return head;
}

immune* list::add(immune* c) // Функция добавления клетки в список
{
	if (tail!=0) // Если список не пуст, добавляем очередную клетку 
	{
		immune* head=tail->get_next(); // Голова списка
		tail->set_next(c); // Назначаем хвосту ссылку на следующую клетку
		c->set_next(head); // Добавленная клетка ссылается на голову списка
	}
	else // Иначе в списке будет одна клетка, ссылающаяся сама на себя
		c->set_next(c); 
	tail=c;
	return tail;
}

class skin // Участок кожи
{
public:
	skin(); // Конструктор
	~skin(); // Деструктор
	void make_barrier(); // Функция для создания барьера вокруг участка кожи
	void print() const;
	void create(); // Функция выделения памяти
	void init(); // Инициализация участка кожи
	void exchange(cell* c, int i, int j) { delete s[i][j]; s[i][j]=c; } // Функция, меняющая клетку при изменении её состояния
	void step_inf(list& l); // Заражение здоровых клеток
	void change_inf_list(list& l); // Изменение больных клеток
	void change_imm_list(); // Изменение иммунных клеток
	void step(); // Шаг процесса
	void process(); // Весь процесс распространения 
private:
	list inf; // Список заражённых клеток
	list imm; // Список иммунных клеток
	cell*** s; // Указатель на двумерный массив указателей
};

void skin::process() // Весь процесс распространения 
{
	int k=1; // Счётчик количества шагов
	char b;
	do
	{	
		cout<<k<<")"<<endl;
		print();
		cout<<"Continue? y/n"<<endl;
		cin>>b;
		step();
		k++;
	}
	while (b!='n');
}

void skin::step() // Шаг всего процесса
{
	list new_imm; // Список для клеток, которые станут иммунными на данном этапе
	list new_inf; // Список для клеток, которые заразятся на данном этапе
	change_inf_list(new_imm); // Изменение заражённых клеток
	step_inf(new_inf); // Заражение соседних клеток
	inf.tail=inf.add_list(new_inf.tail); // Присоединение списка новых заражённых клеток к основному списку заражённых
	change_imm_list(); // Изменение иммунных клеток	
	imm.tail=imm.add_list(new_imm.tail); // Присоединение списка новых иммунных к основному списку иммунных
}

void skin::change_imm_list() // Изменение иммунных клеток
{
	immune* im, *temp; 
	if (imm.tail==0) return; // Если клеток в списке нет, то и изменять нечего
	temp=imm.tail->get_next(); // Голова списка иммунных клеток
	int b;
	do // У каждой клетки уменьшаем счётчик времени и проверяем, не пора ли ей стать здоровой
	{
		if (b=temp->change()) // Убираем из списка клетку, если её время истекло
		{
			im=imm.remove(); 
			healthy* h=(healthy*)im->make_healthy(im); // Создаём новую здоровую с теми же координатами
			exchange(h, h->get_i(), h->get_j()); // Заменяем клетку на поле
		}
		if (imm.tail==0) return; // Если убрали последнюю клетку, выходим из функции
		temp=temp->get_next(); // Переходим к следующей
	}
	while (b || temp!=imm.tail->get_next()); 
}

void skin::change_inf_list(list& l) // Изменение больных клеток
{
	infected* temp;
	if (inf.tail==0) return; // Если клеток в списке нет, то и изменять нечего
	temp=(infected*)inf.tail->get_next(); // Голова списка больных клеток
	int b;
	do // У каждой клетки уменьшаем счётчик времени и проверяем, не пора ли ей перейти в иммунное состояние
	{
		if (b=temp->change())
		{ // Если у клетки истекло время, нужно её поместить в список иммунных клеток и назначить новую голову
			infected* i=(infected*)inf.remove(); // Убираем из списка
			immune* im=(immune*)i->make_imm(i); // Создаём иммунную клетку с теми же координатами
			l.tail=l.add(im); // Добавляем иммунную клетку в список
			exchange(im, im->get_i(), im->get_j()); // Заменяем клетку на поле
		}
		if (inf.tail==0) return; // Если убрали последнюю клетку, выходим из функции
		temp=(infected*)temp->get_next(); // Переходим к следующей
	}
	while (b || temp!=inf.tail->get_next());
}

void skin::step_inf(list& l) // Шаг процесса распространения инфекции
{
	if (inf.tail==0) return; // Если на поле нет заражённых клеток, выходим из функции
	infected* temp=(infected*)inf.tail->get_next(); // Голова списка заражённых клеток
	do // Каждая клетка из списка пытается заразить соседей
	{
		int i=temp->get_i(); // Координаты заражающей клетки 
		int j=temp->get_j();
		// Заражение соседей:
		cell* c;
		for (int a=i-1; a<=i+1; a++)
			for (int b=j-1; b<=j+1; b++)
			{
				if (a!=i || b!=j)
				{ // Клетка пытается заразить только тех соседей, которые не выходят за пределы поля
					c=temp->infect(s[a][b]);
					if (s[a][b]!=c) // Если клетка заразилась:
					{
						l.tail=l.add((infected*)c); // Добавление заражённой клетки в список заражённых
						exchange(c, c->get_i(), c->get_j()); // Изменение клетки на поле
					}
				}
			}
		temp=(infected*)temp->get_next(); 
	} 
	while (temp!=(infected*)inf.tail->get_next());
}

skin::skin() // Конструктор
{
	create(); // Выделение памяти
	make_barrier(); // Создание барьера вокруг участка кожи
	init(); // Инициализация участка кожи
}

skin::~skin() // Деструктор
{
	for (int i=0; i<SIZE; i++)
	{
		for (int j=0; j<SIZE; j++)
			delete s[i][j];
		delete [] s[i];
	}
	delete s;
}

void skin::print() const
{
	for (int i=1; i<SIZE-1; i++)
	{
		for (int j=1; j<SIZE-1; j++)
			s[i][j]->print();
		cout<<endl;
	}
	cout<<endl;
}

void skin::init() // Инициализация участка кожи
{
	
	int ind=SIZE/2; // Индекс центральной заражённой клетки
	for (int i=1; i<SIZE-1; i++)
		for (int j=1; j<SIZE-1; j++)
		{
			s[i][j]=new healthy; // Создаём новую здоровую клетку
			s[i][j]->set_location(i, j); // Заносим её координаты
		}
	infected* in=new infected; // Создаётся новая заражённая клетка
	in->set_location(ind, ind); // Заносятся её координаты
	exchange(in, ind, ind); // Центральная клетка становится заражённой
	inf.tail=inf.add((immune*)s[ind][ind]); // Центральная клетка заносится в список заражённых
}

void skin::create() // Функция выделения памяти
{	
	s=new cell** [SIZE];
	for (int i=0; i<SIZE; i++)
		s[i]=new cell*[SIZE];
}

void skin::make_barrier() // Функция для создания барьера вокруг участка кожи
{
	for (int j=0; j<SIZE; j++)
	{
		s[0][j]=new immune;
		s[0][j]->set_location(0, j);
		s[SIZE-1][j]=new immune;
		s[SIZE-1][j]->set_location(SIZE-1, j);
		s[j][0]=new immune;
		s[j][0]->set_location(j, 0);
		s[j][SIZE-1]=new immune;
		s[j][SIZE-1]->set_location(j, SIZE-1);
	}
}

int main()
{
	srand(time(0));
	skin s;
	s.process();
	system("pause");
}