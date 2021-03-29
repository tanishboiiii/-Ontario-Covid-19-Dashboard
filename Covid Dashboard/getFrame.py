import requests
import csv
import pandas as pd
from datetime import date


def fetchDataChangePerDay():
	csvUrl = "https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/8a88fe6d-d8fb-41a3-9d04-f0550a44999f/download/daily_change_in_cases_by_phu.csv"
	req = requests.get(csvUrl)
	urlContent = req.content
	csvFile = open('newCasesPerDay.csv', 'wb')
	csvFile.write(urlContent)
	csvFile.close()

	table = []
	inptFile = csv.DictReader(open("newCasesPerDay.csv"))
	colNames = list(next(inptFile).keys()) 

	table.append(colNames)

	for row in inptFile:
		for key in colNames:
			if row[key] == "":
				row[key] = 0
		table.append(row)

	return table


def recentCasePerDay():
	today = date.today()
	today = today.strftime("%Y-%m-%d")

	allData = fetchDataChangePerDay()
	info = allData[-1]

	recentDate = str(info["Date"])
	cases = info["Total"]

	if today == recentDate:
		recentDate	= "TODAY"

	html = f"<h1 style= \"color: rgb(255, 88, 59);\">{cases}</h1><p style= \"font-style: italic;\">New Covid-19 confirmed cases in ONTARIO, as per {recentDate}</p>"

	return html	



def caseByDayGraph():
	csvUrl = "https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/8a88fe6d-d8fb-41a3-9d04-f0550a44999f/download/daily_change_in_cases_by_phu.csv"
	req = requests.get(csvUrl)
	urlContent = req.content
	csvFile = open('newCasesPerDay.csv', 'wb')
	csvFile.write(urlContent)
	data = pd.read_csv('newCasesPerDay.csv', usecols=['Date','Total'], parse_dates=['Date'])

	data.set_index('Date',inplace=True)
	return data

def caseByDayTableForm():
	csv_url = "https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/8a88fe6d-d8fb-41a3-9d04-f0550a44999f/download/daily_change_in_cases_by_phu.csv"
	req = requests.get(csv_url)
	url_content = req.content
	csv_file = open('newCasesPerDay.csv', 'wb')
	csv_file.write(url_content)
	data = pd.read_csv('newCasesPerDay.csv', usecols=['Date','Total'])
	return data


def fetchDataTotals():
	csvUrl = "https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv"
	req = requests.get(csvUrl)
	url_content = req.content
	csv_file = open('totalCasesPerDay.csv', 'wb')
	csv_file.write(url_content)
	csv_file.close()

	table = []
	inptFile = csv.DictReader(open("totalCasesPerDay.csv"))
	colNames = list(next(inptFile).keys()) 

	table.append(colNames)

	for row in inptFile:
		for key in colNames:
			if row[key] == "":
				row[key] = 0
		table.append(row)

	return table


def recentCaseTotal():
	today = date.today()
	today = today.strftime("%Y-%m-%d")

	allData = fetchDataTotals()
	info = allData[-1]
	recentDate = str(info["Reported Date"])
	cases = int(float(info["Confirmed Positive"]))

	if today == recentDate:
		recentDate	= "TODAY"

	html = f"<h1 style= \"color: rgb(255, 88, 59);\">{cases}</h1><p style= \"font-style: italic;\">Total Covid-19 confirmed cases in ONTARIO, as per {recentDate}</p>"

	return html	

def caseTotalGraph():
	csvUrl = "https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv"
	req = requests.get(csvUrl)
	url_content = req.content
	csv_file = open('totalCasesPerDay.csv', 'wb')
	csv_file.write(url_content)
	data = pd.read_csv('totalCasesPerDay.csv', usecols=["Reported Date", "Confirmed Positive"], parse_dates=["Reported Date"])

	data.set_index("Reported Date",inplace=True)
	return data

def caseTotalTableForm():
	csvUrl = "https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv"
	req = requests.get(csvUrl)
	url_content = req.content
	csv_file = open('totalCasesPerDay.csv', 'wb')
	csv_file.write(url_content)
	data = pd.read_csv('totalCasesPerDay.csv', usecols=['Reported Date','Confirmed Positive'])
	return data
