#Написать SQL запрос, который выведет:
# все образцы и испытания по ним (поля для вывода ORDNO,
# USRNAME,TESTCODE,TESTNAME)
SELECT ORDERS.ORDNO, ORDERS.USRNAME, ORDTASK.TESTCODE, ORDTASK.TESTNAME
FROM ORDERS
LEFT JOIN ORDTASK ON ORDERS.ORDNO = ORDTASK.ORDNO;

#все образцы, на которые назначено испытание с кодом (TESTCODE) равным 123 (поле
# для вывода ORDNO)
SELECT ORDNO
FROM ORDTASK
WHERE TESTCODE == 123;

#всех пользователей, которые зарегистрировали образцы, на которые назначено
# испытание с названием начинающимся с ''Измерения р';
# (поле для вывода USRNAME).
SELECT ORDERS.USRNAME
FROM ORDERS
JOIN ORDTASK ON ORDERS.ORDNO = ORDTASK.ORDNO
WHERE ORDTASK.TESTNAME LIKE "Измерения р%";

#Напишите часть программы (на любом известном Вам ЯП) отвечающую за сортировку
# одномерного массив целых чисел по возрастанию не используя специальные функции
# сортировки. Объявление, ввод и вывод массива можно опустить.
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
