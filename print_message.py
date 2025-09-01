import win32print
import win32ui

def print_message(message):
    printer_name = win32print.GetDefaultPrinter()
    hprinter = win32print.OpenPrinter(printer_name)
    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(printer_name)
    hdc.StartDoc("Print Message")
    hdc.StartPage()
    hdc.TextOut(100, 100, message)
    hdc.EndPage()
    hdc.EndDoc()
    hdc.DeleteDC()
    win32print.ClosePrinter(hprinter)

if __name__ == "__main__":
    print_message("Hi, I am Bali")