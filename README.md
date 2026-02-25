# Automatic Invoice Printer
### Video Demo: https://youtu.be/G1AkvJPc28Q
### Description:

#### Purpose of this program:
This program aims to handle printing an invoice automatically. Whether you're a freelancer or need to show somebody how much they owe you, with this program you won't have to open Adobe Acrobat or Word; instead, this program will handle the process of making the PDF for you. All you need is this program, its dependencies (which you can see in the "requirements.txt" file), and the information you want to input.

#### How to open:
In order to open the program, download the current version of Python, open a CLI (command line interface), and navigate into the "project" folder which contains the program "project.py". Then execute "python project.py" and the program should start.

#### After opening:
After opening the file, you will be met with a welcome message that will instruct you to either press Enter to start the program or to press Ctrl+D to close the program.

#### Under the hood:
Inside the Python file, we can see that a simple input function waits for any input while trying to catch any EOFErrors to end the program via sys.exit(). So actually, you can type whatever you want and then hit Enter; as long as you don't type Ctrl+D, it won't affect the program.

#### How to use the program:
After pressing Enter, you will be instructed again to press Enter without inputting anything else to end the data input and move on after you have input your data, or to press Ctrl+D to exit the program. Also, you're not supposed to enter whole sentences like "I want to input 'chair'"; instead, only input the name of the item you sold and want to put on the invoice, like "chair".

After typing "chair" and pressing Enter, you will be prompted for the cost of the item in Euros. Enter a positive number, either an integer like "1" or a float like "1.2", and press Enter to confirm your input. If you don't put in a valid number, the program will prompt you again. After inputting your item cost, like "100", the program will prompt you for how many of those items (in this example, the chair) you sold. Again, type in a number that can be converted to a float, like "5", and press Enter.

Now the program repeats the process and asks you for your next item. You can input as many items as you like. Once you have typed in another item like "desk", the program will prompt you, as before, for the item cost and quantity. After you have input all your items and the program prompts you for the next line item, simply press Enter without typing anything else. The program will then immediately print the finished PDF invoice for you. Then it will tell you "Invoice_(number).pdf is done!", whereby (number) is a random 7-digit number. The PDF should now be visible in the project folder.

#### The PDF:
The PDF itself is very simple. At the top, you have the centered headline "Invoice", then you have 4 rows with "Item Description" (the line item you input), "Quantity" (the quantity you input), the "Unit Price" (the item cost you literally typed in), and the "Total".

In our example, the item description would be "chair", the quantity would be 5.0, the unit price 100.00 EUR, and the total for that row would be 500.00 EUR (5.0 * 100.00). Then, beneath the item list in the right-hand corner, we have the subtotal, which consists of all row totals combined. Beneath that is the VAT (value-added tax), which sits at 19% here in Germany. So, 19% of the subtotal (95.00 EUR in our example) is added in taxes. The tax burden is, of course, passed down to the consumer, so the final total which the consumer needs to pay is 595.00 EUR, which is printed on the PDF for you.

#### Under the hood:
The program calls the get_user_input() function in main(), which creates an empty list named item_list in which it will store and return the data the user types in. Then, a flag to check if a break was enabled is set to False. The program prompts the user for the next line item while catching any EOFError exceptions. If the user gives an empty string, the break_set flag is set to True, so the program breaks out of the data input loop.

After the line item is input and the break_set flag is False, the program will prompt the user for the item cost and then the quantity, while converting the input to a float and checking if it's greater than 0. It catches ValueErrors and prompts the user again in an infinite loop if they continue to make the same mistake. When the user doesn't type in a positive number, the program will give a user-friendly error message which explains they have to put in a positive number and then prompts the user again. After the user inputs a valid quantity, the program puts all the input data into a dictionary and then appends the dictionary to the list called item_list. After all the data is input and the user gives an empty string at the line item prompt, the program breaks out of the infinite input loop and returns the item_list.

Next, the main() function calls the calc_total_and_tax() function, which receives the item_list we just created. Inside the calc_total_and_tax() function, a variable named before_tax_total is created and set to 0. This is where we will store the value of all items combined. To calculate this value, we open a for loop that iterates over every dictionary in item_list and multiplies the item quantity by the item cost. Then the tax is calculated by multiplying the before_tax_total with the VAT, which is a global variable with the value 0.19 (19%). So, in the tax variable, a value is stored which is 19% of the before_tax_total. To calculate the after_tax_total, the tax is added to the before_tax_total. Then the before_tax_total, the tax, and the after_tax_total are returned as a tuple, which gets immediately unpacked in main.

Next, in main, the print_pdf() function is called and handed the item_list, the before_tax_total, the tax, and the after_tax_total. Inside the print_pdf() function, first, a random number between 1,000,000 and 9,999,999 is created with random.randrange and stored in the variable pdf_number. Then, in the variable pdf_name, an f-string is stored as "Invoice_{pdf_number}.pdf". This will be the name of the created PDF file. The PDF file is given a large random number so that the user can create almost endless new PDFs without worrying about naming conflicts.

Next, with the FPDF() constructor, we create a new class object named pdf to handle the PDF printing. First, we add a page to the PDF, set the font, size, and y-position, and then print the headline "Invoice" in a centered cell. Then we set the y-value further down, set the font size to 12, and print each row headline, like "Item Description" or "Quantity", in a cell that is 52.5 mm wide (which is exactly 1/4 of a DIN A4 page).

Then, for each dictionary in item_list, the line_item, item_quantity, item_cost, and item_total are also printed in a 52.5 mm cell, so that each piece of data is in the correct column. The item_cost and the item_total are rounded to two decimal places so that the value reflects cents. After the item_total is printed, the PDF moves to the next line to print the next dictionary of data. At the end, the font is set to bold and size 11 to print the before_tax_total, the tax, and the after_tax_total at the bottom right of the list. After finishing the PDF, the pdf_name is returned to main, and the f-string "{pdf_name} is done" is printed to tell the user that the process is finished. The program then ends with exit code 0.

