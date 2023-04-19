from dash import Dash, html, dcc
from components import ids


def render(app: Dash) -> html.Div:
    Region = [
        "Albany",
        "Atlanta",
        "BaltimoreWashington",
        "Boise",
        "Boston",
        "BuffaloRochester",
        "California",
        "Charlotte",
        "Chicago",
        "CincinnatiDayton",
        "Columbus",
        "DallasFtWorth",
        "Denver",
        "Detroit",
        "GrandRapids",
        "GreatLakes",
        "HarrisburgScranton",
        "HartfordSpringfield",
        "Houston",
        "Indianapolis",
        "Jacksonville",
        "LasVegas",
        "LosAngeles",
        "Louisville",
        "MiamiFtLauderdale",
        "Midsouth",
        "Nashville",
        "NewOrleansMobile",
        "NewYork",
        "Northeast",
        "NorthernNewEngland",
        "Orlando",
        "Philadelphia",
        "PhoenixTucson",
        "Pittsburgh",
        "Plains",
        "Portland",
        "RaleighGreensboro",
        "RichmondNorfolk",
        "Roanoke",
        "Sacramento",
        "SanDiego",
        "SanFrancisco",
        "Seattle",
        "SouthCarolina",
        "SouthCentral",
        "Southeast",
        "Spokane",
        "StLouis",
        "Syracuse",
        "Tampa",
        "TotalUS",
        "West",
        "WestTexNewMexico",
    ]
    return html.Div(
        children=[
            html.H6("Region"),
            dcc.Dropdown(
                options=[{"label": i, "value": i} for i in Region],
                multi=True,
                value=Region,
                id=ids.REGION_DROPDOWN,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_REGIONS,
            ),
        ]
    )
