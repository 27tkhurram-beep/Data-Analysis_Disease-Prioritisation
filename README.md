# Data-Analysis_Disease-Prioritisation

I built this Python project to solve a realistic problem: How do healthcare systems such as the NHS decide which diseases to priritise when multiple outbreaks happen at once? When medical resources (like ICU beds or vaccine manufacturing clinics) are limited, you cannot treat every health threat the same way. This project takes basic outbreak data, runs it through a custom weighted scoring formula, and creates a clear visual dashboard to show decision-makers exactly where to send help first. 

*How It Works & Tools Used*

Instead of using basic python lists and slow, [for] loops, I used industry-standard data science tools to keep the code clean and efficient:
    Pandas: to handle the data structures.
    Matplotlib: to build the visual dashboard 

*Core Pandas Features I Used*:

> DataFrames: I converted my raw data into a Pandas DataFrame, which essentially acts like a powerful, programmatic Excel spreadsheet.

> [.apply()] with [axis=1]: Instead of looping through rows one by one [.apply()] lets me run my scoring formula across the entire dataset at once. Setting [axis=1] is crucial because it tells Pandas to read the data horizontally, looking at the transmission, mortality and vaccine status for one specific disease at a time.

> [.sort_values()]: I used this to automaticcaly sor the dataset from highest score to lowest score [ascending=False], making sure the absolute biggest threat always bubbles up to the very top of the list 

*The Math Behind the Threat Model*

The engine uses a weighted scoring system to figure out how dangerous a disease is to a hospital's infastructure.

1. Base Formula 
I chose to weight Mortality Rate at 60% and Transmission Speed at 40%

>   Base Threat = (Transmission Rate x 0.4) + (Mortality Rate x 0.6)

Why this split?
A highly but contagious mild flu can cause a lot of sick days, but a highly lethal disease will completely overwhelm intensive care units (ICUs) and hospital capacity almost instantly. Therefore, mortality needs to be weighted heavier in an emergency. 

2. Real-World Modifiers (Constraints)

To make the simulation realistic, I added conditional logic to handle actual healthcare constraints:

> Vaccine Availability (True): If a vaccine already exists, the immediate danger drops significantly. The code multiplies the base threat score by [0.3]. I didn;t drop it to 0 becuase manufacturing and distributing vaccines still require resources and time. 

> High Lethality, No Vaccine: If a disease has a mortality rate of 10% or higher and no vaccine exists, it triggers an emergency modifier, multiplying the score by [1.3] to flag it as a critical priority.

*Test Data Used*

I created a synthetic dataset representing different disease progiles to test if the math handles edge cases correctly: 

> Ebola: High mortality (50%) but it has a vaccine. The formula correctly keeps its threat levl balanced because a defence exists 

> Measles: Massive transmission rate of [15.0] but very low mortality. The formula ensures it doesn't cause a false alarm 

> SARS: high transmission, 10% mortality, and no vaccine. This safely triggers the emergency [1.3] modifier, pushing it to the top of the priority list. 

*Designing the Dashboard*

The final part of the project turns the sorted data table into a claen verticle bar chart. I added a few specific layout tweaks to make the grpah easy for anyone to read:

> [ha="center] & [va="bottom]: These alihments settings make sure the exact threat score numbers sit perfectly centered right on top of each bar, rather than looking loopsided or getting buried inside the colours. 

> [plt.ylim()]: This automatically reads the highest score in the dataset and adds a little extra spacing to the top of the graph [max score + 3], ensuring the text labels never get cut off by the border of the chart. 

*What I Learnt*

Building this project showed me how data science works in the real world. It isn't just about plugging numbers into a computer; it's about translating messy real-world problems (like hospital capacity and vaccine logic) into clear mathematical constraints so that organisations can make fast, accurate decisions. 
