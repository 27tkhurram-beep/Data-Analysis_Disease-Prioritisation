import pandas as pd 
import matplotlib.pyplot as plt

mock_data = {
    "Disease": ["Ebola", "Measles", "Seasonal Flu", "SARS", "Mers"],
    "Transmission_R0": [1.5, 15.0, 1.3, 3.0, 0.8],       
    "Mortality_Rate_Pct": [50.0, 0.1, 0.1, 10.0, 35.0],  
    "Vaccine_Available": [True, True, True, False, False] 
}

df = pd.DataFrame(mock_data)

# SUBPROGRAM: to calculate the prioriity 
def calculate_priority(row):
    """
    Calculating a base threat score which is based on mortality and transmission rate.
    The availability of vaccine will reduce the threat significantly 
    """
    
    # Base threat Formuale, heavily weighing on mortality rate (60%) then transmission rate (40%)
    base_threat = (row["Transmission_R0"] * 0.4) + (row["Mortality_Rate_Pct"] * 0.6)

    # Vaccine modifier: If there is a vaccine available, the threat decreases by 70% and increase by 30% if Mortality >= 10
    if row["Vaccine_Available"] == True:
        final_score = base_threat * 0.3
    elif row["Mortality_Rate_Pct"] >= 10.0:
        final_score = base_threat * 1.3
    else:
        final_score = base_threat * 1.0

    return final_score 

# Initalise and Process the data further 
# Applying the mathematical model to every single row in the dataset 
df["Priority_Score"] = df.apply(calculate_priority, axis = 1)

# Sorting the values so that the most dangerous disease is at the top 
df_sorted = df.sort_values(by="Priority_Score", ascending=False)

# Print out all of the data table 
print("        ----- EXPERIMENTAL SIMULATION: THREAT PRIORITISATION -----")
print(df_sorted[["Disease", "Transmission_R0", "Mortality_Rate_Pct", "Vaccine_Available"]])
print("\nGenerating the graph...")

# GRAPH VISUALS 

# Setting up a canvas 
plt.figure(figsize=(10,6))

# Create the bars on the graph 
colours = ['#8b0000', '#d2691e', '#ff8c00', '#4682b4', '#5f9ea0']
bars = plt.bar(df_sorted["Disease"], df_sorted["Priority_Score"], color = colours, width=0.6)

# Put on the axis labels 
plt.ylabel("Calculated Priority Score", fontweight = "bold")
plt.xlabel("Diseases", fontweight = "bold")
plt.title("Global Health Threat Prioritisation Dashboard", fontsize = 14, fontweight="bold")

# Adding the threat score on top of each bar 
for bar in bars:
    y_value = bar.get_height()
    # Will place the text slightly above the bars for better aesthetic 
    plt.text(bar.get_x() + bar.get_width()/2, y_value + 0.1,
             f'{y_value:.2f}', ha="center", va="bottom", fontweight="bold")
    
# Setting the y limit as we dont want the numbers going beyond the constraints of the graph 
plt.ylim(0, df_sorted["Priority_Score"].max() + 3)

plt.tight_layout()
plt.show()