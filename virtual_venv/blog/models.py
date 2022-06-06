from django.conf import settings
from django.db import models
from django.utils import timezone
from . import views


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Base():
    def get_database(name_exel_base: str, name_base: str): # name_base - название базы которую хотим назвать
        """Эта функция принимает название exel таблицы и название твое базы.
        И в результате создает файлы json и sql формата"""
        conn = sqlite3.connect(f"{name_base}.db") # создали файл пустой базы
        wb = pd.read_excel(name_exel_base)# читаем exel таблицу
        wb.to_sql(name="mytable", con=conn, if_exists="replace", index=True)# ковертирум в sql формат
        conn.commit()
        
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM mytable """)
        one_result = cursor.fetchall()

        subjects = dict()
        names = [description[0] for description in cursor.description]
        for i, value in enumerate(one_result):
            bas = dict()
            for j, item in enumerate(names):# создает словарь вида -> index: {id: x, some_name: name, ...}
                bas[item] = value[j]
            subjects[f"{i}"] = bas

        with open(f"{name_base}.json", "w") as write_file: # создаем файл json 
            json.dump(subjects, write_file)

    def sort_data(objects: str):
        con = sqlite3.connect(f"{name_base}.db")
        cur = con.cursor()
        objects_ = re.split(',', objects)
        x = dict()
        for i in range(1, len(objects_)):
                x[objects_[0]] = objects_[i]
        sort_list = []
        for i, value in enumerate(x):
            cursor.execute(f"""
                    SELECT *
                    FROM mytable
                    WHERE ({value}='{x[value]}') """)
            pur = cursor.fetchall()
            sort_list.append(pur)
        return sort_list