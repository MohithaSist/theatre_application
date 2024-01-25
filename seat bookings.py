class  theatre_details:
    theatre_details_list=[]
    def __init__(self,theatre_id,theatre_name,location,ratings,movies:list,show_times:dict):
        self.theatre_id=theatre_id
        self.theatre_name=theatre_name
        self.location=location
        self.ratings=ratings
        self.movies=movies
        self.show_times=show_times

class Movie_details:
    Movie_details_list=[]
    def __init__(self,movie_id,movie_name,duration,ratings):
        self.movie_id=movie_id
        self.movie_name=movie_name
        self.duration=duration
        self.ratings=ratings

class seat_details:
    seat_list=[]
    def __init__(self,movie_name,timings):
        self.movie_name=movie_name
        self.timings=timings 
        self.seats=[["A1", "A2", "A3", "A4", "A5"], 
                      ["B1", "B2", "B3", "B4", "B5"], 
                      ["C1", "C2", "C3", "C4", "C5"],
                      ["D1", "D2", "D3", "D4", "D5"]]
        



class Movie_details_functionality:
    def display_movies(self):
        print()
        for movies in Movie_details.Movie_details_list:
            print(movies.movie_id , '\t' , movies.movie_name, '\t' ,movies.duration ,'\t' ,movies.ratings)
        print()
    def select_movie(self):
        choice=int(input("Enter your movie choice : "))
        for movies in Movie_details.Movie_details_list:
            if movies.movie_id==choice:
                #print(movies.movie_name,'9999')
                return movies.movie_name 

class theatre_details_functinality(Movie_details_functionality):
    print()
    def display_theatres(self,sel_mo):
        for theatres in theatre_details.theatre_details_list:
            if (sel_mo in theatres.movies):
                print(theatres.theatre_id ,'\t' , theatres.theatre_name ,'\t', theatres.location, '\t' ,theatres.ratings)
        print()
    def select_theatre(self):
        theatre_choice=int(input("Enter theatre id : "))
        for theatres in theatre_details.theatre_details_list:
            if theatres.theatre_id==theatre_choice:
                return theatres.theatre_name 
    def display_showtime(self,selected_theatre_name):
        print('-----------------------------------------------')
        for det in theatre_details.theatre_details_list:
            #print(selected_theatre_name)
            if det.theatre_name==selected_theatre_name :
                print()
                [print(key,value) for (key,value) in det.show_times.items()]
                print()
        return[det.show_times for det in theatre_details.theatre_details_list if det.theatre_name==selected_theatre_name ]

    def select_showtime(self,selected_theatre_name):
        show_time = self.display_showtime(selected_theatre_name)
        print()
        show_id=int(input("Enter your show id : "))
        if show_id>0 and show_id<6:
            #print(show_time,'time')
            return show_time[0][show_id]
    
class seat_functionality:
    def display_seats(self,selected_movie_name,selected_show_time):
        create_seats=[seats.seats for seats in seat_details.seat_list if selected_movie_name==seats.movie_name and selected_show_time==seats.timings]
        if create_seats==[]:
            new_seats=seat_details(selected_movie_name,selected_show_time)
            seat_details.seat_list.append(new_seats)
            self.display_seats(selected_movie_name,selected_show_time)
        else:
            for seats in seat_details.seat_list:
                if seats.movie_name==selected_movie_name and seats.timings==selected_show_time:
                    print()
                    for seat in seats.seats :
                        print(*seat)
    def select_seats(self,selected_movie_name,selected_show_time):
        selected_seats=[]
        self.display_seats(selected_movie_name,selected_show_time)
        required_seats=[seat.seats for seat in seat_details.seat_list]
        requested_seats=input("Enter your seats(EX.A1 A2) : ").upper().split()
        for i in required_seats[0]:
            for j in i:
                if j in requested_seats:
                    selected_seats.append(j)
        if len(selected_seats)==len(requested_seats):
            for i in required_seats[0]:
                for j in range(len(i)):
                    if i[j] in requested_seats:
                        i[j]=0
        return selected_seats





class Movie_booking_system (theatre_details_functinality,seat_functionality):
    def __init__(self):
        self.mail_id='mohithamathan@gmail.com'
    def run(self):
        a=True
        while a:       
            print()
            print('1.Book tikets')
            print("2.Delete booking history")
            print('3.delete booking history')
            print('4.logout')
            print()
            opt=int(input("Enter your choice : "))
            if opt ==1:
                self.display_movies()
                selected_movie_name=self.select_movie()
                self.display_theatres(selected_movie_name)
                selected_theatre_name=self.select_theatre()
                selected_show_time=self.select_showtime(selected_theatre_name)
                self.select_seats(selected_movie_name,selected_show_time)
            elif opt==4:
                a=False


if __name__=='__main__':
    theatre1=theatre_details(1,'sathya','Erode',3.5,['joe','jigardhanda','adiyea'],{1:'6.00AM',2:'9.00AM',3:'12.00PM',4:'3.00PM',5:'6.00PM'})
    theatre2=theatre_details(2,'SRT','chennai',4,['joe','jigardhanda'],{1:'6.00AM',2:'9.00AM',3:'12.00PM',4:'6.00PM',5:'9.00PM'})
    theatre3=theatre_details(3,'Maruti','coimbatore',3,['joe'],{1:'9.00AM',2:'12.00PM',3:'4.00PM',4:'7.00PM',5:'10.00PM'})
    theatre_details.theatre_details_list.append(theatre1)
    theatre_details.theatre_details_list.append(theatre2)
    theatre_details.theatre_details_list.append(theatre3)

    movie1=Movie_details(1,'joe','2 hr 30 mins',4.5)
    movie2=Movie_details(2,'jigardhanda','2 hr 45 mins',4.9)
    movie3=Movie_details(3,'adiyea','2 hr 20 mins',3.1)
    Movie_details.Movie_details_list.append(movie1)
    Movie_details.Movie_details_list.append(movie2)
    Movie_details.Movie_details_list.append(movie3)

    m=Movie_booking_system()
    m.run()