import sys
import random
from fpdf import FPDF

VAT = 0.19

def main():

    print("###################################################\nWelcome to the automatic Invoice Printer!\nJust put in your information and the program will\nprint a PDF invoice for you. Press enter to start or\npress Ctrl+D to exit.\n###################################################")
    try:
        _ = input("\nInput: ")
    except EOFError:
        sys.exit("\n--Exited with Ctrl+D--")
    else:
        item_list = get_user_input()
        before_tax_total, tax, after_tax_total = calc_total_and_tax(item_list)
        pdf_name = print_pdf(item_list, before_tax_total, tax, after_tax_total)
        print(f"\n{pdf_name} is done!")

def get_user_input():

    item_list = []

    break_set = False
    print("\n--> Press enter to end data input or press Ctrl+D to exit.\n--> Do not enter sentences.\n")
    while True:

        try:
            line_item = input("\nWhat is the next line item? ")
            if line_item == "":
                break_set = True
                break
            if break_set == False:
                while True:
                    try:
                        item_cost = float(input("\nHow much does that item cost in Euros? "))
                        if item_cost > 0:
                            break
                        else:
                            print("\n--Enter a positive number--")
                    except ValueError:
                        print("\n--Enter a positive number--")
                        continue
                while True:
                    try:
                        item_quantity = float(input("\nHow many of those items got sold? "))
                        if item_quantity > 0:
                            break
                        else:
                            print("\n--Enter a positive number--")
                    except ValueError:
                        print("\n--Enter a positive number--")
                        continue
                item_dict = {"line_item": line_item, "item_cost": item_cost, "item_quantity": item_quantity}
                item_list.append(item_dict)
        except EOFError:
            sys.exit("\n--Exited with Ctrl+D--")


    return item_list



def calc_total_and_tax(item_list):

    before_tax_total = 0

    for item_dict in item_list:
        before_tax_total += float(item_dict['item_quantity']) * float(item_dict['item_cost'])

    tax = before_tax_total * VAT

    after_tax_total = before_tax_total + tax

    return before_tax_total, tax, after_tax_total


def print_pdf(item_list, before_tax_total, tax, after_tax_total):

    pdf_number = random.randrange(1000000, 9999999)
    pdf_name = f"Invoice_{pdf_number}.pdf"

    pdf = FPDF()

    pdf.add_page()
    pdf.set_font("helvetica", size=50)
    pdf.set_y(15)
    pdf.cell(0, 30, "Invoice", align="C")
    pdf.set_y(50)
    pdf.set_font("helvetica", size=12)
    pdf.cell(52.5, 10, "Item Description")
    pdf.cell(52.5, 10, "Quantity")
    pdf.cell(52.5, 10, "Unit Price")
    pdf.cell(52.5, 10, "Total", new_x="LMARGIN", new_y="NEXT")

    for item in item_list:

        item_total = float(item['item_quantity']) * float(item['item_cost'])

        pdf.cell(52.5, 10, f"{item['line_item']}")
        pdf.cell(52.5, 10, f"{item['item_quantity']}")
        pdf.cell(52.5, 10, f"{round(item['item_cost'], 2):.2f} EUR")
        pdf.cell(52.5, 10, f"{round(item_total, 2):.2f} EUR", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("helvetica", style="B", size=11)
    pdf.cell(0, 10, f"Subtotal: {round(before_tax_total, 2):.2f} EUR", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"VAT: {round(tax, 2):.2f} EUR", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Total: {round(after_tax_total, 2):.2f} EUR", align="R", new_x="LMARGIN", new_y="NEXT")


    pdf.output(pdf_name)

    return pdf_name






if __name__ == '__main__':
    main()
