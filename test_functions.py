from constants import GREEN, RESET
from main import (
    book,
    help_page,
    add_contact,
    change_phone,
    change_name,
    del_phone,
    add_birthday,
    add_phones,
    name_find,
    search,
    show_all,
    delete_record,
    add_address,
    add_email,
    birthday,
)

from input_output import Console

# =============================================
#             test 2 (functions)
# =============================================

if __name__ == "__main__":
    filename = "book_test_2.bin"

    Console.output(" ================== test 2 ===============")
    Console.output(GREEN + "     виводимо help" + RESET)
    Console.output(help_page())

    Console.output(GREEN + "\n     додаємо новий контакт" + RESET)
    Console.output(add_contact("Jill", "0677977166"))
    Console.output(GREEN + "     намагаємося повторно додати той самий контакт" + RESET)
    Console.output(add_contact("Jill", "0677977167"))
    Console.output(GREEN + "\n     додаємо дату народження" + RESET)
    Console.output(add_birthday("Jill", "06-11-1995"))
    Console.output(GREEN + "     додаємо контакт з датою народження" + RESET)
    Console.output(add_contact("Bill", "0997058845", "15-03-1999"))

    Console.output(GREEN + "     додаємо контакт у якого 3 телефони та дата народження" + RESET)
    Console.output(
        add_contact("Bill_t", "0997078845", "099 745-12-35", "0964523265", "12-11-2002")
    )

    Console.output(GREEN + "\n     додаємо контакт у якого 4 телефони" + RESET)
    Console.output(
        add_contact("Jill_t", "0677977176", "0956783423", "0669873456", "050 345 22 34")
    )
    Console.output(
        GREEN
        + "\n     намагаємося додати новий номер до контакту, що вже існує, командою add_contact"
        + RESET
    )
    Console.output(add_contact("Jill_t", "0677977188"))
    Console.output(GREEN + "     робимо те саме, але правильно - командою add_phones" + RESET)
    Console.output(add_phones("Jill_t", "0677977188"))
    Console.output(
        GREEN
        + "     а тепер додаємо контакту ще 2 номери (однією командою add_phones)"
        + RESET
    )
    Console.output(add_phones("Jill_t", "0677977155", "0668528526"))

    Console.output(GREEN + "\n     міняємо номер телефону контакту" + RESET)
    Console.output(change_phone("Jill_t", "0677977176", "0954122568"))
    Console.output(
        GREEN + "     намагаємося поміняти номер, що не існує у даного контакту" + RESET
    )
    Console.output(change_phone("Jill_t", "0677977176", "0954122568"))
    Console.output(GREEN + "     намагаємося поміняти номер на такий самий" + RESET)
    Console.output(change_phone("Jill_t", "0954122568", "+380954122568"))

    Console.output(GREEN + "\n     видаляємо один з номерів контакту" + RESET)
    Console.output(del_phone("Jill_t", "0503452234"))
    Console.output(GREEN + "     намагаємося видалити номер, якого не існує" + RESET)
    Console.output(del_phone("Jill_t", "0954122599"))
    Console.output(
        GREEN + "     намагаємося видалити номер контакту, якого нема у списку" + RESET
    )
    Console.output(del_phone("Jill_v", "0954122599"))

    Console.output(GREEN + "\n     додаємо день народження існуючому контакту" + RESET)
    Console.output(add_birthday("Jill_t", "28-03-1968"))

    Console.output(GREEN + "\n     міняємо ім'я існуючого контакту!" + RESET)
    Console.output(change_name("jill_t", "jill_v"))

    Console.output(GREEN + "     ще раз міняємо ім'я контакту!" + RESET)
    Console.output(change_name("Jill_v", "jill_n"))

    Console.output(
        GREEN
        + "     намагаємося поміняти ім'я контакту, але не вказуємо нового імені"
        + RESET
    )
    Console.output(change_name("jill_n"))

    Console.output(GREEN + "\n     видаляємо існуючий контакт" + RESET)
    Console.output(delete_record("jill_n"))

    Console.output(GREEN + "     намагаємося видалити контакт, що вже не існує" + RESET)
    Console.output(delete_record("jill_t"))

    Console.output(GREEN + "\n     шукаємо всі записи, де є рядок '45'" + RESET)
    Console.output(search("45"))
    Console.output(GREEN + "     шукаємо всі записи, де є рядок 'ill'" + RESET)
    Console.output(search("ill"))
    Console.output(GREEN + "     забуваємо ввести строку для пошуку" + RESET)
    Console.output(search())
    Console.output(GREEN + "     шукаємо контакт за іменем (рудимент з минулих ДЗ)" + RESET)
    Console.output(name_find("bill_t"))

    Console.output(GREEN + "\n     друкуємо список контактів" + RESET)
    Console.output(show_all())

    Console.output(GREEN + "     зберігаємо список контактів" + RESET)
    Console.output(book.write_contacts_to_file("book_test_2.bin"))

    # відновлення контактів з файлу успішно працює в тесті класів та в самому боті

    Console.output(GREEN + "     видаляємо 2 контакти зі списку" + RESET)
    Console.output(delete_record("Jill"))
    Console.output(delete_record("Bill"))

    Console.output(GREEN + "     друкуємо список контактів" + RESET)
    Console.output(show_all())

    Console.output(GREEN + "     відновлюємо список контактів з файлу" + RESET)

    add_contact("jill", "+380677977166", "12-11-1995")
    add_contact("Bill", "+380997058845", "15-03-1999")

    book = book.read_contacts_from_file("book_test_2.bin")

    Console.output(GREEN + "     друкуємо відновлений список контактів" + RESET)
    Console.output(show_all())

    Console.output(GREEN + "\n     додаємо кілька нових контактів" + RESET)
    Console.output(add_contact("Person_0", "(099)475-71-22"))
    Console.output(add_contact("Person_9", "(099)475-31-11"))
    Console.output(add_contact("Person_1", "(066)4525588", "14-11-1998"))
    Console.output(add_contact("Person_7", "099 225 55 66", "22-04-1870"))
    Console.output(add_contact("Person_2", "0675468899", "0997061212", "16-11-2001"))
    Console.output(add_contact("Person_6", "0987654321", "15-11-1999"))
    Console.output(add_contact("Person_3", "+38(098)221-15-44", "14-11-1988"))
    Console.output(add_contact("Person_8", "0958645548", "08-11-1967"))
    Console.output(add_contact("Person_4", "+380664589955", "07-11-1968"))
    Console.output(add_contact("Person_5", "674567890", "0660554488", "13-11-2005"))

    Console.output(GREEN + "     а тепер додаємо контакту, що НЕ існує номер телефону" + RESET)
    Console.output(add_phones("Jill_e", "0677977155"))

    Console.output(GREEN + "\n     додаємо день народження контакту, що НЕ існує" + RESET)
    Console.output(add_birthday("Jill_e", "28-03-1968"))

    Console.output(GREEN + "\n     додаємо e-mail'и" + RESET)
    Console.output(add_email("person_4", "person_4@gmail.com"))
    Console.output(add_email("person_4", "person_4_plus@gmail.com"))
    Console.output(add_email("person_5", "person_5@gmail.com"))
    Console.output(add_email("person_8", "person_8@gmail.com"))

    Console.output(GREEN + "\n     додаємо адресу" + RESET)
    Console.output(add_address("person_5", "Київ, пр.Берестейський, 73"))

    Console.output(GREEN + "\n     додаємо контакт в якого тільки ім'я" + RESET)
    Console.output(add_contact("helen"))

    Console.output(GREEN + "\n     додаємо йому e-mail" + RESET)
    Console.output(add_email("helen", "helen@gmail.com"))

    Console.output(GREEN + "\n     друкуємо список контактів по 10 рядків на сторінку" + RESET)
    # Console.output(show_all(10)

    Console.output(add_contact("Person_15", "789544555550"))

    Console.output(show_all())

    # Console.output(GREEN + "\n     контакти, в яких день народження " + RESET)
    # result = get_birthdays_on_date(book, 7)
    # Console.output(result)

    Console.output(birthday(7))
    # Console.output(help_page())

    Console.output(GREEN + "\n     міняємо ім'я існуючого контакту!" + RESET)
    Console.output(change_name("Person_5", "Jill_5"))

    Console.output(show_all())