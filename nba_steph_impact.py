#Goal: Show the impact of steph curry and the warriors they had on the league with the 3 point shooting 

import streamlit as st
from streamlit_scroll_navigation import scroll_navbar
import pandas as pd
import matplotlib.pyplot as plt
import base64
from PIL import Image
import glob

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

st.set_page_config(page_title="Steph's Curry Impact in the NBA", layout="wide")

anchor_ids = ["About this site", "3 Point Revolution Timeline", "Efficency", "Steph’s vs League average", "Shot Chart","Conclusion","References" ]
anchor_labels = ["About this site", "3 Point Revolution Timeline", "Efficency", "Steph’s vs League average", "Shot Chart","Conclusion", "References"]

scroll_navbar(
        anchor_ids,
        key = "navbar2",
        anchor_labels=anchor_labels,
        orientation="horizontal")



hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

top_bar_css = """
<style>
header[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0); /* Fully transparent */
}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)



def set_bg_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

set_bg_local("background4.jpg")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("local.css")

#Secton 1:  Intro
#How Steph Curry changed the NBA 
#A data-driven look at the 3-point revolution.

st.markdown(top_bar_css, unsafe_allow_html=True)


st.title("How Steph Curry Changed the NBA Forever")



st.header("A data-driven look at the 3-point revolution", anchor = "About this site")

st.markdown("This website demonstrates how Python, Streamlit, and data can be used to tell a story — in this case, how a single player transformed the NBA and the game of basketball. We will mainly focus on two stats: 3P (3-Point Field Goals Made) and 3PA (3-Point Attempts).")

st.image("steph_curry.jfif", width=300)



#Section 2:
#Before Curry Era 
#THE NBA Before the Splash
#Show Graphs and Data, pre steph era (2000 to 2009) before Curry was drafted

st.subheader("The NBA Before Steph Curry was Drafted(2000 to 2009)", anchor = "3 Point Revolution Timeline")

st.markdown("Before Steph Curry was drafted, 3-point shooting was a secondary strategy. The graph below shows the league average 3-pointers made and attempted per game. Most teams took fewer than 20 threes per game, relying more heavily on mid-range and paint scoring.")


df_2000_2009 = pd.read_csv("2000_2009_3P_stats.csv")

df_2000_2009["Year"] = df_2000_2009["Season"].str[:4].astype(int)

#Curry’s 3PA/game vs. League 3PA/game
fig1a, ax = plt.subplots(figsize=(10,4))

ax.plot(df_2000_2009["Year"], df_2000_2009["3P"], color="red", label="League 3P per game") 
ax.plot(df_2000_2009["Year"], df_2000_2009["3PA"], color="green", label="League's 3PA per game") 

ax.set_xlabel("Season Start Year")
ax.set_ylabel("Values")
ax.set_title("NBA League-Wide 3-Point Stats per game (2000–2009)")
ax.legend()

st.pyplot(fig1a)

display_option_2000_2009 = st.radio(
    "Show Data between 2000 and 2009?", 
    ('Yes', 'No'),
    index=1
)

if display_option_2000_2009 == 'Yes':
    st.dataframe(df_2000_2009, column_config={"3P": {"alignment": "right"},"3PA": {"alignment": "right"} })

else:
    st.write("")






#Section 3:
#Curry before the 1st championship (2009 to 2015)

st.header("Curry's Rise(2009 to 2015)")
st.markdown("When Steph Curry entered the league, his deep range and quick release began to change how teams played. This period captures the beginning of the shift. Comparing 2000–2015, you can see how 3P and 3PA steadily increased—but notice the jump around 2015, the year Curry won MVP.")


df_2000_2015 = pd.read_csv("2000_2015_3P_stats.csv")
curry_df = pd.read_csv("steph_curry_per_game.csv")

df_2000_2015["Year"] = df_2000_2015["Season"].str[:4].astype(int)

#Curry’s 3PA/game vs. League 3PA/game
fig1b, ax = plt.subplots(figsize=(10,5))

ax.plot(df_2000_2015["Year"], df_2000_2015["3P"], color="red", label="League 3P per game") 
ax.plot(df_2000_2015["Year"], df_2000_2015["3PA"], color="green", label="League's 3PA per game") 

ax.set_xlabel("Season Start Year")
ax.set_ylabel("Values")
ax.set_title("NBA League-Wide 3-Point Stats per game (2009–2015)")
ax.legend()

#st.pyplot(fig1b)


df_2000_2015["Year"] = df_2000_2015["Season"].str[:4].astype(int)
curry_df["Year"] = curry_df["Season"].str[:4].astype(int)


df1 = df_2000_2015[(df_2000_2015["Year"] >= 2000) & (df_2000_2015["Year"] <= 2009)]
df2 = df_2000_2015[(df_2000_2015["Year"] > 2009) & (df_2000_2015["Year"] <= 2015)]

curry_sub_stats = curry_df[(curry_df["Year"] > 2009) & (curry_df["Year"] <= 2015)]


fig, ax = plt.subplots(figsize=(10,5))

ax.plot(df1["Year"], df1["3P"], color="red", label="3P (2000-2009)")
ax.plot(df2["Year"], df2["3P"], color="blue", label="3P (2009-2015)")

# Plot 3PA
ax.plot(df1["Year"], df1["3PA"], color="red", linestyle="--", label="3PA (2000-2009)")
ax.plot(df2["Year"], df2["3PA"], color="blue", linestyle="--", label="3PA (2009-2015)")

ax.plot(curry_sub_stats["Year"], curry_sub_stats["3P"], color="green", marker="o", label="Curry 3P (2009-2015)")
ax.plot(curry_sub_stats["Year"], curry_sub_stats["3PA"], color="green", linestyle="--", marker="x", label="Curry 3PA (2009-2015)")



ax.set_xlabel("Season Start Year")
ax.set_ylabel("Values")
ax.set_title("League vs Steph Curry: 3P and 3PA (2000–2015)")
ax.legend()

#st.pyplot(fig)

df_2009_2015 = pd.read_csv("2000_2015_3P_stats.csv")
curry_df_2009_2015 = pd.read_csv("steph_curry_per_game.csv")



df_2009_2015 = df_2009_2015[['Season','3P', '3PA']].copy() 
curry_df_2009_2015 = curry_df_2009_2015[['Season','3P', '3PA']].copy() 


col1, col2 = st.columns(2)
with col1:
    st.pyplot(fig)
with col2:
    st.pyplot(fig1b)





display_option_2009_2015 = st.radio(
    "Show Data between 2009 to 2015?", 
    ('Yes ', 'No '),
    index=1
)

if display_option_2009_2015 == 'Yes ':
    st.markdown("League Stats from 2009 to 2015")
    st.dataframe(df_2009_2015, column_config={"3P": {"alignment": "right"},"3PA": {"alignment": "right"} })
    st.markdown("Curry Stats from 2009 to 2015")
    st.dataframe(curry_df_2009_2015, column_config={"3P": {"alignment": "right"},"3PA": {"alignment": "right"} })

else:
    st.write("")


#Section 4:
#Steph Curry impact from 2015 to 2024 
st.header("The 3 Point Revolution(2015 to 2025)")
st.markdown("This era shows the full impact of Steph Curry and the Warriors. 3-point attempts and makes increase dramatically across the league, and modern offense becomes built around spacing, pace, and shooting.")


df_2000_2025 = pd.read_csv("2015_2025_3P_stats.csv")
df_2015_2025 = pd.read_csv("2015_2025_3P_stats_era.csv")

df_2015_2025["Year"] = df_2015_2025["Season"].str[:4].astype(int)

#Curry’s 3PA/game vs. League 3PA/game
fig1c, ax = plt.subplots(figsize=(10,5))

ax.plot(df_2015_2025["Year"], df_2015_2025["3P"], color="red", label="League 3P per game") 
ax.plot(df_2015_2025["Year"], df_2015_2025["3PA"], color="green", label="League's 3PA per game") 

ax.set_xlabel("Season Start Year")
ax.set_ylabel("Values")
ax.set_title("NBA League-Wide 3-Point Stats per game (2015–2025)")
ax.legend()

#st.pyplot(fig1c)


df_2000_2025["Year"] = df_2000_2025["Season"].str[:4].astype(int)

df1a = df_2000_2025[(df_2000_2025["Year"] >= 2000) & (df_2000_2025["Year"] <= 2009)]
df2a = df_2000_2025[(df_2000_2025["Year"] > 2009) & (df_2000_2025["Year"] <= 2015)]
df3a = df_2000_2025[(df_2000_2025["Year"] > 2015) & (df_2000_2025["Year"] <= 2025)]

fig2, ax = plt.subplots(figsize=(10,5))

ax.plot(df1a["Year"], df1a["3P"], color="red", label="3P (2000-2009)")
ax.plot(df2a["Year"], df2a["3P"], color="blue", label="3P (2009-2015)")
ax.plot(df3a["Year"], df3a["3P"], color="green", label="3P (2015-2025)")

ax.plot(df1a["Year"], df1a["3PA"], color="red", linestyle="--", label="3PA (2000-2009)")
ax.plot(df2a["Year"], df2a["3PA"], color="blue", linestyle="--", label="3PA (2009-2015)")
ax.plot(df3a["Year"], df3a["3PA"], color="green", linestyle="--", label="3PA (2015-2025)")

ax.set_xlabel("Season Start Year")
ax.set_ylabel("Values")
ax.set_title("3P and 3PA (2000–2025)")
ax.legend()

#st.pyplot(fig2)

col1, col2 = st.columns(2)
with col1:
    st.pyplot(fig1c)
with col2:
    st.pyplot(fig2)





display_option_2015_2025 = st.radio(
    "Show Data between 2015 to 2025?", 
    ('Yes ', 'No '),
    index=1
)

if display_option_2015_2025 == 'Yes ':
    st.markdown("League Stats from 2009 to 2015")
    st.dataframe(df_2015_2025, column_config={"3P": {"alignment": "right"},"3PA": {"alignment": "right"} })
    
else:
    st.write("")






st.header("Efficency", anchor ="Efficency")

st.markdown("We now introduce two efficiency statistics used widely in modern analytics:")
st.markdown("*eFG% (Effective Field Goal Percentage)**: Accounts for 3-pointers being worth more than 2-pointers")
st.markdown("**TS% (True Shooting Percentage)**: Includes free throws for a full scoring efficiency measure.")
st.markdown("Both metrics rise from 2000–2025, showing that teams are not only shooting more threes—but scoring more efficiently overall.")



df_2000_2025_league_wide = pd.read_csv("2000_2025_league_stats_pergame.csv")

df_2000_2025_league_wide["Year"] = df_2000_2025_league_wide["Season"].str[:4].astype(int)

fig3, ax = plt.subplots(figsize=(10,4))

#ax.plot(df_2000_2025_league_wide["Year"], df_2000_2025_league_wide["3P"], color="red", label="3P") 
#ax.plot(df_2000_2025_league_wide["Year"], df_2000_2025_league_wide["3PA"], color="green", label="3PA") 
ax.plot(df_2000_2025_league_wide["Year"], df_2000_2025_league_wide["eFG%"], color="red", label="eFG%(Effective Field Goal Percentage)") 
ax.plot(df_2000_2025_league_wide["Year"], df_2000_2025_league_wide["TS%"], color="green", label="TS%(True Shooting Percentage)") 
ax.set_xlabel("Season Start Year")
ax.set_ylabel("Values")
ax.set_title("Efficency scoring over time (2000–2025)")
ax.legend()

st.pyplot(fig3)


display_option_efficency = st.radio(
    "Show efficency data?", 
    ('Yes ', 'No '),
    index=1
)

if display_option_efficency == 'Yes ':
    st.markdown("Efficency scoring data")
    st.dataframe(df_2000_2025_league_wide, column_config={"eFG%": {"alignment": "right"},"TS%": {"alignment": "right"} })
    
else:
    st.write("")




st.header("Steph’s vs League average", anchor ="Steph’s vs League average")

st.markdown("These graphs show how Curry’s 3-point volume and accuracy compare to league averages. He consistently attempts and makes far more threes than the league average, while maintaining elite efficiency.")

df_league_vs_curry = pd.read_csv("curry_vs_league_avg.csv")


df_league_vs_curry["Year"] = df_league_vs_curry["Season"].str[:4].astype(int)

#Curry’s 3PA/game vs. League 3PA/game
fig4, ax = plt.subplots(figsize=(10,5))

ax.plot(df_league_vs_curry["Year"], df_league_vs_curry["Curry_FG3A_per_game"], color="red", label="Curry's 3PA per game") 
ax.plot(df_league_vs_curry["Year"], df_league_vs_curry["League_3PA_per_game"], color="green", label="League's 3PA per game") 

ax.set_xlabel("Season Start Year")
ax.set_ylabel("Values")
ax.set_title("Comparing Curry and the League's 3PA per game")
ax.legend()

#st.pyplot(fig4)

#Curry’s 3PM/game vs. League 3PM/game

fig5, ax = plt.subplots(figsize=(10,5))

ax.plot(df_league_vs_curry["Year"], df_league_vs_curry["Curry_FG3M_per_game"], color="red", label="Curry's 3P per game") 
ax.plot(df_league_vs_curry["Year"], df_league_vs_curry["League_3PM_per_game"], color="green", label="League's 3P per game") 

ax.set_xlabel("Season Start Year")
ax.set_ylabel("Values")
ax.set_title("Comparing Curry and the League's 3P per game")
ax.legend()

#st.pyplot(fig5)


#3-Point Volume Comparison-shows how Curry’s volume increased relative to the league.

#Efficiency Comparison - 
#Curry_FG3_PCT vs. League_3P% over time
fig6, ax = plt.subplots(figsize=(10,5))

ax.plot(df_league_vs_curry["Year"], df_league_vs_curry["Curry_FG3_PCT"], color="red", label="Curry's 3P% per game") 
ax.plot(df_league_vs_curry["Year"], df_league_vs_curry["League_3P%_per_game"], color="green", label="League's 3P% per game") 

ax.set_xlabel("Season Start Year")
ax.set_ylabel("Values")
ax.set_title("Comparing Curry and the League's 3P% per game")
ax.legend()

#st.pyplot(fig6)

col1, col2, col3 = st.columns(3)
with col1:
    st.pyplot(fig4)
with col2:
    st.pyplot(fig5)
with col3:
    st.pyplot(fig6)


display_option_league_vs_curry = st.radio(
    "Show League vs Curry data?", 
    ('Yes ', 'No '),
    index=1
)

if display_option_league_vs_curry == 'Yes ':
    st.markdown("Show League vs Curry data?")
    st.dataframe(df_league_vs_curry, column_config={"Curry_FG3_PCT%": {"alignment": "right"},"League_3P%_per_game%": {"alignment": "right"} })
    
else:
    st.write("")



st.header("Shot Chart", anchor ="Shot Chart")

st.markdown("These shot charts compare Stephen Curry, Damian Lillard, and DeMar DeRozan to show how NBA scoring styles have evolved. Curry represents the shift toward deep, high-volume threes. Lillard follows a similar modern style. DeRozan provides contrast as a midrange-heavy scorer who gradually adapted to today’s spacing era. Notice the dramatic changes to their shots, comparing early into their career and then after the warriors won their title.")

# filepaths (update to your actual filenames)
curry_imgs = {
    "2009-10": "Steph_Curry_shot_chart/Curry_2009.png",
    "2015-16": "Steph_Curry_shot_chart/Curry_2015.png",
    "2023-24": "Steph_Curry_shot_chart/Curry_2023.png"
}
lillard_imgs = {
    "2013-14": "Lillard_shot_chart/Lillard_2013.png",
    "2016-17": "Lillard_shot_chart/Lillard_2016.png",
    "2023-24": "Lillard_shot_chart/Lillard_2023.png"
}
derozan_imgs = {
    "2010-11": "DeRozen_shot_chart/DeRozan_2010.png",
    "2016-17": "DeRozen_shot_chart/DeRozan_2016.png",
    "2021-22": "DeRozen_shot_chart/DeRozan_2023.png"
}

img_width = 400  # increase if you want larger images

st.markdown("### Shot chart comparison — early in their career → after warriors won their title → modern")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Stephen Curry**")
    st.image(list(curry_imgs.values())[0], caption=list(curry_imgs.keys())[0], width=img_width)
    st.image(list(curry_imgs.values())[1], caption=list(curry_imgs.keys())[1], width=img_width)
    st.image(list(curry_imgs.values())[2], caption=list(curry_imgs.keys())[2], width=img_width)

with col2:
    st.markdown("**Damian Lillard**")
    st.image(list(lillard_imgs.values())[0], caption=list(lillard_imgs.keys())[0], width=img_width)
    st.image(list(lillard_imgs.values())[1], caption=list(lillard_imgs.keys())[1], width=img_width)
    st.image(list(lillard_imgs.values())[2], caption=list(lillard_imgs.keys())[2], width=img_width)

with col3:
    st.markdown("**DeMar DeRozan**")
    st.image(list(derozan_imgs.values())[0], caption=list(derozan_imgs.keys())[0], width=img_width)
    st.image(list(derozan_imgs.values())[1], caption=list(derozan_imgs.keys())[1], width=img_width)
    st.image(list(derozan_imgs.values())[2], caption=list(derozan_imgs.keys())[2], width=img_width)



st.subheader("Interactive Shot Chart (Use the slider below to explore how each player's shot chart evolved from season to season).")


st.markdown("Steph Curry Shot Chart")

images = sorted(glob.glob("Steph_Curry_shot_chart/*.png"))

year = st.slider("Season", 2009, 2023, 2009)
img_path = f"Steph_Curry_shot_chart/Curry_{year}.png"
st.image(img_path, width=500, caption=f"Curry Shot Chart {year}")


st.markdown("Demar Derozan shot chart")

images = sorted(glob.glob("DeRozen_shot_chart/*.png"))

year_derozen = st.slider("Season ", 2009, 2023, 2009)
img_path_derozen = f"DeRozen_shot_chart/DeRozan_{year_derozen}.png"
st.image(img_path_derozen, width=500,  caption=f"DeRozen Shot Chart {year_derozen}")



st.markdown("Damian Lillard shot chart")

images = sorted(glob.glob("Lillard_shot_chart/*.png"))

year_Lillard = st.slider("Season  ", 2013, 2023, 2013)
img_path_Lillard = f"Lillard_shot_chart/Lillard_{year_Lillard}.png"
st.image(img_path_Lillard, width=500, caption=f"Lillard Shot Chart {year_Lillard}")




st.header("Conclusion", anchor ="Conclusion")

st.markdown("Steph Curry became the greatest shooter ever and reshaped how the entire NBA plays basketball. Across the league, three-point attempts and makes have risen every single season since Curry entered the league, and the pace of that rise sharply accelerates during the Warriors’ championship years. Teams now space the floor more, shoot earlier in the shot clock, and build offenses around the three in ways that didn’t exist before 2013. This also means, the decrease in midrange shots. Curry’s combination of off-the-dribble threes, deep-range shooting, and constant movement forced defenses to extend far beyond the arc, which in turn encouraged teams to prioritize spacing, shooting, and analytics-driven shot selection. The result: a league-wide shift where the three-pointer is no longer a specialty—it’s the foundation of modern offense. To summarize, Steph Curry didn’t just influence the NBA he also changed its math, strategy, and identity. ")




st.header("References", anchor ="References")
st.subheader("- NBA API for player and league stats ")
st.subheader("- Basketball Reference for historical league averages  ")
st.subheader("- NBA Shot Charts: https://kivanpolimis.com/nba-shot-charts-part-1.html")


