import json
# PLAZA_ID = {"001101": {"Facility": "Suncoast Parkway","Vendor": "Infinity","Plaza Name": "SR589 Oak Hammock Main NB MP49","Building #": "8091"}
#
#
#     "001102": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Oak Hammock Main SB MP49",
#         "Building #": "8091"
#     },
#
#     '8091': {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Oak Hammock Main NB, SB MP49",
#         "Plaza ID(s)": "1101, 1102",
#     },
#
#     "49": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Oak Hammock Main NB, SB MP49",
#         "Plaza ID(s)": "1101, 1102",
#         "Building #": "8091"
#     },
#
#     "001111": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Sugarmill Main NB MP57",
#         "Building #": ""
#     },
#
#     "001112": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Sugarmill Main SB MP57",
#         "Building #": ""
#     },
#
#     "57": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Sugarmill Main NB, SB MP57",
#         "Plaza ID(s)": "1111, 1112",
#         "Building #": ""
#     },
#
#
#     "001121": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Lecanto Main NB MP65",
#         "Building #": ""
#     },
#
#     "001122": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Lecanto Main SB MP65",
#         "Building #": ""
#     },
#
#     "65": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Lecanto Main NB, SB MP65",
#         "Plaza ID(s)": "1121, 1122",
#         "Building #": ""
#     },
#
#     "001201": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Spring Hill Main NB MP32",
#         "Building #": ""
#     },
#
#     "001202": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Spring Hill Main SB MP32",
#         "Building #": ""
#     },
#
#     "32": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Spring Hill Main NB, SB MP32",
#         "Plaza ID(s)": "1201, 1202",
#         "Building #": ""
#     },
#
#     "001211": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 County Line Rd NBOn MP37",
#         "Building #": "7145"
#     },
#
#     '7145': {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 County Line Rd NBOn MP37",
#         "Plaza ID(s)": "1211"
#     },
#
#     "001212": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 County Line Rd SBOff MP37",
#         "Building #": "7135"
#     },
#
#     '7135': {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 County Line Rd SBOff MP37",
#         "Plaza ID(s)": "1212"
#     },
#
#     "37": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 County Line Rd NBOn, SBOff MP37",
#         "Plaza ID(s)": "1211, 1212",
#         "Building #": "7135, 7145"
#     },
#
#     "001221": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 SR50 NBOff MP46",
#         "Building #": "7140"
#     },
#
#     '7140': {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 SR50 NBOff MP46",
#         "Plaza ID(s)": "1221"
#     },
#
#     "001222": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 SR50 SBOn MP46",
#         "Building #": "7139"
#     },
#
#     '7139': {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 SR50 SBOn MP46",
#         "Plaza ID(s)": "1222"
#     },
#
#     "46": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 SR50 SBOn MP46",
#         "Plaza ID(s)": "1221, 1222",
#         "Building #": "7139, 7140"
#     },
#
#     "001301": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Anclote Main NB MP21",
#         "Building #": ""
#     },
#
#     "001302": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Anclote Main SB MP21",
#     },
#
#     "21": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Anclote Main SB MP21",
#         "Plaza ID(s)": "1301, 1302",
#     },
#
#     "001311": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Ridge Road NBOn MP25",
#     },
#
#     "001312": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Ridge Road SBOff MP25",
#     },
#
#     "25": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Ridge Road NBOn ,SBOff MP25",
#         "Plaza ID(s)": "1311, 1312",
#     },
#
#     "001321": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 SR54 NBOff MP19",
#     },
#
#     "001322": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 SR54 SBOn MP19",
#     },
#
#     "19": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 SR54 NBOff, SBOn MP19",
#         "Plaza ID(s)": "1321, 1322",
#     },
#
#     "001331": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Van Dyke Rd NBOn MP14",
#     },
#
#     "001332": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Van Dyke Rd SBOff MP14",
#     },
#
#     "14": {
#         "Facility": "Suncoast Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Van Dyke Rd SBOff MP14",
#         "Plaza ID(s)": "1331, 1332",
#     },
#
#     "001401": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Sugarwood Main NB MP11",
#     },
#
#     "001402": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Sugarwood Main SB MP11",
#     },
#
#     "001403": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Sugarwood Main NB MP11",
#     },
#
#     "001404": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Sugarwood Main SB MP11",
#     },
#
#     "11": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Sugarwood Main NB, SB MP11",
#         "Plaza ID(s)": "1401, 1402, 1403, 1404",
#     },
#
#     "001411": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Hutchison Rd NBOn MP12",
#     },
#
#     "001412": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Hutchison Rd SBOff MP12",
#     },
#
#     "12": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Hutchison Rd NBOn, SBOff MP12",
#         "Plaza ID(s)": "1411, 1412",
#     },
#
#     "001421": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Gunn Hwy NBOn MP9",
#     },
#
#     "001422": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Gunn Hwy SBOff MP9",
#     },
#
#     "9": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Gunn Hwy NBOn, SBOff MP9",
#         "Plaza ID(s)": "1421, 1422",
#     },
#
#     "001431": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Wilsky BI NBOn MP8",
#     },
#
#     "001432": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Wilsky BI SBOff MP8",
#     },
#
#     "8": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Wilsky BI NBOn ,SBOff MP8",
#         "Plaza ID(s)": "1431, 1432",
#     },
#
#     "001501": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Anderson Main NB MP6",
#     },
#
#     "001502": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Anderson Main SB MP69",
#     },
#
#     "001503": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Anderson Main NB MP6",
#     },
#
#     "001504": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Anderson Main SB MP69",
#     },
#
#     "001505": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Anderson Main NB MP6",
#     },
#
#     "001506": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Anderson Main SB MP6",
#     },
#
#     "001511": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Waters Av SBOn MP6",
#     },
#
#     "001512": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Waters Av NBOff MP6",
#     },
#
#     "6": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Anderson Main NB, SB",
#         "Plaza ID(s)": "1431, 1432",
#     },
#
#     "001521": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Hillsborough Av SBOn MP4",
#     },
#
#     "001522": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Hillsborough Av NBOff MP4",
#     },
#
#     "4": {
#         "Facility": "Veterans Expressway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR589 Hillsborough Av NBOff, SBOn MP4",
#         "Plaza ID(s)": "1521, 1522",
#     },
#
#     "001600": {
#         "Facility": "Polk Parkway",
#         "Vendor": "Xerox",
#         "Plaza Name": "Eastern Barrier MP21",
#     },
#
#
#     "21.5": {
#         "Facility": "Polk Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "Eastern Barrier MP21",
#         "Plaza ID(s)": "1600",
#     },
#
#     "001641": {
#         "Facility": "Polk Parkway",
#         "Vendor": "Raytheon",
#         "Plaza Name": "SR570 Pace Road EBOn MP23",
#     },
#
#     "001642": {
#         "Facility": "Polk Parkway",
#         "Vendor": "Raytheon",
#         "Plaza Name": "SR570 Pace Road WBOff MP23",
#     },
#
#     "23": {
#         "Facility": "Polk Parkway",
#         "Vendor": "Raytheon",
#         "Plaza Name": "SR570 Pace Road EBOn, WBOff MP23",
#         "Plaza ID(s)": "1641, 1642",
#     },
#
#     "001700": {
#         "Facility": "Polk Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "Central Barrier MP13",
#     },
#
#     "13": {
#         "Facility": "Polk Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "Central Barrier MP13",
#         "Plaza ID(s)": "1700",
#     },
#
#
#     "001701": {
#         "Facility": "Polk Parkway",
#         "Vendor": "Infinity",
#         "Plaza Name": "SR 540 East-West",
#     },
#
# }

database_filename = r'C:\Users\username\Desktop\Projects\App_Database.txt'
with open(database_filename) as file:
    PASSWORDS = json.load(file)


def save():
    with open(database_filename, 'w') as f:
        json.dump(PASSWORDS, f, sort_keys=True, indent=4)

