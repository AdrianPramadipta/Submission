import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the data
day_df = pd.read_csv("final_day.csv")
hour_df = pd.read_csv("final_hour.csv")

# Set the title of the app
st.title("Bike Sharing Data Analysis")

# Create a sidebar for selecting data
option = st.sidebar.selectbox("Select Data to View", ["Daily Usage", "Hourly Usage"])

# Display the selected data
if option == "Daily Usage":
    st.subheader("Daily Bike Usage")
    daily_avg_use = day_df.groupby('weekday')['cnt'].mean().reset_index()

    days_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    daily_avg_use['weekday'] = pd.Categorical(daily_avg_use['weekday'], categories=days_order, ordered=True)

    plt.figure(figsize=(10, 5))
    sns.barplot(x='weekday', y='cnt', data=daily_avg_use, color='skyblue')
    plt.title('Average use per day')
    plt.xlabel('day')
    plt.ylabel('Average')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    st.pyplot(plt)
    st.write("This graph shows the average bike usage per day of the week.")

elif option == "Hourly Usage":
    st.subheader("Hourly Bike Usage")
    hourly_avg_use = hour_df.groupby('hr')['cnt'].mean().reset_index()
    plt.figure(figsize=(10, 5))
    plt.bar(hourly_avg_use['hr'], hourly_avg_use['cnt'], color='skyblue')
    plt.title('Average Use Per Hour')
    plt.xlabel('Hour')
    plt.ylabel('Average Use')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    st.pyplot(plt)
    st.write("This graph shows the average bike usage per hour of the day.")
