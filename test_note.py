from input_output import Console
from notes import Note, NotesBook
from constants import GREEN, RESET
from main import (
    add_note,
    show_notes,
    add_tag,
    delete_note,
    change_tag,
    delete_tag,
    search_notes,
    edit_note,
)


if __name__ == "__main__":
    note_book = NotesBook()

    Console.output(GREEN + "     створюємо нову нотатку" + RESET)
    Console.output(add_note("000", "If you don’t have "))

    Console.output(GREEN + "     створюємо нову нотатку з #tag" + RESET)
    Console.output(add_note("first", "If you don’t have ", "#3"))

    Console.output(GREEN + "      видаляємо нотатку" + RESET)
    Console.output(delete_note("first"))

    Console.output(GREEN + "     створюємо нову нотатку з #tag" + RESET)
    Console.output(add_note("first", "If you don’t have ", "#3"))

    Console.output(GREEN + "     створюємо нову нотатку з двома #tags" + RESET)
    Console.output(add_note("second", "If you don’t have ", "#3", "#5"))

    Console.output(GREEN + "     додаємо #tags" + RESET)
    Console.output(add_tag("000", "#8"))

    Console.output(GREEN + "     видаляємо #tags" + RESET)
    Console.output(delete_tag("000", "#8"))

    Console.output(GREEN + "     додаємо #tags" + RESET)
    Console.output(add_tag("000", "#88"))

    Console.output(GREEN + "     змінюємо #tags" + RESET)
    Console.output(change_tag("000", "#88", "#99"))

    Console.output(GREEN + "     додаємо #tags" + RESET)
    Console.output(add_tag("000", "#88"))

    Console.output(GREEN + "     шукаємо #tags" + RESET)
    Console.output(search_notes("3"))

    Console.output(GREEN + "     видаляємо #tags" + RESET)
    Console.output(delete_tag("first", "#3"))

    Console.output(GREEN + "     додаємо #tags" + RESET)
    Console.output(add_tag("first", "#888"))

    Console.output(GREEN + "     міняємо content" + RESET)
    Console.output(edit_note("first", "kjhg kjhgf kjhgf 000 fgf"))

    Console.output(GREEN + "     шукаємо #tags" + RESET)
    Console.output(search_notes("000"))

    Console.output(GREEN + "     друкуємо всі notes" + RESET)
    Console.output(show_notes())
