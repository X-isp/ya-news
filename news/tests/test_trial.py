# # news/tests/test_trial.py
# from django.test import TestCase


# class Test(TestCase):

#     def test_example_success(self):
#         self.assertTrue(True)  # Этот тест всегда будет проходить успешно.


# class YetAnotherTest(TestCase):

#     def test_example_fails(self):
#         self.assertTrue(False)  # Этот тест всегда будет проваливаться.

# import unittest
# # news/tests/test_trial.py
# from django.test import TestCase

# # Импортируем модель, чтобы работать с ней в тестах.
# from news.models import News


# # Создаём тестовый класс с произвольным названием, наследуем его от TestCase.
# class TestNews(TestCase):

#     # Все нужные переменные сохраняем в атрибуты класса.
#     TITLE = 'Заголовок новости'
#     TEXT = 'Тестовый текст'
    
#     @classmethod
#     @unittest.skip("Тестовый пример")
#     def setUpTestData(cls):
#         cls.news = News.objects.create(
#             # При создании объекта обращаемся к константам класса через cls.
#             title=cls.TITLE,
#             text=cls.TEXT,
#         )

#     @unittest.skip("Тестовый пример")
#     def test_successful_creation(self):
#         news_count = News.objects.count()
#         self.assertEqual(news_count, 1)
    
#     @unittest.skip("Тестовый пример")
#     def test_title(self):
#         # Чтобы проверить равенство с константой -
#         # обращаемся к ней через self, а не через cls:
#         self.assertEqual(self.news.title, self.TITLE)


# if __name__ == '__main__':
#     unittest.main()