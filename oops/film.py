class Film:

    title:str

    rating:float

    run_time:str

    director:str

    genre:str


    def set_film(self,title,rating,run_time,director,genre):

        self.title=title

        self.rating=rating

        self.run_time=run_time

        self.director=director

        self.genre=genre

    def display(self):

        print(self.title,self.rating,self.run_time,self.director,self.genre)

set_film1=Film()

set_film2=Film()

set_film1.set_film("arm",9.5,"3 hrs","Jithin Lal"," Adventure,Comedy,Drama")

set_film2.set_film("KGF",9.8,"3 hrs","Prashanth Neel","Action,Crime,Drama")

set_film1.display()

set_film2.display()