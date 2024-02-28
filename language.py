import locale

# Determine system language
language, _ = locale.getdefaultlocale()
is_hungarian = language.startswith('hu')

# English error messages
ERROR_NO_DIRECTORY_EN = "Error: No directory provided."
ERROR_INVALID_DIRECTORY_EN = "Error: Invalid directory provided."
ERROR_FILE_NOT_FOUND_EN = "Error: Unable to find the file containing variables ({file_type} extension)."
ERROR_FILE_READING_EN = "Error: An issue occurred while reading the file."
ERROR_CSV_EXPORT_EN = "Error: During export"
SUCCESS_MSG_EN = "Successful export\n{filename}"

# Hungarian error messages
ERROR_NO_DIRECTORY_HU = "Hiba: Nincs megadva könyvtár!"
ERROR_INVALID_DIRECTORY_HU = "Hiba: A megadott könyvtár érvénytelen!"
ERROR_FILE_NOT_FOUND_HU = "Hiba: Nem található a változókat tartalmazó fájl ({file_type} kiterjesztés)."
ERROR_FILE_READING_HU = "Hiba: Probléma merült fel a fájl olvasása során."
ERROR_CSV_EXPORT_HU = "Hiba: Az exportálás során"
SUCCESS_MSG_HU = "Sikeres exportálás!\n{filename}"

# Select error messages based on system language
ERROR_NO_DIRECTORY = ERROR_NO_DIRECTORY_HU if is_hungarian else ERROR_NO_DIRECTORY_EN
ERROR_INVALID_DIRECTORY = ERROR_INVALID_DIRECTORY_HU if is_hungarian else ERROR_INVALID_DIRECTORY_EN
ERROR_FILE_NOT_FOUND = ERROR_FILE_NOT_FOUND_HU if is_hungarian else ERROR_FILE_NOT_FOUND_EN
ERROR_FILE_READING = ERROR_FILE_READING_HU if is_hungarian else ERROR_FILE_READING_EN
ERROR_CSV_EXPORT = ERROR_CSV_EXPORT_HU if is_hungarian else ERROR_CSV_EXPORT_EN
SUCCESS_MSG = SUCCESS_MSG_HU if is_hungarian else SUCCESS_MSG_EN