from openpyxl import Workbook
from datetime import datetime

# Create a workbook and sheets
wb = Workbook()
ws_portfolio = wb.active
ws_portfolio.title = "Portfolio Overview"

# Portfolio Overview Headers
ws_portfolio.append([
    "Stock", "No. of Shares", "Buy Price (₦)", "Current Price (₦)",
    "Total Value (₦)", "% of Portfolio"
])

portfolio_data = [
    ["Zenith Bank", 2140, 35, 35, "=B2*D2", "=E2/SUM(E2:E10)"],
    ["GTCO", 1190, 42, 42, "=B3*D3", "=E3/SUM(E2:E10)"],
    ["UBA", 1920, 26, 26, "=B4*D4", "=E4/SUM(E2:E10)"],
    ["Access Bank", 1135, 22, 22, "=B5*D5", "=E5/SUM(E2:E10)"],
    ["SFS REIT", 1050, 95, 95, "=B6*D6", "=E6/SUM(E2:E10)"],
    ["UPDC REIT", 9100, 5.5, 5.5, "=B7*D7", "=E7/SUM(E2:E10)"],
    ["MTNN", 310, 240, 240, "=B8*D8", "=E8/SUM(E2:E10)"],
    ["DANGCEM", 165, 300, 300, "=B9*D9", "=E9/SUM(E2:E10)"],
    ["Nestle", 20, 1200, 1200, "=B10*D10", "=E10/SUM(E2:E10)"],
]

for row in portfolio_data:
    ws_portfolio.append(row)

# Dividend Tracker Sheet
ws_dividends = wb.create_sheet(title="Dividend Tracker")
ws_dividends.append(["Stock", "Dividend/Share (₦)", "Shares Held", "Total Dividend (₦)", "Payment Date", "Status"])

dividend_data = [
    ["Zenith Bank", 4.0, 2140, "=B2*C2", "March & August", "Pending"],
    ["GTCO", 3.2, 1190, "=B3*C3", "March & August", "Pending"],
    ["UBA", 2.8, 1920, "=B4*C4", "August", "Pending"],
    ["Access Bank", 1.8, 1135, "=B5*C5", "August", "Pending"],
    ["SFS REIT", 5.2, 1050, "=B6*C6", "Quarterly", "Pending"],
    ["UPDC REIT", 0.2, 9100, "=B7*C7", "Quarterly", "Pending"],
    ["MTNN", 13.5, 310, "=B8*C8", "June & December", "Pending"],
    ["DANGCEM", 20.0, 165, "=B9*C9", "June", "Pending"],
    ["Nestle", 25.0, 20, "=B10*C10", "May", "Pending"],
]

for row in dividend_data:
    ws_dividends.append(row)

# Income Calendar
ws_calendar = wb.create_sheet(title="Income Calendar")
ws_calendar.append(["Month", "Expected Payout (₦)", "From Stock(s)"])
calendar_data = [
    ["March", "Zenith, GTCO"],
    ["May", "Nestle"],
    ["June", "MTNN, DANGCEM"],
    ["August", "Zenith, GTCO, UBA, Access"],
    ["December", "MTNN, SFSREIT, UPDCREIT"],
]

for month, stocks in calendar_data:
    ws_calendar.append([month, "", stocks])

# Save workbook
file_path = "/mnt/data/Nigerian_Dividend_Portfolio_Tracker.xlsx"
wb.save(file_path)

file_path
