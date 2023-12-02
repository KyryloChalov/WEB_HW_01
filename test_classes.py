from classes import Record, AddressBook

# from notes import Note, NotesBook
from constants import GREEN, RESET

from input_output import Console

# =============================================
#             test 1 (Classes)
# =============================================

if __name__ == "__main__":
    book = AddressBook()
    filename = "book_test_1.bin"

    Console.output(GREEN + "     створюємо новий контакт" + RESET)
    Console.output(book.add_record(Record("tom", "0995648525", birthday="18-11-1986")))

    Console.output(
        GREEN + "     створюємо новий контакт, у якого тільки день народження" + RESET
    )
    Console.output(book.add_record(Record("helen", birthday="14-11-1999")))

    Console.output(GREEN + "     змінюємо ім'я 'tom' на 'thomas'" + RESET)
    Console.output(book.change_name("tom", "thomas"))

    Console.output(GREEN + "     створюємо новий контакт, у якого є тільки ім'я" + RESET)
    Console.output(book.add_record(Record("jerry")))

    Console.output(GREEN + "     створюємо новий контакт" + RESET)
    Console.output(book.add_record(Record("garry", "0995647821", birthday="15-11-1975")))

    Console.output(GREEN + "     створюємо новій контакт в 3 дії" + RESET)
    name = "bill"
    phone = "0677977166"
    # b_day = "27-10-1968"
    # rec = Record(name, phone, b_day)
    rec = Record(name, phone)
    Console.output(book.add_record(rec))

    Console.output(GREEN + "     додаємо дату народження контакту" + RESET)
    Console.output(rec.add_birthday("16-11-2005"))

    Console.output(GREEN + "     намагаємось додати вже існуючий телефон" + RESET)
    result = rec.add_phone("0677977166")
    Console.output(result)

    Console.output(GREEN + "     додаємо другий телефон" + RESET)
    Console.output(rec.add_phone("0933903357"))

    Console.output(GREEN + "     намагаємося поміняти телефон на такий самий" + RESET)
    Console.output(rec.edit_phone("0677977166", "+380677977166"))

    Console.output(GREEN + "     міняємо номер телефона на інший" + RESET)
    Console.output(rec.edit_phone("0677977166", "0997058845"))

    Console.output(GREEN + "     намагаємося поміняти неіснуючий номер телефона" + RESET)
    Console.output(rec.edit_phone("0671234567", "1234567809"))

    Console.output(GREEN + "     намагаємося видалити неіснуючий номер телефона" + RESET)
    Console.output(rec.remove_phone("0677977166"))

    Console.output(GREEN + "     видаляємо один з номерів телефону" + RESET)
    Console.output(rec.remove_phone("0997058845"))

    Console.output(GREEN + "     додаємо ще один номер" + RESET)
    Console.output(rec.add_phone("0677977166"))

    Console.output(GREEN + "     шукаємо номер" + RESET)
    Console.output(rec.find_phone("0677977166"))

    Console.output(GREEN + "     шукаємо номер" + RESET)
    Console.output(rec.find_phone("0933903357"))

    Console.output(GREEN + "     шукаємо неіснуючий номер" + RESET)
    Console.output(rec.find_phone("0677977444"))

    Console.output(GREEN + "     додаємо новий контакт" + RESET)
    Console.output(book.add_record(Record("ivan", "0671234567")))

    Console.output(GREEN + "     додаємо новий контакт" + RESET)
    Console.output(book.add_record(Record("mary", "0671234555", "13-12-2000")))

    Console.output(GREEN + "     додаємо новий контакт" + RESET)
    Console.output(book.add_record(Record("jill", "0672223344", birthday="12-11-2012")))

    Console.output(GREEN + "     шукаємо контакт" + RESET)
    Console.output(book.find_name("bill"))

    Console.output(GREEN + "     шукаємо неіснуючий контакт" + RESET)
    Console.output(book.find_name("john"))

    Console.output(GREEN + "     перелік контактів до видалень контактів" + RESET)
    Console.output("======= before delete =========")
    Console.output(book)

    Console.output(GREEN + "     зберігаємо контакти" + RESET)
    Console.output(book.write_contacts_to_file(filename))

    Console.output(GREEN + "     видаляємо 5 контактів" + RESET)
    Console.output(book.delete_record("mary"))
    Console.output(book.delete_record("tom"))
    Console.output(book.delete_record("ivan"))
    Console.output(book.delete_record("jill"))
    Console.output(book.delete_record("billy"))

    Console.output(GREEN + "     перелік контактів після видалень" + RESET)
    Console.output("======== after delete ========")
    Console.output(book)

    Console.output(GREEN + "     відновлюємо контакти з файлу" + RESET)
    book = book.read_contacts_from_file(filename)

    Console.output(
        GREEN
        + "     перелік контактів після відновлення (такий самий, як до видалення)"
        + RESET
    )
    Console.output(
        GREEN
        + "     додано сортування контактів за алфавітом - відбувається під час читання файлу"
        + RESET
    )
    Console.output("======== after restoring from a file ========")

    Console.output(GREEN + "     перелік контактів" + RESET)
    Console.output(book)

    Console.output("======== Address fields ========")
    Console.output(GREEN + "     додаємо адресу" + RESET)
    Console.output(rec.add_address("Lviv"))
    Console.output(rec.remove_address())
    Console.output(rec.add_address("10001, New York, Manhattan 123b"))
    Console.output(GREEN + "     перелік контактів" + RESET)
    Console.output(book)

    Console.output("======== Email fields ========")
    Console.output(GREEN + "     додаємо email" + RESET)
    # Console.output(rec.add_email("XXXXXXXXXXXXXX"))
    Console.output(rec.add_email("asd@mail.com"))
    Console.output(rec.remove_email("asdddd@mail.com"))
    Console.output(rec.edit_email("asd@mail.com", "new_mail@mail.com"))
    Console.output(rec.add_email("second@mail.com"))

    Console.output(GREEN + "     змінюємо ім'я 'bill' на 'billy'" + RESET)
    Console.output(book.change_name("bill", "billy"))

    Console.output(GREEN + "     перелік контактів" + RESET)
    Console.output(book)
