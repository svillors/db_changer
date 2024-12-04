from random import choice
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from datacenter.models import Mark, Chastisement, Lesson, Commendation, Schoolkid


def get_schoolkid(name):
    kids = Schoolkid.objects.filter(full_name__contains=name)
    if len(kids) == 1:
        return kids.first()
    elif len(kids) > 1:
        print('С этими данными найдено несколько срзу учеников.')
        return
    else:
        print('Учника с этими данными не существует.')
        return


def get_random_lesson(subject, year_of_study, group_letter):
    lessons = Lesson.objects.filter(subject__title__contains=subject,
                                    year_of_study=year_of_study,
                                    group_letter=group_letter)
    if lessons:
        return choice(lessons)
    print("По этим данным ничего не найдено.")
    return


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid__full_name__contains=schoolkid.full_name).delete()


def create_commendation(schoolkid, lesson):
    compliments = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
    ]
    Commendation.objects.create(text=choice(compliments),
                                created=lesson.date,
                                schoolkid=schoolkid,
                                teacher=lesson.teacher,
                                subject=lesson.subject)


if __name__ == "__main__":
    schoolkid = get_schoolkid(input("Введите ФИО ученика: "))
    if schoolkid:
        print("Введите предмет, класс, литеру класса через пробел.")
        try:
            *subject, year_of_study, group_letter = input("Ввод: ").split()
            lesson = get_random_lesson(' '.join(subject),
                                       int(year_of_study),
                                       group_letter)
            if lesson:
                fix_marks(schoolkid)
                remove_chastisements(schoolkid)
                create_commendation(schoolkid, lesson)
        except ValueError:
            print("Данные не были введены или введены неправильно.")
