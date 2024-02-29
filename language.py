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
CHOOSE_FOLDER_EN = "Select the directory of the Kinco-PLC project"
SAVE_AS_EXPORT_EN = "Save the variables file"

# Hungarian error messages
ERROR_NO_DIRECTORY_HU = "Hiba: Nincs megadva könyvtár!"
ERROR_INVALID_DIRECTORY_HU = "Hiba: A megadott könyvtár érvénytelen!"
ERROR_FILE_NOT_FOUND_HU = "Hiba: Nem található a változókat tartalmazó fájl ({file_type} kiterjesztés)."
ERROR_FILE_READING_HU = "Hiba: Probléma merült fel a fájl olvasása során."
ERROR_CSV_EXPORT_HU = "Hiba: Az exportálás során"
SUCCESS_MSG_HU = "Sikeres exportálás!\n{filename}"
CHOOSE_FOLDER_HU = "Válassza ki a Kinco-PLC projekt könyvtárát"
SAVE_AS_EXPORT_HU = "A változókat tartalmazó fájl mentése"


# GUI text
GUI_CONVERT_EN = "Convert"
GUI_CONVERT_HU = "Konvertálás"
GUI_CONVERT = GUI_CONVERT_HU if is_hungarian else GUI_CONVERT_EN

GUI_CHOOSE_EN = "Choose"
GUI_CHOOSE_HU = "Kiválasztás"
GUI_CHOOSE = GUI_CHOOSE_HU if is_hungarian else GUI_CHOOSE_EN

GUI_TITLE_EN = "Kinco Var Converter"
GUI_TITLE_HU = "Kinco Változó Konvertáló"
GUI_TITLE = GUI_TITLE_HU if is_hungarian else GUI_TITLE_EN

HELP_BTN_EN = "Help"
HELP_BTN_HU = "Segítség"
HELP_BTN = HELP_BTN_HU if is_hungarian else HELP_BTN_HU

# Select error messages based on system language
ERROR_NO_DIRECTORY = ERROR_NO_DIRECTORY_HU if is_hungarian else ERROR_NO_DIRECTORY_EN
ERROR_INVALID_DIRECTORY = ERROR_INVALID_DIRECTORY_HU if is_hungarian else ERROR_INVALID_DIRECTORY_EN
ERROR_FILE_NOT_FOUND = ERROR_FILE_NOT_FOUND_HU if is_hungarian else ERROR_FILE_NOT_FOUND_EN
ERROR_FILE_READING = ERROR_FILE_READING_HU if is_hungarian else ERROR_FILE_READING_EN
ERROR_CSV_EXPORT = ERROR_CSV_EXPORT_HU if is_hungarian else ERROR_CSV_EXPORT_EN
SUCCESS_MSG = SUCCESS_MSG_HU if is_hungarian else SUCCESS_MSG_EN
CHOOSE_FOLDER = CHOOSE_FOLDER_HU if is_hungarian else CHOOSE_FOLDER_EN
SAVE_AS_EXPORT = SAVE_AS_EXPORT_HU if is_hungarian else SAVE_AS_EXPORT_EN
