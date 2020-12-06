class system:
    names = ["ahmad haytam", "mert göksel", "emine gülen", "alex hafner"]
    courses = [219, 260, 291, 155, 203]

    def __init__(self):
        self.assignments = {}
        self.grades = {}
        self.averages = {}
        self.letternotes = {}
        self.name = system.namecheck(self)
        if self.name != 0:
            self.courses = system.course_select(self)
            if self.courses == 0:
                return
            self.assignments[self.name] = self.courses
            system.take_exams(self)
            system.lettergrade(self)
        else:
            pass

    def namecheck(self):
        flag = 1
        while True:
            name_entered = str(input("Please enter your name: ")).lower()
            if flag == 4:
                print("Please try again later...")
                return 0
            if name_entered in system.names:
                print(f"Welcome {name_entered.capitalize()}!"
                      f"\n")
                return name_entered
            else:
                print(f"Wrong entry! {3 - flag} Tries left: ")
                flag += 1

    def course_select(self):
        print("Please select min 3 out of these 5 courses:\n"
              "The selection should be written as ex. '219 260 203'\n"
              f"1-) Differential Equations {system.courses[0]}\n"
              f"2-) Basic Linear Algebra {system.courses[1]}\n"
              f"3-) Statistical Computing I {system.courses[2]}\n"
              f"4-) Basic Statistical Methods {system.courses[3]}\n"
              f"5-) Probability I {system.courses[4]}\n")

        user_input = str(input("Entries: "))
        user_input_list = user_input.split()
        if len(user_input_list) < 3:
            print("You have failed in class...")
            return 0

        for i in range(len(user_input_list)):
            if int(user_input_list[i]) not in system.courses:
                user_input_list[i] = str(input(f"{user_input_list[i]} is not a valid course, Please reenter your revised code (single): "))

        return user_input_list

    def take_exams(self):
        a = 0
        b = []
        for i in range(len(self.courses)):
            b.append(0)
        while len(self.grades) < len(self.courses):
            print(f"You have currently {len(self.courses) - a} lessons to take exams from.\n"
                  f"Please select one of them to enter the grades:\n")
            for i in range(len(self.courses)):
                if b[i] == 0:
                    print(f"-) {self.courses[i]}")

            selection = int(input("Selection: "))
            b[self.courses.index(str(selection))] = 1
            self.grades[selection] = [str(input("Enter your midterm grade: ")),
                                      str(input("Enter your final grade: ")),
                                      str(input("Enter your project grade: "))]
            self.averages[selection] = (int(self.grades[selection][0]) * 3 / 10) + (int(self.grades[selection][1]) / 2) + (int(self.grades[selection][2]) * 2 / 10)
            a += 1

    def lettergrade(self):
        for i in self.averages:
            if self.averages[i] >= 90:
                self.letternotes[i] = "AA"
            elif self.averages[i] >= 70:
                self.letternotes[i] = "BB"
            elif self.averages[i] >= 50:
                self.letternotes[i] = "CC"
            elif self.averages[i] >= 30:
                self.letternotes[i] = "DD"
            else:
                self.letternotes[i] = "FF"
        for i in self.letternotes:
            if self.letternotes[i] == "FF":
                print(f"You have failed from class {i} with grade {self.averages[i]}")


x = system()
