class Runner:
    def __init__(self, name, pr, grade, gender):
        self.name = name
        self.pr = pr
        self.grade = grade
        self.gender = gender
        self.pace = self.calc_pace()
        self.pr_seconds = self.calc_seconds()

    def __str__(self):
        return f"{self.name.title()}, PR of {self.pr}, average pace of {self.pace}min/mi"

    def calc_seconds(self):
        return int(self.pr[:2])*60 + int(self.pr[3:])

    def calc_pace(self):
        seconds = int(self.pr[:2])*60 + int(self.pr[3:])
        pace_total_seconds = round(seconds/3.1)
        pace_seconds = pace_total_seconds%60
        pace_seconds = f"{pace_seconds:0>{2}}"
        pace_minutes = int(pace_total_seconds/60)
        return f"{pace_minutes}:{pace_seconds}"

    #all getters and setters for propertys
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("No name passed in")
        self._name = name

    @property
    def pr(self):
        return self._pr

    @pr.setter
    def pr(self, pr):
        if pr[:2].isnumeric() and pr[2]==":" and pr[3:].isnumeric():
            self._pr = pr
        else:
            raise ValueError("Invalid pr")

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if not grade.isdigit():
            raise ValueError("grade is not a number")
        if grade not in ["9","10","11","12"]:
            raise ValueError("grade not in range")
        self._grade = grade

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if gender not in ["m", "f"]:
            raise ValueError("Invalid Gender")
        self._gender = gender

    @property
    def pace(self):
        return self._pace

    @pace.setter
    def pace(self, pace):
        if pace[:1].isnumeric() and pace[1]==":" and pace[2:].isnumeric():
            self._pace = pace
        else:
            raise ValueError("Invalid pace")

    @property
    def pr_seconds(self):
        return self._pr_seconds

    @pr_seconds.setter
    def pr_seconds(self, pr_seconds):
        if not isinstance(pr_seconds, int):
            raise ValueError("pr_seconds must be an int")
        self._pr_seconds = pr_seconds