# imports csv library
import csv

# RICS .CSV
ricsFileName = 'Oboz'
ricsFile = open(ricsFileName + '.csv')
ricsReader = csv.reader(ricsFile)
ricsData = list(ricsReader)

# AMAZON .CSV
amzFileName = 'Amazon'
amzFile = open(amzFileName + '.csv')
amzReader = csv.reader(amzFile)
amzData = list(amzReader)

# Number of possible rows to go through from Amazon's CSV file
numRows = (len(amzData) + 1)
numRowsRics = (len(ricsData) + 1)

# Name of blank output csv file
outputFileName = 'output ' + ricsFileName
outputFile = open(outputFileName+'.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['Brand', 'RICS SKU', 'Size', '', 'AMZ SKU', 'AMZ Qty'])

# Counting Variables, j must start at 1 so it starts in the right row.
j = 1
i = 0

# Main
while i < numRows:
    if j == (numRowsRics-2):
        break
    amzSku = (amzData[i][0])
    amzQty = (amzData[i][3])
    ricsSku = (ricsData[j][2])
    ricsSupplier = (ricsData[j][7])
    ricsSize = (ricsData[j][15])
    ricsWidth = (ricsData[j][16])
    ricsQty = (ricsData[j][18])
    # All possible SKUs on Amazon (so far)
    skuOne = ricsSku + ' ' + ricsSize + ' ' + ricsWidth
    skuTwo = ricsSku + ' ' + ricsSize + ricsWidth
    skuThree = ricsSku + ' ' + ricsSize + '(' + ricsWidth + ')'
    skuFour = ricsSku + ' ' + ricsSize + ' ' + '(' + ricsWidth + ')'
    skuFive = ricsSku + ' ' + ricsSize + ' ' + 'ricsWidth'
    skuSix = ricsSku + ' ' + ricsSize + ricsWidth
    skuSeven = ricsSku + ' ' + ricsSize + '(' + 'ricsWidth' + ')'
    skuEight = ricsSku + ' ' + ricsSize + ' ' + '(' + 'ricsWidth' + ')'
    skuNine = ricsSku + ' ' + ricsSize + ' ' + 'ricsWidth'
    skuTen = ricsSku + ' ' + ricsSize + 'ricsWidth'
    skuEleven = ricsSku + ' ' + ricsSize + '(' + 'ricsWidth' + ')'
    skuTwelve = ricsSku + ' ' + ricsSize + ' ' + '(' + 'ricsWidth' + ')'
    # In case some SKUs are named with EE on Amazon
    if ricsWidth == "2E":
        ricsWidth2 = "EE"
        skuOne = ricsSku + ' ' + ricsSize + ' ' + ricsWidth
        skuTwo = ricsSku + ' ' + ricsSize + ricsWidth
        skuThree = ricsSku + ' ' + ricsSize + '(' + ricsWidth + ')'
        skuFour = ricsSku + ' ' + ricsSize + ' ' + '(' + ricsWidth + ')'
        skuFive = ricsSku + ' ' + ricsSize + ' ' + ricsWidth2
        skuSix = ricsSku + ' ' + ricsSize + ricsWidth2
        skuSeven = ricsSku + ' ' + ricsSize + '(' + ricsWidth2 + ')'
        skuEight = ricsSku + ' ' + ricsSize + ' ' + '(' + ricsWidth2 + ')'
    # In case some SKUs are named with EEE on Amazon
    elif ricsWidth == "3E":
        ricsWidth3 = "EEE"
        skuOne = ricsSku + ' ' + ricsSize + ' ' + ricsWidth
        skuTwo = ricsSku + ' ' + ricsSize + ricsWidth
        skuThree = ricsSku + ' ' + ricsSize + '(' + ricsWidth + ')'
        skuFour = ricsSku + ' ' + ricsSize + ' ' + '(' + ricsWidth + ')'
        skuNine = ricsSku + ' ' + ricsSize + ' ' + ricsWidth3
        skuTen = ricsSku + ' ' + ricsSize + ricsWidth3
        skuEleven = ricsSku + ' ' + ricsSize + '(' + ricsWidth3 + ')'
        skuTwelve = ricsSku + ' ' + ricsSize + ' ' + '(' + ricsWidth3 + ')'
    
    # X = SKU
    # Y = SIZE
    # Z = WIDTH
    # Checking if SKU is in form "X Y Z"
    if amzSku == skuOne:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # Checking if SKU is in form "X YZ"
    elif amzSku == skuTwo:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # Checking if SKU is in form "X Y(Z)"
    elif amzSku == skuThree:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # Checking if SKU is in form "X Y (Z)"
    elif amzSku == skuFour:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # Checking if SKU is in form "X Y ZZ"
    elif amzSku == skuFive:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # Checking if SKU is in form "X YZZ"
    elif amzSku == skuSix:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # Checking if SKU is in form "X Y(ZZ)"
    elif amzSku == skuSeven:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # Checking if SKU is in form "X Y (ZZ)"
    elif amzSku == skuEight:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # Checking if SKU is in form "X Y ZZZ"
    elif amzSku == skuNine:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # Checking if SKU is in form "X YZZZ"
    elif amzSku == skuTen:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # Checking if SKU is in form "X Y(ZZZ)"
    elif amzSku == skuEleven:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # Checking if SKU is in form "X Y (ZZZ)"
    elif amzSku == skuTwelve:
        if amzQty == ricsQty:
            j += 1
            i=0
        elif amzQty == '':
            j += 1
            i=0
        elif amzQty != ricsQty:
            rics = (float(ricsQty))
            amz = (float(amzQty))
            qty = (rics - amz)
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth, '', amzSku, qty])
            j += 1
            i=0
    # If it finds none of those forms and it reaches the end, write the SKU into the CSV file for Amazon listing.
    else:
        if i == 6362:
            outputWriter.writerow([ricsSupplier, ricsSku, ricsSize + ' ' + ' ' + ricsWidth])
            j += 1
            i=0
    i += 1

print("Finished!")
outputFile.close()
