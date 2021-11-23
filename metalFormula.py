import time

while True:
    print("")
    print("Type 0 to Quit.")
    print("Type 1 for W To Bill rate.")
    print("Type 2 for W. Bill & Bill Invoice.")
    print("Type 3 for Metal Formula.")
    query = input(":- ")
    if "1" in query:
        print("##############")
        print("W To Bill Rate")
        print("##############")
        print('')
        
        rate = int(input("W Rate:- "))
        tax = 112
        WoutGST = round((rate*100)/tax, 2)
        WiGST = round(((WoutGST*18)/100)+WoutGST, 2)
        time.sleep(1)

        print("Without GST:--", WoutGST)
        print("With GST(18%):--", WiGST)


    ###############################################

    elif "2" in query:
        print("############")
        print("Bill Invoice")
        print("############")
        print('')

        iRate = float(input("Item rate:- "))
        iQuantity = float(input("Item quantity:- "))
        tax = int(input("GST Tax %:- "))
        WithOuttax = iRate*iQuantity
        print("")
        print("")
        
        print("Without Tax Value:- ",WithOuttax)

        
        GSTrate = (WithOuttax*tax)/100
        print("GST Tax Value:-", GSTrate)

        nInvoiceValue = round(WithOuttax + GSTrate)
        print("Net Invoice Value:- ", nInvoiceValue)

#############################################################
        print("")
        print("############")
        print("   W. Bill  ")
        print("############")

        BillPercentage = int(input("Bill Percentage:- "))
        GVWL = int(input("Goods Value With Labour:- "))

        taxValue = round((GSTrate/tax)*BillPercentage)
        print("Bill Of Percentage Amount:- ",taxValue)
        nTotal = GVWL+taxValue
        time.sleep(1)
        print("Net Bill Amount:- ",nTotal)
        print("")
        print("")

##############################################################

        while True:
            yN = input("Do you want to change value(y/n): ")
            if "y" in yN:
                iRate = float(input("Item rate:- "))
                iQuantity = float(input("Item quantity:- "))
                WithOuttax = iRate*iQuantity
                GSTrate = (WithOuttax*tax)/100
                nInvoiceValue = round(WithOuttax + GSTrate)
                taxValue = round((GSTrate/tax)*BillPercentage)
                nTotal = GVWL+taxValue
                time.sleep(1)

                print("")
                print("Net Invoice Value",nInvoiceValue)
                print("")
                print("Net Bill Amount(W. Bill Total)",nTotal)
                print("")


            elif "n" in yN:
                time.sleep(1)
                break

    elif "3" in query:
        thickness = float(input("Thickness :- "))
        SideA = float(input("Side A MM :- "))
        SideB = float(input("Side B MM :- "))
        ######################
        KG = (thickness*SideA*SideB*7.86)/1000000
        KG = round(KG, 2)
        time.sleep(1)
        ########################
        print("")              #
        print("KG:",KG, "kg")  #
        print("")              #
        ########################
        time.sleep(1)
        piece = int(input("Total Pieces: "))
        Total_KG = round(KG*piece, 2)
        Total_KG = str(Total_KG)
        print("Total Weight", Total_KG, "Kg")
        totMM = thickness*piece
        Total_incHeight = round(totMM/25.4, 2)
        print("Total Height(in inches):", Total_incHeight)

        while True:
            nY = input("Do you want to try to change pieces(y/n)")
            if "y" in nY:
                print("")
                piece = int(input("Total Pieces: "))
                Total_KG = round(KG*piece, 2)
                Total_KG = str(Total_KG)
                time.sleep(1)

                print("Total Weight", Total_KG, "Kg")
                totMM = thickness*piece
                Total_incHeight = round(totMM/25.4, 2)
                print("Total Height(in inches):", Total_incHeight)

            elif "n" in nY:
                time.sleep(1)
                break

        ############################################################################

    elif "0" in query:
        break

    else:
        print("Invalid Input...")

        print("")
        print("")
        time.sleep(2)
