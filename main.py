#!/usr/bin/python3
import base64
import sys
import bson
import pymongo
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font(family='Arial', size=16)
pdf.cell(40, 10, f'{sys.argv[1]} - {sys.argv[2]}')
pdf.output('report.pdf', 'F')

file = open('./report.pdf', 'rb')
encoded_string = base64.b64encode(file.read())
b = bson.Binary(encoded_string)
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['pythia']
table = db['reports']
x = table.insert_one({
    "file": b
    })
print(x.inserted_id, end='')
