import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Given dictionaries
clinton = {
    "tax": 9,
    "president": 6,
    "police": 5,
    "taxes": 4,
    "black": 3,
    "obama": 3
}

trump = {
    "obama": 12,
    "clinton": 11,
    "president": 9,
    "hillary": 7,
    "nuclear": 4
}

week = {
    "hillaryclinton": 399990,
    "trump": 267766,
    "hillary": 131545,
    "donald": 99249,
    "realdonaldtrump": 66453,
    "president": 58325,
    "clinton": 56073,
    "taxes": 20088,
    "tax": 15288,
    "obama": 17074,
    "black": 13230,
    "police": 11086,
    "nuclear": 7434
}

# Color mapping
color_mapping = {
    "tax": "blue",
    "taxes": "blue",
    "hillaryclinton": "red",
    "hillary": "red",
    "clinton": "red",
    "donald": "green",
    "trump": "green",
    "realdonaldtrump": "green",
    "obama": "yellow",
    "black": "black",
    "police": "purple",
    "nuclear": "pink",
    "president": "orange"
}

def get_colors_for_dict(data_dict):
    return [color_mapping.get(key, "grey") for key in data_dict.keys()]

# Create bar graph for Clinton
fig_clinton = go.Figure([go.Bar(x=list(clinton.keys()), y=list(clinton.values()), marker_color=get_colors_for_dict(clinton))])
fig_clinton.update_layout(title='Clinton Keywords Frequency')
fig_clinton.show()

# Create bar graph for Trump
fig_trump = go.Figure([go.Bar(x=list(trump.keys()), y=list(trump.values()), marker_color=get_colors_for_dict(trump))])
fig_trump.update_layout(title='Trump Keywords Frequency')
fig_trump.show()

# Create bar graph for Week
fig_week = go.Figure([go.Bar(x=list(week.keys()), y=list(week.values()), marker_color=get_colors_for_dict(week))])
fig_week.update_layout(title='Week Keywords Frequency')
fig_week.show()
# Create a combined bar graph with all three dictionaries
combined_fig = make_subplots(rows=1, cols=3, subplot_titles=('Clinton', 'Trump', 'Week'))

combined_fig.add_trace(go.Bar(x=list(clinton.keys()), y=list(clinton.values()), marker_color=get_colors_for_dict(clinton), name="Clinton"), row=1, col=1)
combined_fig.add_trace(go.Bar(x=list(trump.keys()), y=list(trump.values()), marker_color=get_colors_for_dict(trump), name="Trump"), row=1, col=2)
combined_fig.add_trace(go.Bar(x=list(week.keys()), y=list(week.values()), marker_color=get_colors_for_dict(week), name="Week"), row=1, col=3)

combined_fig.update_layout(title='Combined Keywords Frequency')
combined_fig.show()