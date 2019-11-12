# 用于将.txt的文件导入django的数据库中
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
django.setup()


def main():
    from demo_app.models import Book
    with open('mainstorage.txt', encoding='UTF-8') as f:
        i = 0
        for line in f:
            print(line)
            title, author, booktype, introduction = line.split(',')
            Book.objects.get_or_create(id=i, title=title, author=author, booktype=booktype, introduction=introduction)
            i += 1


if __name__ == "__main__":
    main()
    print('Done!')
